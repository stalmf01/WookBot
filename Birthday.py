

class Birthday:
    month = 0
    day = 0
    birthday_days = {}
    birthday_months = {}

    def __init__(self, birthdays):
        birthday_file = open('Birthdays.txt', 'r')
        for count in range(birthdays):
            user = birthday_file.readline()
            day = birthday_file.readline()
            month = birthday_file.readline()
            self.birthday_days[user] = day
            self.birthday_months[user] = month

    def get_day(self, user):
        return self.birthday_days[user]

    def get_month(self, user):
        return self.birthday_months[user]