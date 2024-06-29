import random

def guess_number():
    return random.randint(1, 100)

while True:
    max_attempts = int(input("enter number for your attempts: "))  # طلب عدد المحاولات قبل بدء اللعبة
    number_to_guess = guess_number()
    attempts = 0

    while attempts < max_attempts:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if guess > number_to_guess:
            print("Too high number, Try lower number")
        elif guess < number_to_guess:
            print("Too low! number, Try higher number")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts with the max attempts {max_attempts}.")
            break  # كسر الحلقة الداخلية عند التخمين الصحيح

    else:  # يتم تنفيذ هذه الكتلة إذا انتهت الحلقة الداخلية بدون تخمين صحيح
        print(f"You've run out of attempts. The number was {number_to_guess}.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":  # تصحيح الخطأ في التحقق من تكرار اللعب
        break
