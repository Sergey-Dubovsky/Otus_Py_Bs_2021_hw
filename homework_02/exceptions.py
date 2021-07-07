"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(BaseException):
    # print('Low Fuel!')
    pass

class NotEnoughFuel(BaseException):
    # print('Not Enough Fuel!')
    pass

class CargoOverload(BaseException):
    # print('Cargo Overload!')
    pass

