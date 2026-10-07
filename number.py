import random

secret_number = random.randint(1, 100)
attempts = 0

print("=== 1부터 100 사이의 숫자 맞추기 게임 ===")

while True:
    guess_input = input("숫자를 입력하세요 (종료하려면 'q'): ")

    if guess_input.lower() == 'q':
        print(f"게임을 포기하셨습니다. 정답은 {secret_number}였습니다.")
        break

    if not guess_input.isdigit():
        print("올바른 숫자를 입력하거나 'q'를 입력하세요.")
        continue

    guess = int(guess_input)
    attempts += 1

    if guess < secret_number:
        print("UP! 더 큰 숫자를 입력하세요.")
    elif guess > secret_number:
        print("DOWN! 더 작은 숫자를 입력하세요.")
    else:
        print(f"축하합니다! {attempts}번 만에 정답({secret_number})을 맞추셨습니다!")
        break