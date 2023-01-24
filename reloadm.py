import importlib
import time
import module1
print('Hi')
module1.f1(100,20)
#time.sleep(30)
#importlib.reload(module1)
module1.prod(10,2)
print('hello')
print(dir(importlib))
print(help(importlib))