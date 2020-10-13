days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def days_in_year(year, month, day):
    days = 0
    if is_leap_year(year) and month > 2:
        days += 1
    for m in days_in_month[:month - 1]:
        days += m
    days += day

    return days


def days_to_next_year(year, month, day):
    if is_leap_year(year):
        return 366 - days_in_year(year, month, day)
    else:
        return 365 - days_in_year(year, month, day)


def days_in_years(year1, year2):
    days = 0
    for year in range(year1, year2):
        if is_leap_year(year):
            days += 366
        else:
            days += 365
    return days


def days_to_20201003(y, m, d):
    days = 0
    if y == 2020:
        days = days_in_year(y, m, d) - days_in_year(2020,10,3)
    elif y > 2020:
        days = days_to_next_year(2020,10,3) + days_in_years(2021,y) + days_in_year(y, m, d)
    else:
        days -= days_in_year(2020,10,3) + days_in_years(y+1, 2020) + days_to_next_year(y, m, d)
    return days


def day_in_week(y, m, d):
    days = days_to_20201003(y, m, d)
    return (days + 6) % 7


def print_calendar(year):
    begin_of_week = day_in_week(year, 1, 1)
    for m in days_in_month:
        print('  日 一 二 三  四 五  六')
        print('   ' * begin_of_week, end='')

        if is_leap_year(year) and m == 28:
            m += 1

        for j in range(1, m + 1):
            print("%3d" % j, end='')
            begin_of_week += 1
            begin_of_week %= 7
            if begin_of_week == 0:
                print()

        if begin_of_week != 0:
            print()
        print()


print_calendar(2020)
#print(day_in_week(2007, 8, 28))

