seconds = int(input("Enter a number of seconds (0 <= seconds < 8640000): "))

if seconds < 0 or seconds >= 8640000:
    print("The number must be greater than or equal to 0 and less than 8640000.")
else:
    days = seconds // (24 * 60 * 60)
    remainder = seconds % (24 * 60 * 60)
    hours = remainder // (60 * 60)
    remainder %= (60 * 60)
    minutes = remainder // 60
    seconds = remainder % 60

    if days % 10 == 1 and days % 100 != 11:
        day_str = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_str = "дні"
    else:
        day_str = "днів"

    time_str = "{:02}:{:02}:{:02}".format(hours, minutes, seconds)

    print(f"{days} {day_str}, {time_str}")
