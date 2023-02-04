
# code along with Lauren

class PyPacPoe():
    def __init__(self):
        self.current_player = "X"

        self.no_of_turns = 0

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

    # display a welcome message
    def display_welcome_message(self):
        print('''
        ----------------------
        Let's play Py-Pac-Poe!
        ----------------------
        ''')
        
    def display_board(self):
        print(f'''
            A   B   C
        1)  {self.current_board['a1']}  | {self.current_board['b1']}  | {self.current_board['c1']} 
           -----------
        2)  {self.current_board['a2']}  | {self.current_board['b2']}  | {self.current_board['c2']} 
           -----------
        3)  {self.current_board['a3']}  | {self.current_board['b3']}  | {self.current_board['c3']} 
        ''')
    
    def display_turn(self):
        print(f"Player {self.current_player}'s Move (example B2):")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def get_player_move(self):
        player_move = input("Enter your move: ").lower()
        while not player_move in self.current_board:
            player_move = input("That's not a valid move, try again: ").lower() # checks if this is a valid move

        while self.current_board[player_move] != None:
            player_move = input("This space is taken, try again: ").lower # checks if this is available
        self.current_board[player_move] = self.current_player
    
    def check_for_win(self):
        if self.current_board['a1'] == self.current_board['b1'] and self.current_board['a1'] == self.current_board['c1']:
            # we have a winner
        elif self.current_board['a2'] == self.current_board['b2'] and self.current_board['a2'] == self.current_board['c2']:
            # we have a winner
        elif self.current_board['a3'] == self.current_board['b3'] and self.current_board['a3'] == self.current_board['c3']:
            # we have a winner
        elif self.current_board['a1'] == self.current_board['a2'] and self.current_board['a1'] == self.current_board['a3']:
            # we have a winner  
        elif self.current_board['b1'] == self.current_board['b2'] and self.current_board['b1'] == self.current_board['b3']:
            # we have a winner      
        elif self.current_board['c1'] == self.current_board['c2'] and self.current_board['c1'] == self.current_board['c3']:
            # we have a winner
        elif self.current_board['a1'] == self.current_board['b2'] and self.current_board['a1'] == self.current_board['c3']:
            # we have a winner
        elif self.current_board['a3'] == self.current_board['b2'] and self.current_board['a3'] == self.current_board['c1']:
            # we have a winner
            
                        
    def display_winner(self):
        print(f"Player {self.current_player} has won the game!")

    def display_tie(self):
        print("It was a tie game!")

     
new_game = PyPacPoe()
# new_game.display_welcome_message()
# new_game.display_board()
# new_game.display_turn()
# print(new_game.get_player_move())
new_game.switch_player()
# print(new_game.get_player_move())
