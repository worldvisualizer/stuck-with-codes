from abc import ABC, abstractmethod

# represents some abstract class
class Abstract(ABC):
    DEFAULT_CLASS_VAR = 0
    
    def __init__(self, params):
        self.params = params

    def do_something(self):
        print("doing something")

    @abstractmethod
    def do_method(self):
         raise NotImplementedError('subclass should implement this')

# this class represents nn.Module in pytorch
class Concrete(object):
    DEFAULT_CLASS_VAR = 100

    def __init__(self, another):
        self.another = another

    def forward(self, x):
        print("forward, {}".format(x))

# a base pytorch class representation
class CombinedBase(Abstract, Concrete):
    DEFAULT_CLASS_VAR = 20

    def __init__(self, params):
        super(CombinedBase, self).__init__(params)

    @abstractmethod
    def forward(self, x):
        raise NotImplementedError('subclass should implement this')

# combined concrete pytorch class we will use representation
class CombinedConcrete(CombinedBase):
    DEFAULT_CLASS_VAR = 30

    def __init__(self, params):
        super(CombinedConcrete, self).__init__(params)
        self.network = "network string object ;)"

    def forward(self, x):
        print("Combined Concrete is doing something!", self.network, x)

    def do_method(self):
        print("you really wanted to make this method implemented huh?")


# expected behavior:
# DEFAULT_CLASS_VAR of CombinedConcrete is 30
# CombinedConcrete has self.params and self.another
# CombinedConcrete has do_something() and forward() 
the_class = CombinedConcrete({'training_rate':0.02})
the_class.do_something()
the_class.forward("torched!!")
the_class.do_method()

print("DEFAULT cls var!: ", the_class.DEFAULT_CLASS_VAR)
print("params inst var!: ", the_class.params)
print("another inst var!: ", the_class.another)
print("network inst var!: ", the_class.network)

