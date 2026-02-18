#وارد کردن مازول ها
import random
import sys

#مدیریت کل بازی
def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y

        for attempt in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == correct:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {correct}")

    print(f"Score: {score}")

#دریافت سطح از کاربر
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

#تولید عدد تصادفی با تعداد رقم مشخص
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError

if __name__ == "__main__":
    main()
