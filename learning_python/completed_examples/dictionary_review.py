class Super:
    def hello(self):
        self.data1 = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

x = Sub()

print(x.__dict__)

print(x.__class__)

