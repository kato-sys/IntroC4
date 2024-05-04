parameters = input().split(' ')

if len(parameters) >= 4:
    width = float(parameters[0])

    if width % 1 == 0:
        width = int(parameters[0])
        height = int(parameters[1])
        symbol = parameters[2]
        fill = int(parameters[3])

        if fill == 0:
            if height < 0:
                print('invalid data')
            else:
                print(symbol*width)
                for i in range(height - 2):
                    print(symbol + ' '*(width-2) + symbol)
                print(symbol*width)
        else:
            if height < 0:
                print('invalid data')
            elif width < 0:
                print('invalid data')
            else:
                for i in range(height):
                    print(symbol*width)
    else:
        print('invalid data')
elif len(parameters) == 3:
    width = int(parameters[0])
    height = int(parameters[0])
    symbol = parameters[1]
    fill = int(parameters[2])
    if fill > 1:
        print('invalid data')
    elif fill == 0:
        print(symbol*width)
        for i in range(height - 2):
            print(symbol + ' '*(width-2) + symbol)
        print(symbol*width)
    else:
        if height < 0:
            print('invalid data')
        else:
            for i in range(height):
                print(symbol*width)
else:
    print('invalid data')
