# Text Processor
# Copyright (C) 2018 D. Michael Parrish
# 
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public
# License along with this program.  If not, see
# <https://www.gnu.org/licenses/>.
#
# END OF COPYRIGHT NOTICE
#
#

#                       SYSTEM BOOTSTRAP
#
#
# DESIGN
#
# Edit TEMP_PATH to indicate the directory where the files of
# this system are stored.
#
# Add or remove any files from the long list of py files. The
# system is designed so that files loaded later may depend on
# the objects that are created by exec-ing the files loaded
# earlier.
#
# Bootstrap the system from the >>> prompt with on *nix or
# Windows:
# 
# f = open('~/CODE/Py/3/TP/bootstrap.py'); exec(f.read()); f.close(); del(f)
# f = open('p:/bootstrap.py');             exec(f.read()); f.close(); del(f)
#
#
# HISTORY
#
# 2018-09-25:   added characters.py
# 2018-07-12:   added import of stdout
# 2017-12-18:   Refactor, eliminate variables, added clean-up
#               (del), begin to factor out path.
# 2017-12:      modified

STDERR_PREFIX = '2> '

TEMP_PATH = 'p:/'
from sys import stderr, stdin, stdout
print(
    STDERR_PREFIX + 'bootstrap.py: Attempting exec on contents of files...',
    file=stderr)
for TEMP_FILENAME in map(lambda filename: filename + '.py', '''
        5000restore
        '''.split()):
    with open(TEMP_PATH + TEMP_FILENAME) as TEMP_FILE:
        print(
            STDERR_PREFIX +
            'bootstrap.py: Loading and exec-ing:',
            '\n\t\t'.expandtabs(4),
            TEMP_FILE.name,
            sep='', end='', file=stderr)
        exec(TEMP_FILE.read())
        print(file=stderr)

del(TEMP_FILE, TEMP_FILENAME, TEMP_PATH) # should delete all variables created within this script

