from inspectors import inspect_all, my_tree

class A(): pass
class B(A): pass
class C(B): pass
class D(): pass
class E(D): pass
class F(E): pass
class G(C, F): pass
class H(): pass
class J(G, H): pass

class Super:
    def hello(self):
        self.data = 'spam'

class Sub(Super):
    def hola(self):
        self.data2 = 'eggs'

if True:
    x = J()
    my_tree(x)

    # x = Super()
    # y = Sub()
    # y.hello()
    # y.hola()
    # #inspect_all(y)
    # my_tree(y)