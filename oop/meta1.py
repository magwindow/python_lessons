'''Пользовательские метаклассы'''

class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, clsdict):
        uppercase_attr = {}
        for name, val in clsdict.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)



class Foo(metaclass=UpperAttrMetaclass):
    bar = "bip"

print(hasattr(Foo, "bar"))    
print(hasattr(Foo, "BAR")) 

f = Foo()
print(f.BAR)