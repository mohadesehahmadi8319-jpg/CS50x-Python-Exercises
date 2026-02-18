#وارد کردن ماژول
import random

#دریافت عدد با حلقه
while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
    except ValueError:
        pass

#تولید عدد تصادفی
secret = random.randint(1,level)

#حلقه حدس زدن
while True:
    try:
        guess  = int(input("Guess: "))
        if guess <= 0:
            continue

        if guess < secret:
            print("Too small!")
        elif guess > secret:
            print("Too large!")
        else:
            print("Just right!")
            break

    except ValueError:
        pass
