class Character:
    def __init__(self, name, race, job):
        self.name = name
        self.race = race
        self.job = job

    def __str__(self):
        return '\nCharacter: {} \nRace: {} \nJob: {}\n'.format(self.name, self.race, self.job)


aero = Character('Aero', 'Kobold', 'Rogue')
print(aero)
