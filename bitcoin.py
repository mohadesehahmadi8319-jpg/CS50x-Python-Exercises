import sys
import requests

def main():
    #چک کردن تعداد آرگومان ها
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument ")
    #تبدیل کردن به عدد
    try:
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    #گرفتن قیمت از API
    api_key = "52195b7192f4706fd2cb331a5a456cce70e8701acd55d461007b0026a66d1b5e"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apikey={api_key}"

    try:
        response = requests.get(url)
    except requests.RequestExcaption:
        sys.exit("Requst Error")

    if response.status_code != 200:
        sys.exit("API Error")

    data = response.json()
    price = float(data["data"]["priceUsd"])

    #محاسبه و نمایش قیمت
    total = n * price
    print(f"${total:,.4f}")

if __name__ == "__main__":
    main()


