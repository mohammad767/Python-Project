import numpy as np
import random

class XO_game:
    
    def __init__(self):
        self.arr = [["", "", ""],
                    ["", "", ""],
                    ["", "", ""]]
        self.tabel = np.array(self.arr)
        self.in_lst = ["0,0", "0,1", "0,2",
                       "1,0", "1,1", "1,2",
                       "2,0", "2,1", "2,2"]
        self.ch = None  # ذخیره انتخاب کاربر (X یا O)
        
    def check_winner(self):
        """بررسی برنده‌ی بازی"""
        for i in range(3):
            # چک کردن سطرها و ستون‌ها
            if self.tabel[i, 0] == self.tabel[i, 1] == self.tabel[i, 2] and self.tabel[i, 0] != "":
                return self.tabel[i, 0]
            if self.tabel[0, i] == self.tabel[1, i] == self.tabel[2, i] and self.tabel[0, i] != "":
                return self.tabel[0, i]
        # چک کردن قطرها
        if self.tabel[0, 0] == self.tabel[1, 1] == self.tabel[2, 2] and self.tabel[0, 0] != "":
            return self.tabel[0, 0]
        if self.tabel[0, 2] == self.tabel[1, 1] == self.tabel[2, 0] and self.tabel[0, 2] != "":
            return self.tabel[0, 2]
        return None  # هیچ برنده‌ای وجود ندارد

    def human(self):
        if self.ch is None:  # فقط یک‌بار انتخاب X یا O را بپرس
            self.ch = input("Choose X or O: ").upper()
            while self.ch not in ["X", "O"]:
                self.ch = input("Invalid choice! Choose X or O: ").upper()
        
        print('\n'.join(' '.join(self.in_lst[i:i + 3]) for i in range(0, len(self.in_lst), 3)))
        self.ind = input("Enter the place of your choice: ")
        while self.ind not in self.in_lst:
            self.ind = input("Invalid choice! Enter a valid place: ")

        self.in_lst[self.in_lst.index(self.ind)] = "__"
        self.ind = self.ind.split(",")  # تبدیل رشته به لیست
        self.tabel[int(self.ind[0]), int(self.ind[1])] = self.ch
    
    def cpu(self):
        cpu_ch = "O" if self.ch == "X" else "X"  # حریف انتخاب می‌شود
        self.ind = random.choice([i for i in self.in_lst if i != "__"])  # انتخاب تصادفی خانه خالی
        self.in_lst[self.in_lst.index(self.ind)] = "__"
        self.ind = self.ind.split(",")
        self.tabel[int(self.ind[0]), int(self.ind[1])] = cpu_ch
        print("CPU move:\n", self.tabel)

    def play_cpu(self):
        for _ in range(9):  # حداکثر ۹ حرکت
            self.human()
            winner = self.check_winner()
            if winner:
                print(f"{winner} Won the game!")
                return "win"

            self.cpu()
            winner = self.check_winner()
            if winner:
                print(f"{winner} Won the game!")
                return "win"

        print("Good Game, It's a Tie!")
    
    def play_human(self):
        for _ in range(9):
            self.human()
            winner = self.check_winner()
            if winner:
                print(f"{winner} Won the game!")
                return "win"

        print("Good Game, It's a Tie!")

def run():
    while True:
        user = XO_game()
        ch = input("Do you want to play with human or CPU? ").lower()
        if ch == "cpu":
            if user.play_cpu() == "win":
                break
        elif ch == "human":
            if user.play_human() == "win":
                break
        else:
            print("Invalid choice! Please enter 'human' or 'cpu'.")

run()
