# Leetcode Problems--Day of the week

class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        import datetime
        d=                            {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
        return(d[datetime.datetime(year, month,day).weekday()])