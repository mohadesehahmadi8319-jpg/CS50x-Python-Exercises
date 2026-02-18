months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date = input("Date: ").strip()


    if "/" in date:
        try:
            month, day, year = map(int, date.split("/"))
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
        except (ValueError, TypeError):
            pass


    else:
        parts = date.split()
        if len(parts) == 3:
            month_name, day_str, year_str = parts
            month_name = month_name.capitalize()

            if month_name in months and day_str.endswith(","):
                try:
                    day = int(day_str[:-1])  
                    year = int(year_str)
                    month_num = months.index(month_name) + 1
                    if 1 <= day <= 31:
                        print(f"{year}-{month_num:02}-{day:02}")
                        break
                except (ValueError, IndexError):
                    pass

