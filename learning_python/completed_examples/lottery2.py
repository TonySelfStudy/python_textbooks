"""Lottery example 2.
Notes
-----
1) The 'sample' function is used in place of 'choice' since it selects without replacement
    (e.g. you can't pull the same number twice if we are using the ping-pong style approach)
2) All choices are numeric so they can sort more easily
3) The order of the selection is not important (1, 2, 3) is a winning ticket for (2, 3, 1)
4) The number of total and selected balls are now variables
"""
from random import sample
from math import factorial as fac

class Lottery:
    def __init__(self, num_balls, num_selections):
        self.num_balls = num_balls                  # Number of ping-pong balls in the hopper
        self.num_selections = num_selections        # Number of balls selected per drawing
        self.choices = list(range(self.num_balls))  # List of all ping-pong ball numbers
        self.odds = self.win_chance()               # Find chance of a winning combination

        self.winning_ticket = self.get_ticket()     # Find the winning ticket with the same mechanism as selecting one

        print(f"\nA new lottery is created!\n"
              f"Now selecting {num_selections} balls "
              f"from a total of {num_balls} ping pong balls.")
        print(f"The winning ticket is {self.winning_ticket}.")
        print(f"Your expected chance of winning is 1 in {int(self.odds):,}.")

        self.run_lottery()

    def get_ticket(self):
        x = sample(self.choices, self.num_selections)
        x.sort()
        return x

    def run_lottery(self):
        count = 1  # start at 1, not 0, because you can hit it the first time
        while self.get_ticket() != self.winning_ticket:
            count += 1
        print(f"Match found after {count:,} iteration(s).")

    def win_chance(self):
        """
        Calculate the chance that a ticket could win based on number of balls and choices.

        The number of ways to choose r objects from n when order
        is not important and we are drawing without replacement is given by:
        C(n,r) = n!/(r! * (n-r)!)

        source: http://mathforum.org/library/drmath/view/56122.html

        why dum dum is president: https://www.iheart.com/content/2018-01-02-13-things-that-will-actually-improve-your-chances-of-winning-the-lottery/

        """
        n = self.num_balls
        r = self.num_selections

        return fac(n) / (fac(r) * fac(n-r))


if __name__ == "__main__":
    lottery1 = Lottery(num_balls=10, num_selections=2)
    lottery2 = Lottery(num_balls=15, num_selections=6)
    lottery3 = Lottery(num_balls=15, num_selections=15)
    lottery4 = Lottery(num_balls=30, num_selections=5)
