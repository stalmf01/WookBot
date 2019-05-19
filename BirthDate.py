class UsersBirthdays:

    def __init__(self, guild, user, channel, display_name, month, day):
        self.guildid = str(guild)
        self.userid = str(user)
        self.channelid = str(channel)
        self.display_name = str(display_name)
        self.month = str(month)
        self.day = str(day)

    def write_to_file(self):
        with open('Birthdays.txt', 'a') as birthday:
            birthday.write(self.guildid + ' ' + self.userid + ' ' + self.channelid + ' ' + self.display_name
                           + ' ' + self. month + ' ' + self.day + '\n')

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_userid(self):
        return self.userid
