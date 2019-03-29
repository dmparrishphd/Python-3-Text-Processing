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
def astuple(*args): ###
    '''Combines the separate arguments into one tuple; returns
    the tuple.'''
    return args

def entuple(arg): #.#
    '''Wraps the single argument in a tuple. Returns a tuple whose single
    element is arg.'''
    return astuple(arg)

def tuplefy(arg):
    '''If arg is a tuple, return it. If arg is a list, return
    its conversion to tuple. Otherwise, return a tuple
    whose content is arg.'''
    if isinstance(arg, list):
        return tuple(arg)
    if not isinstance(arg, tuple):
        return astuple(arg)
    return arg