class UsersBirthdays:
    celebrated = 0

    def __init__(self, guild, user, channel, display_name, month, day):
        self.guildid = str(guild)
        self.userid = str(user)
        self.channelid = str(channel)
        self.display_name = str(display_name)
        self.month = str(month)
        self.day = str(day)

    def write_to_file(self):
        with open('Birthdays.txt', 'a') as birthday:
            birthday.write(self.guildid + ',' + self.userid + ',' + self.channelid + ',' + self.display_name
                           + ',' + self. month + ',' + self.day + '\n')

    def get_day(self):
        return int(self.day)

    def get_month(self):
        return int(self.month)

    def get_userid(self):
        return int(self.userid)

    def get_guild(self):
        return int(self.guildid)

    def set_celebrated(self, date):
        self.celebrated = date
