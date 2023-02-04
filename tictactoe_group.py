
# tic tac toe code along with Lauren

class PyPacPoe():
    def __init__(self):
      self.current_player = "X"
      self.no_of_turns = 0
      self.is_winner = False
      self.is_tie = False
      self.current_board = {
          "a1": None,
          "a2": None,
          "a3": None,
          "b1": None,
          "b2": None,
          "b3": None,
          "c1": None,
          "c2": None,
          "c3": None
      }

    def display_welcome_message(self):
        print('''
        ------------------------
        Let's play Py-Pac-Poe!
        ------------------------
        ''')
            
              
    def display_board(self):
        print(f'''
            A   B   C
        1)  {self.current_board['a1']}  |  {self.current_board['b1']} |  {self.current_board['c1']}
          -----------
        2)  {self.current_board['a2']}  |  {self.current_board['b2']} |  {self.current_board['c2']}
          -----------
        3)  {self.current_board['a3']}  |  {self.current_board['b3']} |  {self.current_board['c3']}
        ''')

    def display_turn(self):
        print(f"Player {self.current_player}'s Move (example B2): ")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def get_player_move(self):
        player_move = input("Enter your move: ").lower()
        while not player_move in self.current_board:
            self.display_board()
            player_move = input("That is not a valid move, try again: ").lower()
        while self.current_board[player_move] != None:
             self.display_board()
             player_move = input("This space is taken, try again: ").lower()
        self.current_board[player_move] = self.current_player
        self.no_of_turns += 1

    def check_for_win(self):
        if self.current_board['a1'] == self.current_player and self.current_board['b1'] == self.current_player and self.current_board['c1'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a2'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c2'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a3'] == self.current_player and self.current_board['b3'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a1'] == self.current_player and self.current_board['a2'] == self.current_player and self.current_board['a3'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['b1'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['b3'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['c1'] == self.current_player and self.current_board['c2'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a1'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c3'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.current_board['a3'] == self.current_player and self.current_board['b2'] == self.current_player and self.current_board['c1'] == self.current_player:
            self.is_winner = True
            self.display_winner()
        elif self.no_of_turns == 9 and not self.is_winner:
            self.is_tie = True
            self.display_tie()
        return
            
    def display_winner(self):
        print(f"Player {self.current_player} has won the game!")

    def display_tie(self):
        print("It was a tie game!")

    def play(self):
        while not self.is_winner and not self.is_tie:
          self.display_board()
          self.display_turn()
          self.get_player_move()
          self.display_board()
          self.check_for_win()
          self.switch_player()

    def init_game(self):
        self.display_welcome_message()
        self.play()



        


new_game = PyPacPoe()

new_game.init_game()