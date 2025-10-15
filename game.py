import random

def guess_number():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    previous_guess = None
    score = 100  # Начальный счет

    print(f"У тебя есть {max_attempts} попыток!")
    print(f"Твой начальный счет: {score} очков")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}. Введи число: "))
            attempts += 1

            # Штраф за каждую попытку
            score -= 5

            if guess == secret_number:
                bonus = max_attempts - attempts  # Бонус за оставшиеся попытки
                score += bonus * 10
                print(f"\n🎉 Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                print(f"🏆 Твой финальный счет: {score} очков")
                if attempts <= 3:
                    print("⭐ Ты настоящий экстрасенс!")
                elif attempts <= 6:
                    print("👍 Отличный результат!")
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

                # Добавляем небольшую подсказку на середине игры
                if remaining == max_attempts // 2:
                    if secret_number % 2 == 0:
                        print("💡 Подсказка: число четное!")
                    else:
                        print("💡 Подсказка: число нечетное!")
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