""" const.py

Cell constants

NUM_CELLS       - Number of cells on the map
CELLS           - List of the cells (cell ID) on the map
CELL_ID[r][c]   - Mapping from (r,c) to cell id
CELL_R[cell]    - Mapping from cell id to row number
CELL_C[cell]    - Mapping from cell id to column number
NUM_SPAWNS      - Number of spawn cells on the map
SPAWNS          - List of spawn cells on the map
IS_SPAWN[cell]  - True at cell if it is a spawn
ADJ[cell]       - All cells adjacent to a cell
ADJ2[cell]      - All cells distance 2 from a cell

Command constants

CMD_SUICIDE   - Command ID for suicide
CMD_GUARD     - Command ID for guard
CMD_MOVE      - Command ID for moving to a certain cell
CMD_ATTACK    - Command ID for attacking a certain cell
IS_MOVE       - Whether a command ID is a move command
CELL_MOVE     - Cell ID for a certain move command
IS_ATTACK     - Whether a command ID is an attack command
CELL_ATTACK   - Cell ID for a certain attack command
CMDS          - All valid commands for a certain cell

"""

import rg

NUM_CELLS = 0
CELLS = []
NUM_SPAWNS = 0
SPAWNS = []
IS_SPAWN = []
CELL_ID = [[None for c in xrange(19)] for r in xrange(19)]
CELL_R = []
CELL_C = []
for r in xrange(19):
  for c in xrange(19):
    if 'obstacle' not in rg.loc_types((r,c)):
      CELLS.append(NUM_CELLS)
      CELL_ID[r][c] = NUM_CELLS
      CELL_R.append(r)
      CELL_C.append(c)
      if 'spawn' in rg.loc_types((r,c)):
        SPAWNS.append(NUM_CELLS)
        IS_SPAWN.append(True)
        NUM_SPAWNS += 1
      else:
        IS_SPAWN.append(False)
      NUM_CELLS += 1

ADJ = [[] for cell in CELLS]
for r in xrange(19):
  for c in xrange(19):
    if CELL_ID[r][c] != None:
      if r - 1 >= 0 and CELL_ID[r - 1][c] != None:
        ADJ[CELL_ID[r][c]].append(CELL_ID[r - 1][c])
      if r + 1 < 19 and CELL_ID[r + 1][c] != None:
        ADJ[CELL_ID[r][c]].append(CELL_ID[r + 1][c])
      if c - 1 >= 0 and CELL_ID[r][c - 1] != None:
        ADJ[CELL_ID[r][c]].append(CELL_ID[r][c - 1])
      if c + 1 < 19 and CELL_ID[r][c + 1] != None:
        ADJ[CELL_ID[r][c]].append(CELL_ID[r][c + 1])

ADJ2 = [[] for cell in CELLS]
for cell in CELLS:
  for c1 in ADJ[cell]:
    for c2 in ADJ[c1]:
      if c2 != cell and c2 not in ADJ[cell]:
        ADJ2[cell].append(c2)

CMD_SUICIDE = 0
CMD_GUARD = 1
CMD_MOVE = range(2, NUM_CELLS + 2)
CMD_ATTACK = range(NUM_CELLS + 2, NUM_CELLS + NUM_CELLS + 2)
IS_MOVE = [False for cmd in xrange(NUM_CELLS + NUM_CELLS + 2)]
CELL_MOVE = [None for cmd in xrange(NUM_CELLS + NUM_CELLS + 2)]
IS_ATTACK = [False for cmd in xrange(NUM_CELLS + NUM_CELLS + 2)]
CELL_ATTACK = [None for cmd in xrange(NUM_CELLS + NUM_CELLS + 2)]
for cell in CELLS:
  IS_MOVE[CMD_MOVE[cell]] = True
  CELL_MOVE[CMD_MOVE[cell]] = cell
  IS_ATTACK[CMD_ATTACK[cell]] = True
  CELL_ATTACK[CMD_ATTACK[cell]] = cell
CMDS = [[] for cell in CELLS]
for cell in CELLS:
  CMDS[cell].append(CMD_SUICIDE)
  CMDS[cell].append(CMD_GUARD)
  for c in ADJ[cell]:
    CMDS[cell].append(CMD_MOVE[c])
    CMDS[cell].append(CMD_ATTACK[c])
