import random
import os
import time

class RockPaperScissors:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.total_rounds = 0
        self.choices = {
            '1': 'rock',
            '2': 'paper',
            '3': 'scissors',
            'rock': 'rock',
            'paper': 'paper',
            'scissors': 'scissors',
            'r': 'rock',
            'p': 'paper',
            's': 'scissors'
        }
        
        # ASCII art for choices
        self.ascii_art = {
            'rock': """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
            'paper': """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
            'scissors': """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
        }

    def clear_screen(self):
        """Clear the terminal screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self):
        """Display game header."""
        print("="*60)
        print("🎮 ROCK-PAPER-SCISSORS GAME 🎮")
        print("="*60)
        print()

    def display_rules(self):
        """Display game rules."""
        print("📋 GAME RULES:")
        print("• Rock beats Scissors")
        print("• Scissors beats Paper")
        print("• Paper beats Rock")
        print("• Same choice = Tie")
        print("-" * 40)

    def display_menu(self):
        """Display choice menu."""
        print("🎯 Make your choice:")
        print("1. Rock     (or type 'rock' or 'r')")
        print("2. Paper    (or type 'paper' or 'p')")
        print("3. Scissors (or type 'scissors' or 's')")
        print("4. View Statistics")
        print("5. Reset Scores")
        print("6. Quit Game")
        print("-" * 40)

    def get_user_choice(self):
        """Get and validate user choice."""
        while True:
            choice = input("Enter your choice: ").lower().strip()
            
            if choice in ['4', 'stats', 'statistics']:
                return 'stats'
            elif choice in ['5', 'reset']:
                return 'reset'
            elif choice in ['6', 'quit', 'exit', 'q']:
                return 'quit'
            elif choice in self.choices:
                return self.choices[choice]
            else:
                print("❌ Invalid choice! Please try again.")
                print()

    def get_computer_choice(self):
        """Generate random computer choice."""
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        """Determine the winner of the round."""
        if user_choice == computer_choice:
            return 'tie'
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return 'user'
        else:
            return 'computer'

    def display_choices(self, user_choice, computer_choice):
        """Display both choices with ASCII art."""
        print("🎭 ROUND RESULT:")
        print(f"You chose: {user_choice.upper()}")
        print(self.ascii_art[user_choice])
        
        print(f"Computer chose: {computer_choice.upper()}")
        print(self.ascii_art[computer_choice])

    def display_round_result(self, winner, user_choice, computer_choice):
        """Display the result of the current round."""
        print("🏆 RESULT:")
        if winner == 'tie':
            print("🤝 It's a TIE!")
        elif winner == 'user':
            print("🎉 YOU WIN!")
            if user_choice == 'rock' and computer_choice == 'scissors':
                print("💥 Rock crushes Scissors!")
            elif user_choice == 'scissors' and computer_choice == 'paper':
                print("✂️ Scissors cuts Paper!")
            elif user_choice == 'paper' and computer_choice == 'rock':
                print("📜 Paper covers Rock!")
        else:
            print("🤖 COMPUTER WINS!")
            if computer_choice == 'rock' and user_choice == 'scissors':
                print("💥 Rock crushes Scissors!")
            elif computer_choice == 'scissors' and user_choice == 'paper':
                print("✂️ Scissors cuts Paper!")
            elif computer_choice == 'paper' and user_choice == 'rock':
                print("📜 Paper covers Rock!")

    def update_scores(self, winner):
        """Update game scores."""
        self.total_rounds += 1
        if winner == 'user':
            self.user_score += 1
        elif winner == 'computer':
            self.computer_score += 1
        else:
            self.ties += 1

    def display_current_scores(self):
        """Display current game scores."""
        print("\n📊 CURRENT SCORES:")
        print(f"You: {self.user_score} | Computer: {self.computer_score} | Ties: {self.ties}")
        print(f"Total Rounds: {self.total_rounds}")

    def display_statistics(self):
        """Display detailed game statistics."""
        if self.total_rounds == 0:
            print("📈 No games played yet!")
            return

        print("\n📈 GAME STATISTICS:")
        print("=" * 30)
        print(f"Total Rounds Played: {self.total_rounds}")
        print(f"Your Wins: {self.user_score}")
        print(f"Computer Wins: {self.computer_score}")
        print(f"Ties: {self.ties}")
        print()
        
        if self.total_rounds > 0:
            user_percentage = (self.user_score / self.total_rounds) * 100
            computer_percentage = (self.computer_score / self.total_rounds) * 100
            tie_percentage = (self.ties / self.total_rounds) * 100
            
            print(f"Your Win Rate: {user_percentage:.1f}%")
            print(f"Computer Win Rate: {computer_percentage:.1f}%")
            print(f"Tie Rate: {tie_percentage:.1f}%")
            
            if self.user_score > self.computer_score:
                print("🏆 You're leading!")
            elif self.computer_score > self.user_score:
                print("🤖 Computer is leading!")
            else:
                print("🤝 It's a tie overall!")

    def reset_scores(self):
        """Reset all scores to zero."""
        self.user_score = 0
        self.computer_score = 0
        self.ties = 0
        self.total_rounds = 0
        print("🔄 Scores have been reset!")

    def play_round(self):
        """Play a single round of the game."""
        user_choice = self.get_user_choice()
        
        # Handle special commands
        if user_choice == 'stats':
            self.display_statistics()
            return True
        elif user_choice == 'reset':
            self.reset_scores()
            return True
        elif user_choice == 'quit':
            return False
        
        # Play the round
        computer_choice = self.get_computer_choice()
        
        print("\n🎲 Computer is making its choice...")
        time.sleep(1)
        
        self.display_choices(user_choice, computer_choice)
        
        winner = self.determine_winner(user_choice, computer_choice)
        self.display_round_result(winner, user_choice, computer_choice)
        self.update_scores(winner)
        self.display_current_scores()
        
        return True

    def play_again(self):
        """Ask if user wants to play another round."""
        while True:
            play_again = input("\n🎮 Play another round? (y/n): ").lower().strip()
            if play_again in ['y', 'yes', '']:
                return True
            elif play_again in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' for yes or 'n' for no.")

    def display_final_message(self):
        """Display final game message."""
        print("\n🎊 GAME OVER!")
        if self.total_rounds > 0:
            self.display_statistics()
            print("\nThanks for playing! 🎮")
        else:
            print("Thanks for visiting! Come back anytime! 👋")

    def run(self):
        """Main game loop."""
        self.clear_screen()
        self.display_header()
        self.display_rules()
        
        print("Welcome to Rock-Paper-Scissors! 🎉")
        print("Type 'quit' at any time to exit the game.")
        print()
        
        while True:
            self.display_menu()
            
            if not self.play_round():
                break
            
            if not self.play_again():
                break
            
            self.clear_screen()
            self.display_header()
        
        self.display_final_message()

def main():
    """Main function to start the game."""
    game = RockPaperScissors()
    game.run()

if __name__ == "__main__":
    main()
