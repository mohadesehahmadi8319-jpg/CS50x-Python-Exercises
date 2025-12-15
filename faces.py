def convert(imoji):
    return imoji.replace(":)", "🙂").replace(":(", "🙁")

def main():
    text_input = input()
    print(convert(text_input))

main()
