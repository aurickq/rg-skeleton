import const
import log

class AI:
  def compute_commands(self, gs):
    """
    This is the main function that computes moves for every bot in a turn.
    Global variable sharing has already been taken care of in robot.py. The
    parameter gs is a GameState object, defined in game_state.py. Commands
    are issued to each bot by calling bot.set_command(cmd) before each turn is
    over. Some helpful constants can be found in const.py.
    """

    log.i('Computing commands for turn ' + str(gs.turn))
    
    for bot in gs.friends:
      bot.set_command(const.CMD_GUARD)
