class PlagueGame:
    def __init__(self):
        self.budget = 100
        self.score = 0
        self.progress = 0
        self.win_condition = 100
        self.loss_condition = 0
        self.game_over = False

    def display_menu(self):
        print("1. Play Game")
        print("2. Exit")

    def play_game(self):
        while not self.game_over:
            self.display_status()
            self.take_action()
            self.update_game_state()

    def display_status(self):
        print(f"Budget: {self.budget}")
        print(f"Score: {self.score}")
        print(f"Progress: {self.progress}/{self.win_condition}")
        print("---")

    def take_action(self):
        action = input("Choose an action (spend, gain): ").strip().lower()
        if action == "spend":
            self.spend_budget()
        elif action == "gain":
            self.gain_resources()

    def spend_budget(self):
        amount = int(input("Enter amount to spend: "))
        if amount <= self.budget:
            self.budget -= amount
            self.score += amount // 10
            print(f"Spent {amount}, new budget: {self.budget}, new score: {self.score}")
        else:
            print("Not enough budget!")

    def gain_resources(self):
        gain = int(input("Enter resources gained: "))
        self.budget += gain
        self.progress += gain
        print(f"Gained {gain}, new budget: {self.budget}, progress: {self.progress}/{self.win_condition}")

    def update_game_state(self):
        if self.progress >= self.win_condition:
            print("You win!")
            self.game_over = True
        elif self.budget <= self.loss_condition:
            print("Game over! You lost.")
            self.game_over = True

if __name__ == '__main__':
    game = PlagueGame()
    game.display_menu()
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        game.play_game()
    elif choice == "2":
        print("Exiting game...")
    else:
        print("Invalid choice!")