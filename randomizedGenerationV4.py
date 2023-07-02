import random
from data import subjects, prepositions, adjectives, locations, famous_artists


class generation_v4:
    def __init__(self, subjects, prepositions, adjectives, locations, famous_artists):
       self.subjects = subjects.lower()
       self.prepositions = prepositions.lower()
       self.adjectives = adjectives.lower()
       self.locations = locations.lower()
       self.famous_artists = famous_artists.lower()



    def prompt(self):
       print(f' {self.subjects} {self.prepositions} a {self.subjects} in a {self.adjectives} {self.locations} in {self.famous_artists} styling')
       


a = random.choice(subjects)
b = random.choice(prepositions)
c = random.choice(adjectives)
d = random.choice(locations)
e = random.choice(famous_artists)



myObject = generation_v4(a, b, c, d, e)

print(myObject.prompt())
