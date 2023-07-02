import random
from data import subjects, adverbs, verbs, prepositions, locations, famous_artists


class generation_v2:
    def __init__(self, subjects, adverbs, verbs, preposition, locations, famous_artists):
       self.subjects = subjects.lower()
       self.adverbs = adverbs.lower()
       self.verbs = verbs.lower()
       self.prepositions = verbs.lower()
       self.locations = locations.lower()
       self.famous_artists = famous_artists.lower()



    def prompt(self):
       print(f' {self.subjects} {self.adverbs} {self.verbs} in a {self.locations} in {self.famous_artists} styling')
       



a = random.choice(subjects)
b = random.choice(adverbs)
c = random.choice(verbs)
d = random.choice(prepositions)
e = random.choice(locations)
f = random.choice(famous_artists)



myObject = generation_v2(a, b, c, d, e, f)

print(myObject.prompt())
