def inspect_all(obj):
    """Inspect and printout information about obj."""

    print(f"{'*'*10} Object type = {type(obj)} {'*'*10}")


    # get values visible to dir
    print('-' * 50)
    print("Contents of dir(obj)")
    print('-'*50)
    for i in dir(obj):
        print(i)
        str1 = f"obj.{i}"
        # todo - change this to get attribute to see if that stops the crashing
        print(f"\t{eval(str1)}")

    # get the dictionary
    print('-' * 50)
    print("Contents of obj.__dict__")
    print('-' * 50)
    my_dict = obj.__dict__
    if my_dict:
        for k, v in my_dict.items():
            print(f'{k}: {v}')
    else:
        print(f"\t{my_dict}")

    # get the class information
    print('-' * 50)
    print("Contents of obj.__class__")
    print('-' * 50)
    print(obj.__class__)

    # This function is called recursively, exit when you drill down to the type of object is type
    if type(obj) == type:
        print("Can't drill into the type of type ... ending recursion")
        return
    else:
        inspect_all(obj.__class__)

def class_info(my_class, indent=0):
    my_name = my_class.__name__
    my_bases = my_class.__bases__
    print(' ' * indent, end='')
    indent += 3
    print(my_name)
    for i in my_bases:
        class_info(i, indent)


def my_tree(obj):
    """Inspect an object's inheritance tree"""

    print(f"Inspecting {obj.__class__}")
    class_info(obj.__class__)

