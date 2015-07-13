import const

class Bot:
  """ Bot
  
  Public attributes:

  cell          - The cell the bot is at
  player_id     - ID of the bot's owner
  hp            - HP of the bot
  robot_id      - Unique identifier for friendly bots
  is_friendly   - Whether this bot belongs the the player

  Public methods:

  set_command   - Set the command to be issued for this bot
  get_command   - Get the command to be issued for this bot

  """

  def set_command(self, cmd):
    self._cmd = cmd

  def get_command(self):
    return self._cmd

  def __init__(self, robot):
    self.cell = const.CELL_ID[robot.location[1]][robot.location[0]]
    self.player_id = robot.player_id
    self.hp = robot.hp
    if hasattr(robot, 'robot_id'):
      self.robot_id = robot.robot_id
      self.is_friendly = True
    else:
      self.is_friendly = False
    self._cmd = None

  def __str__(self):
    return str(self.__dict__)

  def __repl__(self):
    return self.__str__()
