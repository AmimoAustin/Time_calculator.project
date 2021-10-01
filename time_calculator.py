days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]


def add_time(start, duration, *args):
    (L, N) = start.split(" ")
    (SH, SM) = L.split(":")
    (DH, DM) = duration.split(":")

    total_minutes = int(SM) + int(DM)
    total_hours = int(SH) + int(DH)
    future_days = 0

    if total_minutes >= 60:
        total_minutes -= 60
        total_hours += 1

    if total_minutes < 10:
        total_minutes = f"{total_minutes}".zfill(2)

    if total_hours >= 12:
        t, r = divmod(total_hours, 12)
        total_hours = r if r else total_hours
        if total_hours > 12:
            # only for cases where total hours is 24, 36 etc...
            total_hours = total_hours - ((t - 1) * 12)

        if t > 0:
            if N == 'PM':
                future_days = ((t - 1) // 2) + 1
            else:
                future_days = t // 2

        if t > 0 and t % 2 != 0:
            N = 'AM' if N == 'PM' else 'PM'

    added_h = str(total_hours) + ":"
    added_m = str(total_minutes) + " " + f"{N}"
    new_time = (added_h + added_m)

    if args:
        day = args[0].title()
        if future_days > 0:
            index = days.index(day)
            index += future_days % 7
            if index > 6:
                index = index - 7
            day = days[index]

        new_time += f", {day}"

    if future_days == 1:
        new_time += " (next day)".rjust(11)
    elif future_days > 1:
        new_time += f" ({future_days} days later)".rjust(11)

    return new_time


#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
#print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20", "tueSday"))
#print(days.index("Monday"))
#print(add_time("6:30 PM", "205:12"))