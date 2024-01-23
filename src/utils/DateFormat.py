import datetime


class DateFormat():

    @classmethod
    def ConvertDate(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
    
    @classmethod
    def ConvertDateTime(self, date):
        return datetime.datetime.strftime(date, '%d-%m-%Y %H:%M')
