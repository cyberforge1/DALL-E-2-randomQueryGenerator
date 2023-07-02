import random
from data import subjects, prepositions, environments, stylings


class generation_v1:
    def __init__(self, subject, prepositions, environments, stylings):
       self.subject = subject.lower()
       self.prepositions = prepositions.lower()
       self.environments = environments.lower()
       self.stylings = stylings.lower()


    def prompt(self):
       print(f' {self.subject} in a {self.environments} {self.prepositions} {self.stylings}')
       



a = random.choice(subjects)
b = random.choice(prepositions)
c = random.choice(environments)
d = random.choice(stylings)



myObject = generation_v1(a, b, c, d)

print(myObject.prompt())
