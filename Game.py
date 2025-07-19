import os

class TicTacToe:
    def _init_(self):
        self.board = [[str(i * 3 + j + 1) for j in range(3)] for i in range(3)]
        self.current_player = 'X'

    def display_board(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nTIC TAC TOE - High Level Version\n")
        print("Player 1 (X)  vs  Player 2 (O)\n")
        for i in range(3):
            print(" ", end="")
            for j in range(3):
                print(f" {self.board[i][j]} ", end="")
                if j < 2:
                    print("|", end="")
            if i < 2:
                print("\n---+---+---")
        print("\n")

    def is_winner(self):
        b = self.board
        lines = [
            b[0], b[1], b[2],  # Rows
            [b[0][0], b[1][0], b[2][0]],  # Columns
            [b[0][1], b[1][1], b[2][1]],
            [b[0][2], b[1][2], b[2][2]],
            [b[0][0], b[1][1], b[2][2]],  # Diagonals
            [b[0][2], b[1][1], b[2][0]]
        ]
        return any(line.count(self.current_player) == 3 for line in lines)

    def is_draw(self):
        return all(cell in ['X', 'O'] for row in self.board for cell in row)

    def make_move(self, position):
        row, col = (position - 1) // 3, (position - 1) % 3
        if self.board[row][col] in ['X', 'O']:
            return False
        self.board[row][col] = self.current_player
        return True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.display_board()
            try:
                move = int(input(f"Player '{self.current_player}', enter your move (1-9): "))
                if move < 1 or move > 9:
                    print("Invalid move. Try again.")
                    continue
                if not self.make_move(move):
                    print("Cell already occupied. Try again.")
                    continue
            except ValueError:
                print("Please enter a valid number.")
                continue

            if self.is_winner():
                self.display_board()
                print(f"Player '{self.current_player}' wins! 🎉")
                break
            elif self.is_draw():
                self.display_board()
                print("It's a draw! 🤝")
                break
            self.switch_player()

def main():
    while True:
        game = TicTacToe()
        game.play()
        again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if _name_ == "_main_":
    main()
