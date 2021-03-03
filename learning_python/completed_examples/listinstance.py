class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += f'\t{attr}={self.__dict__[attr]}\n'
        return result

    def __str__(self):
        return f"<Instance of {self.__class__.__name__}, " \
               f"address {id(self)}:\n" \
               f"{self.__attrnames()}>"

if __name__ == "__main__":
    from completed import testmixin

    testmixin.tester(ListInstance)