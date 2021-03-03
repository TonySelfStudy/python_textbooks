from random import choice


class Lottery:
    """A class to model a Lottery."""

    choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

    def __init__(self):
        self.winners = [choice(self.choices), choice(self.choices), choice(self.choices), choice(self.choices)]
        self.winners = [choice(self.choices) for x in range(4)]
        print(f"The winning ticket is {self.winners}")

    def get_ticket(self):
        return [choice(self.choices), choice(self.choices), choice(self.choices), choice(self.choices)]


the_lottery = Lottery()
count = 0

while (the_lottery.get_ticket() != the_lottery.winners):
    count += 1

print(f"Match found after {count} iterations.")