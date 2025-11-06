import ast
import inspect

# Узел-посетитель, который "понижает" глобально доступные
# имена в тело функции, делая их локальными переменными.
class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names
        
    def visit_FunctionDef(self, node):
        # Компилируем некие присвоения для понижения регистра констант
        code = '__globals = globals()\n'
        code += '\n'.join(f"{name} = __globals['{name}']" for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')
        # Инъецируем новые инструкции в тело функции
        node.body[:0] = code_ast.body
        # Сохраняем объект функции
        self.func = node
        

# Декоратор, который превращает глобальные имена в локальные
def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        # Пропускаем линии исходного кода перед декоратором @lower_names
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break
            
        src = '\n'.join(srclines[n+1:])
        # Хак, чтобы разобраться с отступами кода
        if src.startswith((' ','\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')
        
        # Трансформируем AST
        cl = NameLower(namelist)
        cl.visit(top)
        # Выполняем модифицированное AST
        temp = {}
        exec(compile(top,'','exec'), temp, temp)
        # Достаем модифицированный объект кода
        func.__code__ = temp[func.__name__].__code__
        return func
    return lower


INCR = 1

@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR
        print(n)
        
countdown(10)
