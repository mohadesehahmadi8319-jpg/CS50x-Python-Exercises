while True:
    try:
        xy = input("لطفا کسر مورد نظر را وارد کنید: ")
        parts = xy.split('/')

        if len(parts) != 2:
            print("باید فرمت ورودی به صورت x/y باشد")
            continue

        x = int(parts[0])
        y = int(parts[1])

        if x > y or y == 0 or x < 0:
            print("لطفا مقدار صحیح را وارد کنید")
            continue

        percentage = (x / y) * 100
        rounded_percentage = round(percentage)

        if rounded_percentage <= 1:
            print("E")
        elif rounded_percentage >= 99:
            print("F")
        else:
            print(f"{rounded_percentage}%")

        break

    except (ValueError, ZeroDivisionError):
        print("ورودی نامعتبر است. لطفا اعداد صحیح و مخرج غیر صفر وارد کنید.")
