class BetterDate:
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_str(cls, datestr):
        parts = datestr.split("-")
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])

        return cls(year, month, day)


xmas = BetterDate.from_str("2024-12-25")
print(xmas.year)
print(xmas.month)
print(xmas.day)
