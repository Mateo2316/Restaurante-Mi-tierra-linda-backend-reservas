import datetime

class DateFormat():

    @classmethod
    def convertDate(self, date):
        return datetime.datetime.strftime(date, '%d-%m-%Y')
