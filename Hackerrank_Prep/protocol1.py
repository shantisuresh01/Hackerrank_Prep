'''
Created on Aug 6, 2023

@author: shanti
Description: Just testing the new PEP 544 Protocol and testing an abstract property.
Sort of based on: How to define a property as part of a protocol:
https://stackoverflow.com/questions/69417586/how-to-define-a-property-as-part-of-a-protocol

'''
from typing import  runtime_checkable, Protocol
from abc import abstractproperty

@runtime_checkable
class MyProto(Protocol):
    _foo: str = 'Default'
    @abstractproperty
    def foo(self):
        ''' Read-only attribute foo '''
        #return self._foo

class MyClass():
    @property
    def foo(self):
        return "New implementation"
class MyProto2(MyProto):
    @property
    def foo(selfself):
        print("MyProto2 implementation")

def my_func(c:MyProto) -> None:
    print(c.foo)
    
if __name__ == '__main__':
    var = MyClass()
    my_func(c = var)
    '''
    Maybe we need to sub-class the Protocl after all 
    '''
    var2 = MyProto2()
    my_func(var2)
    