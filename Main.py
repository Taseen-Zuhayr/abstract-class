from abc import ABC , abstractmethod

class Absclass(ABC):

    def print(self,x):
        print("Pass a value:",x)

    @abstractmethod
    def task(self):
        print("we are in abstract class!it is hidden")

#subclass
class test(Absclass):
    def task(self):
        print("not abstract class and it is not hidden")

#obj creation
x = test()
x.task()