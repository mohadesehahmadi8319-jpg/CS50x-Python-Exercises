def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # طول:
    if len(s) < 2 or len(s) > 6:
        return False
    
    # دو حرف اول:
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # چک کردن کاراکتر مجاز:
    for char in s:
        if not char.isalnum():
            return False

    # چک کردن اعداد:
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
            if s[i] == '0':
                return False
            break

    return True
main()
