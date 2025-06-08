while True:
    print("\nМеню:")
    print("1. Ввести число")
    print("2. Вийти")

    choice = input("Оберіть пункт меню (1-2): ")

    if choice == "1":
        number = input("Введіть число: ")

        if not (number.isdigit() or (number[0] == "-" and number[1:].isdigit())):
            print("Будь ласка, введіть коректне ціле число.")
            continue

        abs_number = number if number[0] != "-" else number[1:]
        sum_digits = 0
        zero_count = 0
        num_digits = 0

        for digit in abs_number:
            sum_digits += int(digit)
            num_digits += 1
            if digit == "0":
                zero_count += 1

        avg_digits = sum_digits / num_digits

        print(f"Кількість цифр: {num_digits}")
        print(f"Сума цифр: {sum_digits}")
        print(f"Середнє арифметичне: {avg_digits:.2f}")
        print(f"Кількість нулів: {zero_count}")
    elif choice == "2":
        print("До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
