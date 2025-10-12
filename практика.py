import random


def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"У тебя есть {max_attempts} попыток!")

    while attempts < max_attempts:
        try:
            # Получаем ввод от пользователя
            guess = int(input(f"\nПопытка {attempts + 1}. Введи число: "))
            attempts += 1

            # Проверяем угадал ли пользователь
            if guess < secret_number:
                print("Слишком маленькое число! Попробуй еще.")
            elif guess > secret_number:
                print("Слишком большое число! Попробуй еще.")
            else:
                print(f"\n🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break

            # Подсказка о количестве оставшихся попыток
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Осталось попыток: {remaining}")
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