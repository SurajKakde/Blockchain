# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
def output_squares(squares):
    print(squares(5))

# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
output_squares(lambda el: el * el)


# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.
def output_squares1(squares, *args):
    print(args)
    for el in args:
        print(squares(el))


output_squares1(lambda el: el * el, 2,3,4,5)
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.

def output_squares2(squares, *args):
    for el in args:
        print('result : {:20.2f} '.format(squares(el)))


output_squares2(lambda el: el * el, 2,3,4,5)