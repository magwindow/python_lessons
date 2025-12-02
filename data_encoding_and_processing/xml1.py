'''Преобразование словаря в XML'''
from xml.etree.ElementTree import Element, tostring

def dict_to_xml(tag, d):
    '''Преобразуем простой словарь из пар ключей/значений в XML'''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

s = dict_to_xml('person', {'name': 'Guido', 'age': 56})
print(s)
print(tostring(s))