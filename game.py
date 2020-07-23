import hashlib


class Game:
  def __init__(self):
    self._players = []
    self._total_kills = 0
    self._kills = {}
  

  def add_player(self, user_name: str, user_id: int):
    self._players.append(user_name)
    self._kills[user_id] = {"name": user_name, "score": 0}
  

  def __str__(self) -> str:
    output = f"{{\n    total_kills: {self._total_kills};\
    \n    players: {self._players};\
    \n    kills: {{\n"
    
    for user_id in self._kills.values():
      output += f"        \"{user_id['name']}\": {user_id['score']},\n"

    output += "    }\n}"

    return output


  def __repr__(self) -> dict:
    return str({"total kills": self._total_kills, "players": self._players, "kills": self._kills})
  

  def generate_hash(self) -> str:
    return hashlib.sha256(self.__repr__().encode('utf-8')).hexdigest()
  

  def data_to_store(self):
    return {"total kills": self._total_kills, "players": self._players, "kills": self._kills}