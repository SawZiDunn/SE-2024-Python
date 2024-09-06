def time24hourTo12hour(time):
    hour, minute = time.split(":")

    if int(hour) > 12:
        hour = int(hour) - 12
        return f"{hour}:{minute} PM"
    return time + " AM"

print(time24hourTo12hour("23:24"))