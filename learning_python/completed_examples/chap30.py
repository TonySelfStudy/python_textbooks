class Super:
    x=0
    def printme(self):
        print(f"In Super printme x={self.x}")

class Sub(Super):
    y=1
    def printme(self):
        Super.printme(self)
        print(f"In Sub printme y={self.y}")



a = Sub();
a.printme()
