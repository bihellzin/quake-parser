class Game:
  def __init__(self):
    self._players = {}
    self._total_kills = 0


class Players:
  def __init__(self, username: str, user_id: int):
    self._username = username
    self._kills = 0
    self._user_id = user_id


  @property
  def username(self) -> str:
    return self._username


  @username.setter
  def username(self, new_username: str):
    self._username = new_username