import datetime
import math


def time_add(start, duration = None, day = None):
    begin = start.split()
    beginT = begin[0].split(':')
    beginH = int(beginT[0])
    beginM = int(beginT[1])
    beginB = begin[1]
    durationT = duration.split(':')
    durationH = int(durationT[0])
    durationM = int(durationT[1])

    if beginB == 'PM' and beginH != 12:
        beginH = beginH + 12
    elif beginB == 'AM' and beginH == 12:
        beginH = 0

    time = str(beginH) + ':' + '{:02d}'.format(beginM) + beginB.rjust(3)

    days = math.floor( (beginH + durationH + (beginM + durationM)/60) / 24 )
    MinOver = math.floor( (beginM + durationM) / 60 )
    timeH = (beginH + durationH + MinOver) % 24
    timeM = (beginM + durationM) % 60

    if timeH > 11:
        beginB = 'PM'
    else:
        beginB = 'AM'

    if timeH > 12:
        timeH = timeH % 12
    elif timeH == 0:
        timeH = 12

    time = str(timeH) + ':' + '{:02d}'.format(timeM) + beginB.rjust(3)

    sun = 0
    mon = 1
    tues = 2
    wed = 3
    thur = 4
    fri = 5
    sat = 6
    if day != None:
        if day.lower() == 'sunday':
            dayNum = sun
        elif day.lower() == 'monday':
            dayNum = mon
        elif day.lower() == 'tuesday':
            dayNum = tues
        elif day.lower() == 'wednesday':
            dayNum = wed
        elif day.lower() == 'thursday':
            dayNum = thur
        elif day.lower() == 'friday':
            dayNum = fri
        elif day.lower() == 'saturday':
            dayNum = sat

        dayNum = dayNum + days

        if dayNum == 0:
            dayName = 'Sunday'
        elif dayNum == 1:
            dayName = 'Monday'
        elif dayNum == 2:
            dayName = 'Tuesday'
        elif dayNum == 3:
            dayName = 'Wednesday'
        elif dayNum == 4:
            dayName = 'Thursday'
        elif dayNum == 5:
            dayName = 'Friday'
        elif day.lower() == 'saturday':
            dayName = 'Saturday'

        dayspass = '({} days later)'.format(days)

        if days > 1:
            print(time + ',' + dayName.rjust(len(dayName)+1) + dayspass.rjust(len(dayspass)+1))
        elif days == 1:
            print(time + ',' + dayName.rjust(len(dayName) + 1) + ' (next day)')
        else:
            print(time + ',' + dayName.rjust(len(dayName) + 1))
    else:
        dayspass = '({} days later)'.format(days)
        if days > 1:
            print(time + dayspass.rjust(len(dayspass) + 1))
        elif days == 1:
            print(time + ' (next day)')
        else:
            print(time)






