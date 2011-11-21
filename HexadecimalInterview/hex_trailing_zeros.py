#!/usr/bin/env python
#
# A solution for the Hexadecimal puzzle solution, 
#   http://codercharts.com/puzzle/hexadecimal-interview
#
# Copyright 2011 Nicolas Remond (https://github.com/nire)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


def trailing_zeros(n):
	pow = 0
	twos = 0
	while True:
		pow += 1
		d = 2**pow
		if n < d:
			break
		twos += int(n/d)
		
	return twos / 4
		

def main(argv):
	if len(argv) != 2 :
		print argv[0] + " takes exactly 1 arguments"
		exit(0)

	with open(argv[1],'r') as f:
		f.readline() # first line is useless for us
		
		for line in f.readlines():
			print trailing_zeros(int(line))


# -- The following code executes upon command-line invocation
if __name__ == "__main__": 
	import sys
	main(sys.argv)