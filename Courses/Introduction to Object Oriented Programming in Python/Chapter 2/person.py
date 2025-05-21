class Person:
    CURRENT_YEAR = 2024

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        age = cls.CURRENT_YEAR - birth_year
        return cls(name, age)


bob = Person.from_birth_year("Bob", 1990)
