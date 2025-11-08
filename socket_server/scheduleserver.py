from collections import deque
from select import select
from socket import socket, AF_INET, SOCK_STREAM

# Эток класс представляет общее yield-событие в планировщике
class YieldEvent:
    def handle_yield(self, sched, task):
        pass
    
    def handle_resume(self, sched, task):
        pass
    
# Планировщик задач
class Scheduler:
    def __init__(self):
        self._numtasks = 0 # Общее количество задач
        self._ready = deque() # Задачи, готовые к запуску
        self._read_waiting = {} # Задачи, ждущие чтения
        self._write_waiting = {} # Задачи, ждущие записи
        
    # Опрашивает на события ввода-вывода и перезапускает ждущие задачи
    def _iopoll(self):
        rset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)
            
    def new(self,task):
        '''Добавляет новую запущенную задачу в планировщик'''
        self._ready.append((task, None))
        self._numtasks += 1
        
    def add_ready(self, task, msg=None):
        '''
        Добавляет уже запущенную задачу в очередь готовых.
        msg – это то, что посылается в задачу, когда она
        возобновляется.
        '''
        self._ready.append((task, msg))
        
    # Добавляет задачу во множество чтения
    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)
        
    # Добавляет задачу во множество записи
    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)
        
    def run(self):
        '''Запускает планировщик задач, пока задач не останется'''
        while self._numtasks:
            if not self._ready:
                self._iopoll()
            task, msg = self._ready.popleft()
            try:
                # Запустить корутину к следующему yield
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1
                

# Пример реализации сокетного ввода-вывода на основе корутин
class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes
    
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    
    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)
        

class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data
    
    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)
    
    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)
        

class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock
    
    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)
    
    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)
        
        
# Обертка вокруг объекта сокета для использования с yield
class Socket(object):
    def __init__(self, sock):
        self._sock = sock
    
    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)
    
    def send(self, data):
        return WriteSocket(self._sock, data)
    
    def accept(self):
        return AcceptSocket(self._sock)
    
    def __getattr__(self, name):
        return getattr(self._sock, name)
    

if __name__ == '__main__':
    # Пример функции, использующей генераторы. Это нужно вызывать
    # с использованием line = yield from readline(sock)
    def readline(sock):
        chars = []
        while True:
            c = yield sock.recv(1)
            if not c:
                break
            chars.append(c)
            if c == b'\n':
                break
        return b''.join(chars)
    
    # Эхо-сервер, использующий генераторы
    class EchoServer:
        def __init__(self, addr, sched):
            self.sched = sched
            sched.new(self.server_loop(addr))
            
        def server_loop(self,addr):
            s = Socket(socket(AF_INET, SOCK_STREAM))
            s.bind(addr)
            s.listen(5)
            while True:
                c, a = yield s.accept()
                print('Got connection from ', a)
                self.sched.new(self.client_handler(Socket(c)))
                
        def client_handler(self, client):
            while True:
                line = yield from readline(client)
                if not line:
                    break
                line = b'GOT:' + line
                while line:
                    nsent = yield client.send(line)
                    line = line[nsent:]
            client.close()
            print('Client closed')
            
        
    sched = Scheduler()
    EchoServer(('', 16000), sched)
    sched.run()