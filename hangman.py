import random

# 1. 단어 목록에서 무작위 단어를 하나 고르는 함수
def get_random_word():
    words = ["python", "apple", "banana", "computer", "guitar"]
    return random.choice(words)

# 2. 현재 맞춰야 할 단어의 상태를 표시하는 함수
def display_word(secret_word, guessed_letters):
    # 단어의 각 글자가 맞춘 글자 목록에 있으면 그 글자를, 없으면 '_'로 표시합니다.
    result = [letter if letter in guessed_letters else "_" for letter in secret_word]
    return " ".join(result)

# 3. 메인 게임 진행 함수
def play_game():
    secret_word = get_random_word()
    guessed_letters = []  # 추측한 글자들을 저장할 리스트
    lives = 6            # 기회 횟수

    print("=== 단어 맞추기 게임 (Hangman) ===")

    while lives > 0:
        print("\n현재 단어:", display_word(secret_word, guessed_letters))
        print(f"남은 기회: {lives}")
        print("입력했던 글자들:", ", ".join(guessed_letters) if guessed_letters else "없음")

        guess = input("글자를 하나 입력하세요: ").lower()

        # 알파벳 1글자만 입력했는지 확인
        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 올바르게 입력해주세요.")
            continue

        # 이미 입력한 글자인지 확인
        if guess in guessed_letters:
            print("이미 입력했던 글자입니다. 다른 글자를 시도해보세요.")
            continue

        guessed_letters.append(guess)

        # 정답 단어에 포함된 글자인지 확인
        if guess in secret_word:
            print(f"좋습니다! '{guess}' 글자가 단어에 들어있습니다.")
        else:
            print(f"아쉽네요! '{guess}' 글자는 단어에 없습니다.")
            lives -= 1

        # 단어를 모두 맞췄는지 확인 (모든 글자가 guessed_letters에 포함되었는지)
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n축하합니다! 정답 단어 '{secret_word}'를 맞추셨습니다!")
            return

    print(f"\n기회를 모두 소진하셨습니다. 정답은 '{secret_word}'였습니다.")

# 게임 시작
play_game()