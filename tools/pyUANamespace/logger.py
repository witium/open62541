#!/usr/bin/env/python
# -*- coding: utf-8 -*-

###
### Author:  Chris Iatrou (ichrispa@core-vector.net)
### Version: rev 13
###
### This program was created for educational purposes and is released into the
### public domain under the General Public Licence. A copy of the GNU GPL is
### available under http://www.gnu.org/licenses/gpl-3.0.html.
###
### This program is not meant to be used in a production environment. The
### author is not liable for any complications arising due to the use of
### this program.
###

import inspect

###
### Tidy logging helpers
###

LOG_LEVEL_DEBUG  = 4
LOG_LEVEL_INFO   = 2
LOG_LEVEL_WARN   = 1
LOG_LEVEL_ERROR  = 0
LOG_LEVEL_SILENT = -1

# Change the following to filter logging output
GLOBAL_LOG_LEVEL = LOG_LEVEL_DEBUG

def log(callee, logstr, level=LOG_LEVEL_DEBUG):
  prefixes = { LOG_LEVEL_DEBUG : "DBG: ",
               LOG_LEVEL_INFO  : "INF: ",
               LOG_LEVEL_WARN  : "WRN: ",
               LOG_LEVEL_ERROR : "ERR: ",
               LOG_LEVEL_SILENT: ""
            }
  if level <= GLOBAL_LOG_LEVEL:
    if prefixes.has_key(level):
      print str(prefixes[level]) + callee.__class__.__name__ + "." + inspect.stack()[1][3] +  "(): " + logstr
    else:
      print callee.__class__.__name__  + "." + inspect.stack()[1][3] + "(): " + logstr