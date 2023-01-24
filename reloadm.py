import module1
import time
import importlib
print('Hi')
module1.f1(100,20)
time.sleep(15)
importlib.reload(module1)
module1.prod(10,2)
print('hello')
#print(dir(importlib))
#print(help(importlib))