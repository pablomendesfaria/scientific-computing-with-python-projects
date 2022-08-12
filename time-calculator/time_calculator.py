def add_time(start, duration, wday=None):
    def change_am_pm(ante_post):
        if ante_post == 'AM':
            return 'PM'
        else:
            return 'AM'

    def change_week_day(weekday):
        if weekday is not None:
            weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            idx = weekdays.index(weekday.title())
            if idx == len(weekdays)-1:
                return weekdays[0]
            else:
                return weekdays[idx+1]
        else:
            return None

    start_time = start.replace(':', ' ').split(' ')
    start_time[0], start_time[1] = int(start_time[0]), int(start_time[1])

    duration_time = duration.split(':')
    duration_time[0], duration_time[1] = int(duration_time[0]), int(duration_time[1])

    am_pm = start_time[2]
    days = 0
    current_weekday = wday

    res_min = start_time[1] + duration_time[1]
    if res_min >= 60:
        res_min -= 60
        start_time[0] += 1
        if start_time[0] >= 12:
            start_time[0] -= 12
            if am_pm == 'PM':
                days += 1
                am_pm = change_am_pm(am_pm)
                current_weekday = change_week_day(current_weekday)
            else:
                am_pm = change_am_pm(am_pm)

    res_hours = start_time[0] + duration_time[0]
    if res_hours >= 12:
        if res_hours > 12:
            res_hours -= 12
        if am_pm == 'PM':
            days += 1
            am_pm = change_am_pm(am_pm)
            current_weekday = change_week_day(current_weekday)
        else:
            am_pm = change_am_pm(am_pm)

    while res_hours >= 12:
        res_hours -= 12
        if am_pm == 'PM':
            days += 1
            am_pm = change_am_pm(am_pm)
            current_weekday = change_week_day(current_weekday)
        else:
            am_pm = change_am_pm(am_pm)

    if res_hours == 0:
        res_hours = 12

    if current_weekday is not None:
        if days == 0:
            new_time = f'{res_hours}:{res_min:02d} {am_pm}, {current_weekday}'
        elif days == 1:
            new_time = f'{res_hours}:{res_min:02d} {am_pm}, {current_weekday} (next day)'
        else:
            new_time = f'{res_hours}:{res_min:02d} {am_pm}, {current_weekday} ({days} days later)'
    else:
        if days == 0:
            new_time = f'{res_hours}:{res_min:02d} {am_pm}'
        elif days == 1:
            new_time = f'{res_hours}:{res_min:02d} {am_pm} (next day)'
        else:
            new_time = f'{res_hours}:{res_min:02d} {am_pm} ({days} days later)'

    return new_time
