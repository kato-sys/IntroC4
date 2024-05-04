import sys


def round_to(value: float, decimal_digits: int) -> float:
    power10: float = 10 ** decimal_digits
    return round(value * power10) / power10


for monto_viejo in sys.stdin:
    monto_viejo = float(monto_viejo)
    if monto_viejo >= 0:
        if monto_viejo <= 100000000:

            monto_raw = monto_viejo/1.13
            monto_nuevo = monto_raw*1.115

            print(f'{round_to(monto_viejo, 2):.2f}: {round_to(monto_nuevo, 2):.2f} ({monto_viejo - monto_nuevo:.2f})')
        else:
            print(f'{round_to(monto_viejo, 2):.2f}: invalid data')
    else:
        print(f'{round_to(monto_viejo, 2):.2f}: invalid data')
