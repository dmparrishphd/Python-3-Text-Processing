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

def freadentire(filename): ###
    '''Return entire contents of file specified by the string
    filename. History--- 2017-12-28: changed argument name;
    changed argument to positional argument.'''
    with open(filename) as f:
        return f.read()

def opena(filename): ###
    return open(filename, 'a')

def fopenw(filename): ###
    return open(filename, 'w')

def fread(file, n=1): ###
    '''Wrapper for file.read(n)'''
    return file.read(n)

def freset(file, position=0): ###
    '''Sets (absolute) file position. Returns the file.'''
    file.seek(position);   return file

def rewind(file): #.#
    '''Sets file position to beginning. Returns the file.'''
    return freset(file)

def fread_previous(f, n=1024): ###
    '''Reads from file f the previous n *characters* or the
    number which occur before the current file position, if
    there are fewer than n. Restores f to original position.
    Reminder: multiple *bytes* may form the end-of-line
    marker.'''
    pos  = f.tell()
    newpos = max(0, p - n)
    f.seek(newpos)
    ret = f.read(pos - newpos)
    f.seek(pos)
    return ret

def decononadvancingfilefunction(file_function): ###
    '''Intended as a function decorator. Given a function whose
    first argument is a file, returns a function that has the
    same effect, except that the position of the file in
    question is restored to its initial position upon return.'''
    def nonadvancingfilefunction(file, *args, **kwargs):
        pos = file.tell()
        ret = file_function(file, *args, **kwargs)
        file.seek(pos)
        return ret
    return nonadvancingfilefunction

