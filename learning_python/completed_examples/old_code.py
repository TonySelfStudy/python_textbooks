def full_stack():
    stack = traceback.extract_stack()
    (filename, lineno, function_name, code) = stack[-3]
    print(filename)
    print(lineno)
    print(function_name)
    print(code)