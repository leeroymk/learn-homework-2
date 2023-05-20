def main():

    with open('referat.txt', 'r', encoding='utf-8') as file:
        content = file.read()

        print(f"Длина строки: {len(content)}")

        print(f"Количество слов в тексте: {len(content.split())}")
        content_wo_dots = content.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as newf:
        newf.write(content_wo_dots)


if __name__ == "__main__":
    main()
