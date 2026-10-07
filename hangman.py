import random

def get_random_word():
    words = ["python", "apple", "banana", "computer", "guitar"]
    return random.choice(words)

def display_word(secret_word, guessed_letters):
    result = [letter if letter in guessed_letters else "_" for letter in secret_word]
    return " ".join(result)

def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    lives = 6

    print("=== 단어 맞추기 게임 (Hangman) ===")

    while lives > 0:
        print("\n현재 단어:", display_word(secret_word, guessed_letters))
        print(f"남은 기회: {lives}")
        print("입력했던 글자들:", ", ".join(guessed_letters) if guessed_letters else "없음")

        guess = input("글자를 하나 입력하세요: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 올바르게 입력해주세요.")
            continue

        if guess in guessed_letters:
            print("이미 입력했던 글자입니다. 다른 글자를 시도해보세요.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"좋습니다! '{guess}' 글자가 단어에 들어있습니다.")
        else:
            print(f"아쉽네요! '{guess}' 글자는 단어에 없습니다.")
            lives -= 1

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n축하합니다! 정답 단어 '{secret_word}'를 맞추셨습니다!")
            return

    print(f"\n기회를 모두 소진하셨습니다. 정답은 '{secret_word}'였습니다.")

play_game()