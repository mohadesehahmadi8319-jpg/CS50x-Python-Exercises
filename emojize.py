#وارد کردن ماژول
import emoji

#گرفتن ورودی ار کاربر
text = input("Input: ")

#تبدیل به ایموجی
result = emoji.emojize(text , language = "alias")

#نمایش خروجی
print("Output:", result)
