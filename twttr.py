text = input("لطفا رشته یا کلمه مورد نظر را تایپ کنید.")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
for char in text:
    if char not in vowels:
        print(char, end="")
print()

