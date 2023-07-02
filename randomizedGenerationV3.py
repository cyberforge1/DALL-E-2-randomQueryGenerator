import random
from data import stylings, prepositions, environments, adjectives, objects


class generation_v3:
    def __init__(self, stylings, prepositions, environments, adjectives, objects):
       self.stylings = stylings.lower()
       self.prepositions = prepositions.lower()
       self.environments = environments.lower()
       self.adjectives = adjectives.lower()
       self.objects = objects.lower()



    def prompt(self):
       print(f' {self.stylings} {self.prepositions} {self.environments} with a {self.adjectives} {self.objects}')
       


a = random.choice(stylings)
b = random.choice(prepositions)
c = random.choice(environments)
d = random.choice(adjectives)
e = random.choice(objects)



myObject = generation_v3(a, b, c, d, e)

print(myObject.prompt())
