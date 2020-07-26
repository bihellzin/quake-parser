import hashlib


class Game:
  def __init__(self):
    self._players = []
    self._total_kills = 0
    self._kills = {}
  

  def add_player(self, user_name: str, user_id: int):
    """
    Add a new player to the game
    """
    self._players.append(user_name)
    self._kills[user_id] = {"name": user_name, "score": 0}
  

  def __str__(self) -> str:
    """
    To make the print(Game_instance) look better
    """
    output = f"{{\n    total_kills: {self._total_kills};\
    \n    players: {self._players};\
    \n    kills: {{\n"
    
    for user_id in self._kills.values():
      output += f"        \"{user_id['name']}\": {user_id['score']},\n"

    output += "    }\n}"

    return output


  def __repr__(self) -> dict:
    """
    To make the repr(Game_instance) look better
    """
    return str({"total kills": self._total_kills, "players": self._players, "kills": self._kills})
  

  def generate_hash(self) -> str:
    "Generate the hash of the game based on the __repr__ returned"
    return hashlib.sha256(self.__repr__().encode("utf-8")).hexdigest()
  

  def data_to_store(self):
    """
    What is going to be stored in the database, this is the Games.game_info
    """
    self.format_kills()
    return {"total kills": self._total_kills, "players": self._players, "kills": self._kills}
  

  def format_kills(self):
    """
    Format the self._kills to use the username as key, instead of user id
    """
    new_kills_format = {}
    for user_id in self._kills:
      new_kills_format[self._kills[user_id]["name"]] = self._kills[user_id]["score"]

    self._kills = new_kills_format