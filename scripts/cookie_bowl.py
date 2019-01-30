"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

I added some stuff to it (Mark Lawson

"""

import sys
import os

sys.path.append(os.path.abspath("/home/pi/Programming/ThinkBayes2/thinkbayes2/"))

from thinkbayes2 import Pmf

from bowl import Bowl

class Cookie(Pmf):
    """A map from string bowl ID to probablity."""

    def __init__(self, bowl1, bowl2):
        """Constructor"""
        self.bowl1 = bowl1
        self.bowl2 = bowl2
        Pmf.__init__(self)
        self.Set(bowl1.bowl_name, 1)
        self.Set(bowl2.bowl_name, 1)
        self.Normalize()
        self.set_mixes()

    def Update(self, data):
        """Updates the PMF with new data.

        data: string cookie type
        """
        for hypo in self.Values():
            like = self.Likelihood(data, hypo)
            self.Mult(hypo, like)
        self.Normalize()


    def set_mixes(self):
        """Set the mixes by pulling the ratios from
        the bowls"""
        self.mixes = {
            'Bowl 1':dict(vanilla=self.bowl1.v_ratio, 
                chocolate=self.bowl1.c_ratio),
            'Bowl 2':dict(vanilla=self.bowl2.v_ratio, 
                chocolate=self.bowl2.c_ratio),
        }

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        mix = self.mixes[hypo]
        like = mix[data]
        return like

    def take_cookie(self, data, bowl_name):
        """Take the given cookie from the given bowl
        and update mixes"""
        if self.bowl1.bowl_name == bowl_name:
            if data == "vanilla":
                self.bowl1.take_v()
            elif data == "chocolate":
                self.bowl1.take_c()
        elif self.bowl2.bowl_name == bowl_name:
            if data == "vanilla":
                self.bowl2.take_v()
            elif data == "chocolate":
                self.bowl.take_c()

        self.set_mixes()


def main():

    mybowl1 = Bowl("Bowl 1", 30, 10)
    mybowl2 = Bowl("Bowl 2", 20, 20)

    pmf = Cookie(mybowl1,mybowl2)

    pmf.Update('vanilla')

    for hypo, prob in pmf.Items():
        print(hypo, prob)

    pmf.take_cookie("vanilla", "Bowl 1")

    print(pmf.mixes)

    pmf.Update("vanilla")

    for hypo, prob in pmf.Items():
        print(hypo, prob)



if __name__ == '__main__':
    main()
