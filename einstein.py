def energy(jool):
    c = 300000000
    return jool*c*c

def main():
    m = int(input("جرم را وارد کنید."))
    print(energy(m))

main()

