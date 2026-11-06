seconds = int(input("Enter time in seconds: "))
ten_minutes_in_seconds = 600

if seconds < ten_minutes_in_seconds:
    difference = ten_minutes_in_seconds - seconds
    print(f"{difference} seconds left to 600 seconds")
else:
    if seconds > ten_minutes_in_seconds:
        print("Seconds provided are higher than 600 seconds")
    else:
        print("Seconds provided match 600 seconds")