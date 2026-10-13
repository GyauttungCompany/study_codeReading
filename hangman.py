# random 라이브러리 가져오기
import random

# 미리 만들어 놓은 문자열에서 임의로 하나를 골라 반환하는 함수
def get_random_word():
    # 미리 문자열들을 만들어서 words에 보관
    words = ["python", "apple", "banana", "computer", "guitar"]
    # words에서 랜덤하게 하나를 골라서 반환
    return random.choice(words)

# 게임 진행 문자 출력 예 : _ _ _ _, p _ _ _ _ _
def display_word(secret_word, guessed_letters):
    # 사용자가 입력한 문자가 랜덤으로 선택된 문자 안에 포함되어 있다면 그 문자를 아니라면 _를 반환
    result = [letter if letter in guessed_letters else "_" for letter in secret_word]
    # 결과를 " "를 포함해서 출력함.
    return " ".join(result)

# 게임 실행 함수
def play_game():
    # 랜덤 문자 가져오기
    secret_word = get_random_word()
    # 사용자가 입력한 문자를 담을 리스트
    guessed_letters = []
    # 남은 목숨
    lives = 6

    # 게임 UI 출력
    print("=== 단어 맞추기 게임 (Hangman) ===")

    # 목숨이 0보다 크다면 계속 게임을 진행
    while lives > 0:
        # 현재 단어: _ _ _ _ _ _ 이런식으로 출력
        print("\n현재 단어:", display_word(secret_word, guessed_letters))
        # 남은 기회: 출력
        print(f"남은 기회: {lives}")
        # 입력했던 글자들: a, b, c 이런식으로 출력됨
        print("입력했던 글자들:", ", ".join(guessed_letters) if guessed_letters else "없음")
        # 사용자의 입력을 받아서 소문자로 전환
        guess = input("글자를 하나 입력하세요: ").lower()
        # 입력한 문자가 알파벳인지 그리고 1개만 입력했는지 검사.
        if len(guess) != 1 or not guess.isalpha():
            print("알파벳 한 글자만 올바르게 입력해주세요.")
            # 이상하게 입력하면 처음으로
            continue
        # 이미 입력했던 문자인지 검사
        if guess in guessed_letters:
            print("이미 입력했던 글자입니다. 다른 글자를 시도해보세요.")
            # 처음으로
            continue
        # 입력한 문자를 guessed_letters에 추가
        guessed_letters.append(guess)
        # 입력한 문자가 랜덤 문자열에 포함되어 있다면
        if guess in secret_word:
            print(f"좋습니다! '{guess}' 글자가 단어에 들어있습니다.")
        # 입력한 문자가 랜덤 문자열에 포함되어 있지 않다면
        else:
            print(f"아쉽네요! '{guess}' 글자는 단어에 없습니다.")
            # 목숨 차감
            lives -= 1
        # 입력한 문자들이 랜덤 문자열 안에 전부 있다면
        if all(letter in guessed_letters for letter in secret_word):
            print(f"\n축하합니다! 정답 단어 '{secret_word}'를 맞추셨습니다!")
            return

    print(f"\n기회를 모두 소진하셨습니다. 정답은 '{secret_word}'였습니다.")
# 게임 시작.
play_game()