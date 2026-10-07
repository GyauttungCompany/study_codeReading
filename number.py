# random 모듈 가져오기
import random

# 1~100까지의 숫자 중 랜덤으로 하나 가져와서 secret_number에 할당
secret_number = random.randint(1, 100)
# 시도 횟수를 저장할 변수
attempts = 0
# 게임 제목 문구 출력
print("=== 1부터 100 사이의 숫자 맞추기 게임 ===")
# 반복문 시작
while True:
    # 사용자 숫자 입력
    guess_input = input("숫자를 입력하세요 (종료하려면 'q'): ")
    # 사용자가 q를 입력하면 게임 종료. 종료하면서 랜덤 숫자가 무엇인지 알려줌
    # 사용자가 q를 입력했다면
    if guess_input.lower() == 'q':
        # 랜덤 숫자가 무엇인지 알려주고
        print(f"게임을 포기하셨습니다. 정답은 {secret_number}였습니다.")
        # 반복문을 종료
        break
    
    # 사용자가 입력한 내용이 숫자인지 확인.
    if not guess_input.isdigit():
        # 숫자가 아니라면 숫자를 입력하도록 안내
        print("올바른 숫자를 입력하거나 'q'를 입력하세요.")
        # 바로 재입력하도록 반복문 처음으로 이동시킴
        continue
    # input은 문자열을 반환하고 guess_input의 내용이 문자열이어서 int()로 정수로 변환
    guess = int(guess_input)
    # 사용자가 숫자를 옳바르게 입력했으므로 시도 횟수 +1
    attempts += 1
    # 사용자가 입력한 숫자가 랜덤 숫자보다 더 작다면
    if guess < secret_number:
        # 더 큰 숫자를 입력하도록 안내
        print("UP! 더 큰 숫자를 입력하세요.")
    # 사용자가 입력한 숫자가 랜덤 숫자보다 더 크다면
    elif guess > secret_number:
        # 더 작은 숫자를 입력하도록 안내
        print("DOWN! 더 작은 숫자를 입력하세요.")
    # 그 외의 경우는 사용자가 입력한 숫자가 랜덤 숫자와 같은 것이므로
    else:
        # 시도 횟수와 랜덤 숫자를 알려주고
        print(f"축하합니다! {attempts}번 만에 정답({secret_number})을 맞추셨습니다!")
        # 반복문 종료
        break