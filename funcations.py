def unlimited_arguments(*args, **keyword_args):
    print(args)
    for arguments in args:
        print(arguments)
    print(keyword_args)
    for arguments in keyword_args:
        print(arguments)


unlimited_arguments(1,2,3,4,name='suraj',age=29)