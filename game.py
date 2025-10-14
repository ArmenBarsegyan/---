import random


def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    previous_guess = None

    print(f"У тебя есть {max_attempts} попыток!")

    while attempts < max_attempts:
        try:
            # Получаем ввод от пользователя
            guess = int(input(f"\nПопытка {attempts + 1}. Введи число: "))
            attempts += 1

            # Проверяем угадал ли пользователь
            if guess == secret_number:
                print(f"\n🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                if attempts <= 3:
                    print("⭐ Ты настоящий экстрасенс!")
                elif attempts <= 6:
                    print("👍 Отличный результат!")
                break
            elif guess < secret_number:
                print("Слишком маленькое число! Попробуй еще.")
            else:
                print("Слишком большое число! Попробуй еще.")

            # Добавляем подсказку о том, ближе ли текущая попытка к предыдущей
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

                # Добавляем небольшую подсказку на середине игры
                if remaining == max_attempts // 2:
                    if secret_number % 2 == 0:
                        print("💡 Подсказка: число четное!")
                    else:
                        print("💡 Подсказка: число нечетное!")
            else:
                print(f"\n💥 К сожалению, попытки закончились! Я загадал число {secret_number}")

        except ValueError:
            print("Пожалуйста, введи целое число!")

    # Предлагаем сыграть еще раз
    play_again = input("\nХочешь сыграть еще раз? (да/нет): ").lower()
    if play_again in ['да', 'д', 'yes', 'y']:
        guess_number()
    else:
        print("Спасибо за игру! До свидания!")


# Запускаем игру
if __name__ == "__main__":
    guess_number()