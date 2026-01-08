expression = input("مقدار دلخواه را وارد کنید.")
x, y, z = expression.split(" ")
x = int(x)
z = int(z)

if y == "/" and z == 0:
    print("! تقسیم بر صفر مجاز نیست")
else:
    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    print(f"{result:.1f}")





