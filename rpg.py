import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power

    def is_alive(self):
        return self.hp > 0

    def attack(self, target):
        damage = random.randint(int(self.attack_power * 0.8), int(self.attack_power * 1.2))
        print(f"⚔️ {self.name}(이)가 {target.name}에게 {damage}의 데미지를 입혔습니다!")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"   ({f'{self.name} 남은 체력: {self.hp}/{self.max_hp}'})")

    def heal(self):
        heal_amount = 20
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"🧪 {self.name}(이)가 체력을 {heal_amount} 회복했습니다! (현재 체력: {self.hp}/{self.max_hp})")


def main():
    print("=== RPG 전투 텍스트 게임 ===")
    
    player = Character(name="용사", hp=100, attack_power=18)
    monster = Character(name="슬라임", hp=60, attack_power=12)

    print(f"\n{monster.name}(이)가 나타났다!\n")

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

        if monster.is_alive():
            monster.attack(player)

        print()
        turn += 1

    if player.is_alive():
        print(f"🎉 {monster.name}을(를) 처치했습니다! 승리!")
    else:
        print(f"💀 {player.name}(이)가 쓰러졌습니다... 패배!")


main()