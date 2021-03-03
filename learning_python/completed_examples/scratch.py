class Yeah(object):
    def __init__(self, name):
        self.name = name
    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        print('__getattribute__ ', item)
        # Calling the super class to avoid recursion
        return super(Yeah, self).__getattribute__(item)
    # Gets called when the item is not found via __getattribute__
    def __getattr__(self, item):
        print('__getattr__ ', item)
        return super(Yeah, self).__setattr__(item, 'orphan')

print('about to create y1')
y1 = Yeah('yes')
print('y1 just created')

y1.name
print('1st foo call')
y1.foo
print('2nd foo call')
y1.foo
y1.goo
y1.__dict__
