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


weight_log = [('Gentoo', 230.0, 5500.0, 'MALE'),
              ('Gentoo', 229.0, 5800.0, 'MALE'),
              ('Gentoo', 225.0, 5400.0, 'MALE'),
              ('Gentoo', 219.0, 5250.0, 'MALE'),
              ('Gentoo', 210.0, 4300.0, 'FEMALE'),
              ('Gentoo', 216.0, 4925.0, 'MALE')]

labeled_entries = []

for species, flipper_length, body_mass, sex in weight_log:
    labeled_entries.append(WeightEntry(
        species, flipper_length, body_mass, sex))

print([entry.mass_to_flipper_length_ratio
      for entry in labeled_entries[:5]])
