from bot import Bot
import const

class GameState:
  """ GameState
 
  Public attributes:
  
  turn            - Current turn number
  bots            - List of all bots
  bot_at          - Mapping of cells to bots
  friends         - List of bots belonging to player
  friend_at       - Mapping of cells to friendly bots
  enemies         - List of enemy bots
  enemy_at        - Mapping of cells to enemy bots
  
  """

  def __init__(self, game):
    self.turn = game.turn
    self.bots = []
    self.bot_at = [None for cell in const.CELLS]
    self.friends = []
    self.friend_at = [None for cell in const.CELLS]
    self.enemies = []
    self.enemy_at = [None for cell in const.CELLS]
    for robot in game.robots.values():
      bot = Bot(robot)
      self.bots.append(bot)
      self.bot_at[bot.cell] = bot
      if bot.is_friendly:
        self.friends.append(bot)
        self.friend_at[bot.cell] = bot
      else:
        self.enemies.append(bot)
        self.enemy_at[bot.cell] = bot
  
  def __str__(self):
    return str(self.__dict__)

  def __repl__(self):
    return self.__str__()
