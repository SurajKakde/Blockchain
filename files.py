with open('demo.txt', mode='r') as f:
    # # f.write('Add this content!\n')
    # fl = f.readlines()
    # f.close()
    #
    # for line in fl:
    #     print(line[:-1])

    line = f.readline()
    while line:
        print(line)
        line = f.readline()

    # print(f.readline())

print('Done!')
