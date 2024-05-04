import sys


def sign_of(number):
    return (number > 0) - (number < 0)


def round_half_up(value: float) -> int:
    return sign_of(value) * int(abs(value) + 0.5)


for line in sys.stdin:
    line = float(line)
    nota_ponderada = round_half_up((line/(10*0.5))) * 0.5
    if line <= 100:
        if line >= 0:
            if nota_ponderada >= 6.0:
                if nota_ponderada >= 7.0:
                    print(' ' + f'{nota_ponderada} AP')
                else:
                    print(' ' + f'{nota_ponderada} AMP')
            else:
                print(' ' + f'{nota_ponderada} PE')
        else:
            print(f'{line:.2f} ERR')
    else:
        print(f'{line:.2f} ERR')
