#وارد کردن ماژول ها
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

#بررسی همه فونت های معتبر
fonts = figlet.getFonts()

#بررسی آرگومان خط فرمان
if len(sys.argv) == 1:
    font_name = random.choice(fonts)

elif len(sys.argv) == 3:

    #بررسی آرگومان اول
    if sys.argv[1] not in ["-f","--font"]:
        sys.exit("Invalid usage")

    #بررسی آرگومان دوم(اسم فونت)
    if sys.argv[2] not in fonts:
        sys.exit("Invalid usage")

    font_name = sys.argv[2]

else:
    #تعداد آرگومان اشتباه
    sys.exit("Invalid usage")

#تنظیم فونت
figlet.setFont(font=font_name)

#دریافت آرگومان
text = input("Input: ")
print(figlet.renderText(text))
