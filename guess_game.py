# guess_game.py
import random

def guess_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Chào mừng đến với Game Đoán Số!")
    print("Mình đã nghĩ ra một số từ 1 đến 100. Bạn đoán xem nó là số nào?")
    
    while True:
        try:
            guess = int(input("Nhập số bạn đoán: "))
            attempts += 1
            if guess < number_to_guess:
                print("Số mình nghĩ lớn hơn!")
            elif guess > number_to_guess:
                print("Số mình nghĩ nhỏ hơn!")
            else:
                print(f"Chúc mừng! Bạn đã đoán đúng số {number_to_guess} sau {attempts} lần thử.")
                break
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

if __name__ == "__main__":
    guess_game()
