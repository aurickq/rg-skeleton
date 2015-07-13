"""
Logging module for robotgame.

log.i for general information.
log.w for warnings.
log.e for errors.

Example:

>>> import log
>>> log.i('This is a log message!')

"""

def _log(lvl, msg):
  print '[' + lvl + '] ' + msg

i = lambda msg: _log('II', msg)
w = lambda msg: _log('WW', msg)
e = lambda msg: _log('EE', msg)
