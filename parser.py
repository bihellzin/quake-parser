from game import Game


class Parser:
  def __init__(self):
    self._game = False
    self._game_number = 1
  

  def check_kill(self, killer_id: int, killed_id: int):
    self._game._total_kills += 1
    
    if killer_id == killed_id or killer_id == '1022':
      self._game._kills[killed_id]["score"] -= 1
    
    else:
      self._game._kills[killer_id]["score"] += 1

  
  def new_game_started(self):
    if self._game:
      # salva os dados no banco de dados e inicia uma nova instacia de jogo
      self._game = Game()
      self._game_number += 1
  
    else:
      self._game = Game()
    

  def user_info_changed(self, line_read: list):
    if len(line_read) == 4:
      current_username = self.get_username(line_read[3])

    else:
      full_info = ''
      for i in range(3, len(line_read)):
        full_info += line_read[i]
      
      current_username = self.get_username(full_info)

    user_id = line_read[2]

    if user_id in self._game._kills.keys():
      if self._game._kills[user_id]['name'] != current_username:
        old_username = self._game._kills[user_id]['name']
        self._game._players[self._game._players.index(old_username)] = current_username
        self._game._kills[user_id]['name'] = current_username
    
    else:
      self._game.add_player(current_username, user_id)
  

  def get_username(self, string: str):
    username = ''
    char_index = 2 # first letter
    char = string[char_index]

    while char != '\\':
      username += char
      char_index += 1
      char = string[char_index]
    
    return username


  def print_game(self, game_hash: str):
    print(f'Game {self._game_number}\n')
    print(f'Hash: {game_hash}\n')
    for user_id in self._game._kills:
      print(f'Score: {self._game._kills[user_id]["score"]}   Player: {self._game._kills[user_id]["name"]}') 
    print('\n # # # # # # # # # # # # # # # # # # # #\n')


  def generate_hash(self):
      return self._game.generate_hash()
    