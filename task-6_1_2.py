def write_to_file():
    with open('poem.txt', 'w', encoding='utf-8') as file:
        file.write("Если б мишки были пчелами,\n")
        file.write("То они бы нипочем,\n")
        file.write("Никогда и не подумали,\n")
        file.write("Так высоко строить дом.\n")


def read_from_file():
    with open('poem.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    print(content)

write_to_file()
read_from_file()