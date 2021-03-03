class AttrDisplay:

    def gatherAttrs(self):

        # x = dir(self)
        # print(f'{len(x)} members --> {x}')
        # for y in x:
        #     print(y)
        #     print(getattr(self, y))

        attrs = []
        for key in sorted(self.__dict__):
            # print(f"{key}: {getattr(self, key)}")
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)

    def __repr__(self):
        return '[*%s: %s*]' % (self.__class__.__name__, self.gatherAttrs())


if __name__ == '__main__':

    class TopTest(AttrDisplay):
        # print('in top test main body')
        count = 0

        def __init__(self):
            # print('in top test init body')

            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X = TopTest()
    print(X)

    Y = SubTest()
    print(Y)

