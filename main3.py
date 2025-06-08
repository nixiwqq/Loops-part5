import random

def multiplication_quiz():
    print("\nЛаскаво просимо до тесту на знання таблиці множення!")

    levels = {
        1: (1, 5, 5),    # Легкий рівень: числа від 1 до 5, 5 запитань
        2: (1, 10, 7),   # Середній рівень: числа від 1 до 10, 7 запитань
        3: (1, 12, 10)   # Складний рівень: числа від 1 до 12, 10 запитань
    }

    print("\nОберіть рівень складності:")
    print("1 - Легкий")
    print("2 - Середній")
    print("3 - Складний")

    level = int(input("Введіть номер рівня (1, 2 або 3): "))
    while level not in levels:
        print("Будь ласка, оберіть правильний номер рівня (1, 2 або 3).")
        level = int(input("Введіть номер рівня (1, 2 або 3): "))

    min_num, max_num, num_questions = levels[level]
    score = 0

    print(f"\nВи обрали рівень {level}. Вам потрібно відповісти на {num_questions} запитань.")

    for i in range(1, num_questions + 1):
        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)

        answer = int(input(f"Питання {i}: Скільки буде {num1} * {num2}? "))

        if answer == num1 * num2:
            print("Правильно!")
            score += 1
        else:
            print(f"Неправильно. правильна відповідь: {num1 * num2}")

    print("\nРезультати:")
    print(f"Ви відповіли правильно на {score} із {num_questions} запитань")

    if score == num_questions:
        print("Відмінно! Ви справжній майстер таблиці множення")
    elif score >= num_questions * 0.7:
        print("Добре! Ви знаєте таблицю множення досить добре")
    elif score >= num_questions * 0.4:
        print("Задовільно, вам слід ще трохи попрактикуватися")
    else:
        print("Погано, варто більше тренуватися.")

multiplication_quiz()