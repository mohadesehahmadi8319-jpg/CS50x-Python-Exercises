casecamel = input("لطفا رشته مورد نظر را وارد کنید.")
snake_case = ""
for c in casecamel:
    if c.isupper():
        snake_case += "_" + c.lower()

    else:
        snake_case += c

print(snake_case)
