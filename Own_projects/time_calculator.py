
days_of_week = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
                "friday": 4, "saturday": 5, "sunday": 6}

days_of_week_tuple = ("Monday", "Tuesday", "Wednesday", "Thursday",
                      "Friday", "Saturday", "Sunday")


def add_time(start, duration, weekday=None):

    # Time to be added
    split_duration = duration.split(":")

    duration_minutes = int(split_duration[1])
    duration_hours = int(split_duration[0])

    # Original time
    split_start = start.split(":")
    split_start_am_pm = (split_start[1]).split(" ")

    start_minutes = int(split_start_am_pm[0])
    start_hours = int(split_start[0])

    # AM or PM
    am_pm = split_start_am_pm[1]
    am_or_pm = {"AM": "PM", "PM": "AM"}

    # Minutes Calculation
    tot_minutes = start_minutes + duration_minutes
    if tot_minutes >= 60:
        start_hours += 1
        tot_minutes = tot_minutes % 60

    tot_minutes = tot_minutes if tot_minutes > 9 else "0" + str(tot_minutes)

    # Hours Calculation
    tot_hours = (start_hours + duration_hours) % 12
    tot_hours = 12 if tot_hours == 0 else tot_hours

    # Days Calculation
    days = int(duration_hours / 24)
    if am_pm == "PM" and start_hours + (duration_hours % 12) >= 12:
        days += 1

    # AM or PM Calculation
    time_am_or_pm = int((start_hours + duration_hours) / 12)
    am_pm = am_or_pm[am_pm] if time_am_or_pm % 2 == 1 else am_pm

    # Output
    new_time = f"{tot_hours}:{tot_minutes} {am_pm}"

    # weekday Calculation
    if weekday:
        weekday = weekday.lower()
        index = int((days_of_week[weekday]) + days) % 7
        new_day = days_of_week_tuple[index]
        new_time += f", {new_day}"
    if days == 1:
        new_time += f" (next day)"
    if days > 1:
        new_time += f" ({str(days)} days later)"

    return new_time


if __name__ == '__main__':
    print(add_time("11:59 PM", "24:05", "Wednesday"))
    # expected = "12:04 AM, Friday (2 days later)"

    print(add_time("11:59 PM", "24:05"))
    # expected = "12:04 AM (2 days later)"

    print(add_time("11:40 AM", "0:25"))
    # expected = "12:05 PM"

    print(add_time("9:15 PM", "5:30"))
    # expected = "2:45 AM (next day)"

    print(add_time("8:16 PM", "466:02", "tuesday"))
    # expected = "6:18 AM, Monday (20 days later)"

    print(add_time("8:16 PM", "466:02"))
    # expected = "6:18 AM (20 days later)"

    print(add_time("11:55 AM", "3:12"))
    # expected = "3:07 PM"
