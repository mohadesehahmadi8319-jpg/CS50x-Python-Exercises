items = {}

while True:
    try:
        item = input().strip().lower()
        items[item] = items.get(item, 0) + 1
    except EOFError:
        print()
        break


for item_name, count in sorted(items.items()):
    print(f"{count} {item_name.upper()}")
