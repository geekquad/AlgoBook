# Zeller's Congruence Rule


def day_of_date(d) :
    day_dict = {
        0 : 'Sunday',
        1 : 'Monday',
        2 : 'Tuesday',
        3 : 'Wednesday',
        4 : 'Thursday',
        5 : 'Friday',
        6 : 'Saturday'}
    return day_dict[d]

def month_shift(month, year):
    if month == 1 or month == 2:
        month += 10
        year -= 1
        return month , year  
    
    else:
        month -= 2
        return month ,year

def ZellersCongruence(day, month, year):
    month , year = month_shift(month, year)
    k = day
    m = month
    d = year % 100 
    c = year // 100
    f = (k + ((13 * m -1) // 5) + d + (d // 4) + (c // 4) - 2 * c)
    f = (f % 7) 
    return day_of_date(f)
    
    
    
day = int(input('Enter Day -> '))
month = int(input('Enter Month -> '))
year = int(input('Enter Year -> '))

print("The Day of the Given Date is -> ", ZellersCongruence(day, month, year))
