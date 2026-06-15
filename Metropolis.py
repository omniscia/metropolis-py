#!/usr/bin/env python
# 
# Copyright (c) 2001 Vivake Gupta (vivakeATomniscia.org).  All rights reserved.
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#
# This software is maintained by Vivake (vivakeATomniscia.org) and is available at:
#     /~vivake/python/Metropolis.py


""" Simplex - Metropolis-Hastings Algorithm for Monte Carlo Simulations

Metropolis minimizes an arbitrary nonlinear function of N variables by the
Nedler-Mead Simplex method as described in:

Metropolis N., Rosenbluth A.W., Rosenbluth M.N., Teller A.H. and Teller E. 
    "Equations of state calculations by fast computing machines." 
    Journal of Chemical Physics 21 (1953): 1087-1091.

Hastings, W. K. "Monte Carlo sampling methods using Markov chains and their 
    applications." Biometrika 57 (1970): 97-109. 

It makes no assumptions about the smoothness of the function being minimized.
It converges to a local minimum which may or may not be the global minimum
depending on the initial guess used as a starting point.
"""

import math
import copy

class Metropolis:
    def __init__(self, objFunc, possibles, randomizer, start, reduction):
        pass

    def minimize(self):
        pass


cities = [[0, 4], [3, 6], [2, 7], [3, 7]]

possibles = []
for w in range(1, len(cities)):
    for x in range(1, len(cities)):
        for y in range(1, len(cities)):
            for z in range(1, len(cities)):
                possibles = possibles + [[w, x, y, z]]

def objFunc(args):
    dist = 0.0
    for x in range(1, len(args)):
        dist = dist + math.sqrt(math.pow(cities[x-1][0] - cities[x][0], 2) + math.pow(cities[x-1][1] - cities[x][1], 2))
    dist = dist + math.sqrt(math.pow(cities[len(args) - 1][0] - cities[0][0], 2) + math.pow(cities[len(args) - 1][1] - cities[0][1], 2))

    return dist

def main():
    print(objFunc([2, 3, 1, 0]))

if __name__ == '__main__':
    main()
