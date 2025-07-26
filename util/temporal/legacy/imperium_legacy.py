class Maths:
    @staticmethod
    def isLeap(year):
        return year%400==0 or (year%100!=0 and year%4==0)

class Routine(Maths):
    days_in_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    def __init__(self):
        pass
    
    def epoch_to_imperium (self, seconds, detailed=False):
        if seconds<0:
            return 'Invalid unix epoch time: Use the Centurian module in the same package.'
        
        year=1970
        while seconds >= (365 + Maths.isLeap(year))*86400:
            seconds -= (365 + Maths.isLeap(year))*86400
            year+=1
        yy=year-1970
        month=0
        for i in Routine.days_in_month:
            if month==1: (month:=month+1) # to avoid epoch zero errors
            if seconds <= (i*86400): break
            seconds -= (i+(month==2 and Maths.isLeap(year)))*86400
            month+=1

        day=(seconds // 86400) + (seconds%86400>=0)
        seconds %= 86400
        hours=seconds // 3600
        minutes= (seconds%3600) // 60
        sec = (seconds%60)
        if detailed:
            return {
                "yy": yy,
                "m": month,
                "d": day,
                "h": hours,
                "min": minutes,
                "sec": sec,
                "ir": f"{yy:02}{month:02}{day:02}_{hours:02}{minutes:02}{sec:02}"
            }
        else:
            return f"{yy:02}{month:02}{day:02}_{hours:02}{minutes:02}{int(sec)}"
    
    def imperium_to_epoch(self, imperium):
        #In this comprehension, the key:value is the value of comprehension; value is modified seperately as it it gets a value then reduces itself after the first iteration by walrus operator
        serie={i:(imperium%100 if i == 1 else (imperium:=imperium//100)%100) for i in range(1,7)}
        # print(serie)
        #seconds
        seconds=serie[1]

        #minutes
        seconds+=serie[2]*60

        #hours
        seconds+=serie[3]*3600
        
        current_year=(1970+serie[6])
        #days
        if serie[4] > (Routine.days_in_month[serie[5]-1]+ (serie[5]==2 and Maths.isLeap(current_year))): return 'invalid day'
        seconds+=(serie[4]-1)*86400


        #months-yeah, this is may look like a mess
        if serie[5] <= 0 or serie[5] > 12: return 'invalid month.'
        seconds+=sum((Routine.days_in_month[i] + (i==1 and Maths.isLeap(current_year)))*86400 for i in range(serie[5]-1))

        #year
        if serie[6]>9999: return 'invalid for epoch time. check Centaurian module'
        seconds+=sum(((365+(Maths.isLeap(i)))*86400) for i in range(1970, current_year))
        
        return seconds
    

    def day(self, imperium):
        pass


