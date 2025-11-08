import threading
from contextlib import contextmanager

# Локальное для потока состояние для хранения информации
# об уже полученных блокировках
_local = threading.local()

@contextmanager
def acquire(*locks):
    # Сортирует блокировки по идентификатору объекта
    locks = sorted(locks, key=lambda x: id(x))
    
    # Убеждается, что порядок блокировки ранее
    # приобретенных блокировок не нарушен
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')
    
    # Получает все блокировки
    acquired.extend(locks)
    _local.acquired = acquired
    
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Освобождает блокировки в порядке, обратном их получению
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]
        
        
x_lock = threading.Lock()
y_lock = threading.Lock()

def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')

def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')
            

# t1 = threading.Thread(target=thread_1)
# t1.daemon = True
# t1.start()

# t2 = threading.Thread(target=thread_2)
# t2.daemon = True
# t2.start() 


# Поток-философ
def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.currentThread(), 'eating')
            
# Палочки (представлены блокировками)
NSTICKS = 5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

# Создаем всех философов
for n in range(NSTICKS):
    t = threading.Thread(target=philosopher, args=(chopsticks[n], chopsticks[(n+1) % NSTICKS]))
    t.start()