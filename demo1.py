class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        print 'My name is:', self.name


p = Person('Bill')
p1 = Person('Apple')
print p