import random


def choose_difficulty():
    print("\n🎯 Выбери уровень сложности:")
    print("1 - Легкий (15 попыток)")
    print("2 - Средний (10 попыток)")
    print("3 - Сложный (5 попыток)")
    print("4 - Эксперт (3 попытки)")

    while True:
        try:
            choice = int(input("Твой выбор (1-4): "))
            if choice == 1:
                return 15, 80  # попытки, начальные очки
            elif choice == 2:
                return 10, 100
            elif choice == 3:
                return 5, 150
            elif choice == 4:
                return 3, 200
            else:
                print("Пожалуйста, выбери число от 1 до 4")
        except ValueError:
            print("Введи число от 1 до 4!")


def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    # Выбор уровня сложности
    max_attempts, initial_score = choose_difficulty()

    secret_number = random.randint(1, 100)
    attempts = 0
    previous_guess = None
    score = initial_score  # Начальный счет зависит от сложности

    print(f"\nУ тебя есть {max_attempts} попыток!")
    print(f"Твой начальный счет: {score} очков")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}. Введи число: "))
            attempts += 1

            # Штраф за каждую попытку (зависит от сложности)
            score -= 10 if max_attempts <= 5 else 5

            if guess == secret_number:
                bonus = max_attempts - attempts  # Бонус за оставшиеся попытки
                score += bonus * 15
                print(f"\n🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                print(f"🏆 Твой финальный счет: {score} очков")

                # Разные сообщения в зависимости от сложности
                if max_attempts <= 3:
                    print("🚀 Невероятно! На экспертном уровне!")
                elif attempts <= max_attempts * 0.3:
                    print("⭐ Ты настоящий экстрасенс!")
                elif attempts <= max_attempts * 0.6:
                    print("👍 Отличный результат!")
                else:
                    print("💪 Хорошая игра!")
                break
            elif guess < secret_number:
                print("Слишком маленькое число! Попробуй еще.")
            else:
                print("Слишком большое число! Попробуй еще.")

            # Сравнение с предыдущей попыткой
            if previous_guess is not None:
                current_diff = abs(guess - secret_number)
                previous_diff = abs(previous_guess - secret_number)
                if current_diff < previous_diff:
                    print("🔥 Ты стал ближе к цели!")
                elif current_diff > previous_diff:
                    print("❌ Ты отдалился от цели...")

            previous_guess = guess

            # Подсказка о количестве оставшихся попыток
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Осталось попыток: {remaining}")
                print(f"Текущий счет: {score} очков")

                # Добавляем подсказки в зависимости от сложности
                if remaining == max_attempts // 2:
                    if max_attempts <= 5:  # Только на сложных уровнях
                        if secret_number % 2 == 0:
                            print("💡 Подсказка: число четное!")
                        else:
                            print("💡 Подсказка: число нечетное!")
                    else:
                        print("💭 Подумай хорошенько!")
            else:
                print(f"\n💥 К сожалению, попытки закончились! Я загадал число {secret_number}")
                print(f"🏆 Твой финальный счет: {score} очков")

        except ValueError:
            print("Пожалуйста, введи целое число!")
            score -= 2  # Штраф за неверный ввод

    play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        guess_number()
    else:
        print("Спасибо за игру! До свидания!")


if __name__ == "__main__":
    guess_number()