class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "Day: {:<2} Month: {:<2} Year: {:<4}".format(self.day, self.month, self.year)

    def add_days(self, amount):
        day_upper_limit = 30
        if self.day + amount > day_upper_limit:
            self.day += amount - 30
            self.month += 1
        else:
            self.day += amount
