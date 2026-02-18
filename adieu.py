import inflect

p = inflect.engine()

#لیست خالی برای ذخیره کردن اسم ها
names = []

#حلقه
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

if names:
    print(f"Adieu, adieu, to {p.join(names)}")

