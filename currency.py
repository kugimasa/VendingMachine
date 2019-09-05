from enum import IntEnum

class Currency(IntEnum):
    Ten = 10
    Fifty = 50
    Hundred = 100
    FiveHundred = 500
    Thousand = 1000

    @classmethod
    def items(self):
       return [self.Thousand, self.FiveHundred, self.Hundred, self.Fifty, self.Ten]