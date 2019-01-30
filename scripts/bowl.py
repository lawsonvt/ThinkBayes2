"""The is an attempt at creating a bowl class
to solve Exercise 2-1 in the Think Bayes book"""

class Bowl(object):
    """A bowl object that keeps track of our cookies"""

    def __init__(self, bowl_name, v_cookies, c_cookies):
        """Constructor"""
        self.bowl_name = bowl_name
        self.v_cookies = float(v_cookies)
        self.c_cookies = float(c_cookies)
        self.ratio()

    def ratio(self):
        """Calculate ratios"""
        self.v_ratio = self.v_cookies / (self.v_cookies+self.c_cookies)
        self.c_ratio = self.c_cookies / (self.v_cookies+self.c_cookies)

    def take_c(self):
        """take a chocolate cookie"""
        self.c_cookies = self.c_cookies - 1
        self.ratio()

    def take_v(self):
        """take a vanilla cookie"""
        self.v_cookies = self.v_cookies - 1
        self.ratio()


