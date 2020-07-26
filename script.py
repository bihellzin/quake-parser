import models
from parser import Parser
from models import Games
from access_db import *
from database import engine


if __name__ == '__main__':
  """
  Store the games in the database and print a report of the games in the games.log 
  file
  """
  models.Base.metadata.create_all(bind=engine) # Creates the database if not created yet

  db = get_db()

  file_parser = Parser()

  with open('games.log', 'r') as file:
    file_data = file.read().split('\n')
  
  
  for line in file_data:
    line_elements = line.split()
    try:
      if line_elements[1] == 'InitGame:':
        if not file_parser._game:
          file_parser.new_game_started()
        
        else:
          game_hash = file_parser.generate_hash()
          file_parser.print_game(game_hash)
          
          game = Games()
          game.game_info = file_parser._game.data_to_store()
          game.hash_game = game_hash
          
          db.add(game)
          db.commit()
          file_parser.new_game_started()

      
      elif line_elements[1] == 'Kill:':
        file_parser.check_kill(line_elements[2], line_elements[3])
      
      elif line_elements[1] == 'ClientUserinfoChanged:':
        file_parser.user_info_changed(line_elements)
    
    except IndexError:
      game_hash = file_parser.generate_hash()
      file_parser.print_game(game_hash)
      
      game = Games()
      game.game_info = file_parser._game.data_to_store()
      game.hash_game = game_hash
      
      db.add(game)
      db.commit()
      file_parser.new_game_started()
  

