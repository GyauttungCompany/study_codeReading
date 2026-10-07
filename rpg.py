import random

# 1. 캐릭터(플레이어와 몬스터)의 기본 틀이 되는 클래스 정의
class Character:
    # __init__은 객체가 생성될 때 자동으로 실행되는 생성자 메서드입니다.
    def __init__(self, name, hp, attack_power):
        self.name = name          # 캐릭터 이름
        self.hp = hp              # 현재 체력
        self.max_hp = hp          # 최대 체력
        self.attack_power = attack_power  # 공격력

    # 살아있는지 확인하는 메서드
    def is_alive(self):
        return self.hp > 0

    # 상대방을 공격하는 메서드
    def attack(self, target):
        # 80%~120% 범위의 무작위 데미지 계산
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        print(f"⚔️ {self.name}(이)가 {target.name}에게 {damage}의 데미지를 입혔습니다!")
        target.take_damage(damage)

    # 데미지를 받는 메서드
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"   ({target_status := f'{self.name} 남은 체력: {self.hp}/{self.max_hp}'})")

    # 체력을 회복하는 메서드
    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"🧪 {self.name}(이)가 체력을 {heal_amount} 회복했습니다! (현재 체력: {self.hp}/{self.max_hp})")


# 2. 게임을 실행하는 메인 로직
def main():
    print("=== RPG 전투 텍스트 게임 ===")
    
    # Character 클래스를 사용해 '플레이어'와 '몬스터' 객체(인스턴스)를 각각 만듭니다.
    player = Character(name="용사", hp=100, attack_power=18)
    monster = Character(name="슬라임", hp=60, attack_power=12)

    print(f"\n{monster.name}(이)가 나타났다!\n")

    # 두 캐릭터가 모두 살아있는 동안 전투 진행
    turn = 1
    while player.is_alive() and monster.is_alive():
        print(f"--- [Turn {turn}] ---")
        action = input("행동을 선택하세요 (1: 공격, 2: 회복): ")

        if action == "1":
            player.attack(monster)
        elif action == "2":
            player.heal()
        else:
            print("잘못된 입력입니다. 기회를 날렸습니다!")

        # 몬스터가 아직 살아있다면 플레이어를 공격
        if monster.is_alive():
            monster.attack(player)

        print()
        turn += 1

    # 승패 결과 출력
    if player.is_alive():
        print(f"🎉 {monster.name}을(를) 처치했습니다! 승리!")
    else:
        print(f"💀 {player.name}(이)가 쓰러졌습니다... 패배!")


# 프로그램 시작
main()