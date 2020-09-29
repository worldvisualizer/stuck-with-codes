class Foo(object):
    
    def __init__(self, parameters):
        self.assign = None
        self.parameters = parameters

    @classmethod
    def import_foo(cls, parameters=3):
        inst = cls(parameters)
        inst.assign = 4
        return inst

instance = Foo.import_foo()
print(instance, instance.parameters, instance.assign)
