def main():
    time = input("inter time plz")
    t = convert(time)
    if 7.0 <= t <= 8.0:
        print("breakfast time")
    elif 12.0 <= t <=13.0:
        print("lunch time")
    elif 18.0 <= t <= 19.0:
        print("dinner time")
def convert(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes = int(minutes)
    return hour + minutes / 60
if __name__ == "__main__":
    main()
