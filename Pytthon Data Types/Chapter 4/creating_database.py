from dataclasses import dataclass


@dataclass
class WeightEntry:
    species: str
    body_mass: int
    flipper_length: int
    sex: str

    @property
    def mass_to_flipper_length_ratio(self):
        return self.body_mass / self.flipper_length
