import rg

from game_state import GameState
from const import *
import ai
import log

class Robot:
  def act(self, game):
    if Robot._turn != game.turn:
      Robot._gs = GameState(game)
      Robot._turn = game.turn
      Robot._ai.compute_commands(Robot._gs)
    for bot in Robot._gs.friends:
      if bot.robot_id == self.robot_id:
        cmd = bot.get_command()
        if cmd != None:
          if cmd == CMD_SUICIDE:
            return ['suicide']
          elif cmd == CMD_GUARD:
            return ['guard']
          elif IS_MOVE[cmd]:
            r = CELL_R[CELL_MOVE[cmd]]
            c = CELL_C[CELL_MOVE[cmd]]
            return ['move', (c, r)]
          elif IS_ATTACK[cmd]:
            r = CELL_R[CELL_ATTACK[cmd]]
            c = CELL_C[CELL_ATTACK[cmd]]
            return ['attack', (c, r)]
          else:
            log.e('Unrecognized command! Suiciding... Bot: ' + str(bot))
            return ['suicide']
        else:
          log.e('No command found! Suiciding... Bot: ' + str(bot))
          return ['suicide']
    log.e('Bot was not found! Something has gone horribly wrong. Suiciding... robot_id: ' + str(self.robot_id))
    return ['suicide']

Robot._turn = -1
Robot._ai = ai.AI()
