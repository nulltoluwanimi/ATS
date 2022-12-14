class TicTacToe:
    def __init__(self):
        self.board = ['0', '0', '0',
                      '0', '0', '0',
                      '0', '0', '0']

        self.game_stll_going = True
        self.winner = None
        self.current_player = "X"

    def display_board(self):
        print(self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print(self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print(self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def play_game(self):
        self.display_board()
        while self.game_stll_going:
            self.handle_turn(self.current_player)
            self.check_if_game_over()
            self.flip_player()

        if self.winner == "X" or self.winner == "O":
            print(self.winner + " Won. ")
        elif self.winner is None:
            print(" Tie. ")

    def handle_turn(self, player):
        print(player + "'s turn.")
        positions = input("Choose a position from 1-9 ")

        valid = False
        while not valid:
            while positions not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                positions = input("Invalid input. Choose a position from 1-9 ")
            positions = int(positions) - 1

            if self.board[positions] == "0":
                valid = True
            else:
                print("You cant go there. Go again.")

        self.board[positions] = player

        self.display_board()

    def check_if_game_over(self):
        self.check_for_winner()
        self.check_if_tie()

    def check_for_winner(self):

        row_winner = self.check_row()
        columns_winner = self.check_column()
        diagonals_winner = self.check_diagonals()

        if row_winner:
            self.winner = row_winner
        elif columns_winner:
            self.winner = columns_winner
        elif diagonals_winner:
            self.winner = diagonals_winner
        else:
            self.winner = None
        return

    def check_row(self):

        row_1 = self.board[0] == self.board[1] == self.board[2] != "0"
        row_2 = self.board[3] == self.board[4] == self.board[5] != "0"
        row_3 = self.board[6] == self.board[7] == self.board[8] != "0"

        if row_1 or row_2 or row_3:
            self.game_stll_going = False

        if row_1:
            return self.board[0]
        elif row_2:
            return self.board[3]
        elif row_3:
            return self.board[6]
        return

    def check_column(self):

        column_1 = self.board[0] == self.board[3] == self.board[6] != "0"
        column_2 = self.board[1] == self.board[4] == self.board[7] != "0"
        column_3 = self.board[2] == self.board[5] == self.board[8] != "0"

        if column_1 or column_2 or column_3:
            self.game_stll_going = False

        if column_1:
            return self.board[0]
        elif column_2:
            return self.board[1]
        elif column_3:
            return self.board[2]
        return

    def check_diagonals(self):

        diagonals_1 = self.board[0] == self.board[4] == self.board[8] != "0"
        diagonals_2 = self.board[6] == self.board[4] == self.board[2] != "0"

        if diagonals_1 or diagonals_2:
            self.game_stll_going = False

        if diagonals_1:
            return self.board[0]
        elif diagonals_2:
            return self.board[6]
        return

    def check_if_tie(self):
        if "0" not in self.board:
            self.game_stll_going = False
        return

    def flip_player(self):

        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"
        return


play_game = TicTacToe()
play_game.play_game()
