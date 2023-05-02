import random
import tkinter as tk

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Game Gunting-Batu-Kertas")
        self.master.configure(bg='#FFFC99')
        self.master.geometry("380x180")

        self.options = ["gunting", "batu", "kertas"]
        self.player_score = 0
        self.komputer_score = 0

        self.player_choice_label = tk.Label(master, text="Pilihan Anda:", bg='#FFFC99', fg="#000000")
        self.player_choice_label.grid(row=0, column=3, padx="20px")

        self.komputer_choice_label = tk.Label(master, text="Pilihan Komputer:", bg='#FFFC99', fg="#000000")
        self.komputer_choice_label.grid(row=1, column=3)

        self.result_label = tk.Label(master, text="", bg='#FFFC99', fg="#000000")
        self.result_label.grid(row=2, column=3, pady="10px")

        self.player_score_label = tk.Label(master, text="Skor Anda: 0", bg='#FFFC99', fg="#000000")
        self.player_score_label.grid(row=3, column=3)

        self.komputer_score_label = tk.Label(master, text="Skor Komputer: 0", bg='#FFFC99', fg="#000000")
        self.komputer_score_label.grid(row=4, column=3)

        self.gunting_button = tk.Button(master, text="Gunting", bg="#B1F8F2", command=lambda: self.play("gunting"))
        self.gunting_button.grid(row=5, column=2, padx="20px")

        self.batu_button = tk.Button(master, text="Batu", bg="#BCD39c", command=lambda: self.play("batu"))
        self.batu_button.grid(row=5, column=3)

        self.kertas_button = tk.Button(master, text="Kertas", bg="#D5B942", command=lambda: self.play("kertas"))
        self.kertas_button.grid(row=5, column=4, padx="20px")
        
        

    def play(self, player_choice):
        try:
            komputer_choice = random.choice(self.options)

            self.player_choice_label.config(text=f"Pilihan Anda: {player_choice}")
            self.komputer_choice_label.config(text=f"Pilihan Komputer: {komputer_choice}")

            if player_choice == komputer_choice:
                result = "Hasilnya seri!"
            elif player_choice == "gunting" and komputer_choice == "kertas":
                result = "Anda menang!"
                self.player_score += 1
            elif player_choice == "batu" and komputer_choice == "gunting":
                result = "Anda menang!"
                self.player_score += 1
            elif player_choice == "kertas" and komputer_choice == "batu":
                result = "Anda menang!"
                self.player_score += 1
            else:
                result = "Komputer menang!"
                self.komputer_score += 1

            self.result_label.config(text=result)
            self.player_score_label.config(text=f"Skor Anda: {self.player_score}")
            self.komputer_score_label.config(text=f"Skor Komputer: {self.komputer_score}")

            if self.player_score == 3 or self.komputer_score == 3:
                self.end_game()
        except Exception as e:
            print("Terjadi kesalahan saat memainkan game:", str(e))

    def end_game(self):
        if self.player_score > self.komputer_score:
            winner = "Anda"
        else:
            winner = "Komputer"

        self.result_label.config(text=f"{winner} memenangkan game!")
        self.gunting_button.config(state=tk.DISABLED)
        self.batu_button.config(state=tk.DISABLED)
        self.kertas_button.config(state=tk.DISABLED)

root = tk.Tk()
game = Game(root)
root.mainloop()
