#!/usr/bin/env python3

# -*- coding: utf-8 -*-

"""
Author: Dorin Geman

 === Deploy & Run A CLion Lab Project ===

Usage: ./deployLab <number_of_lab>
Python Version: 3.6.7
"""

import os
import sys

print('BOMBOCLAT!')

try:
	sys.argv[1]
except IndexError:
	print('Usage: ./deployLab <number_of_lab>')
	sys.exit()

LAB = sys.argv[1]

if not LAB.isdigit():
	print('Error: <number_of_lab> is not a number')
	sys.exit()

if len(LAB) is 1:
	LAB = '0' + LAB

SKEL = 'skel-lab' + LAB + '.zip'

if not os.path.exists(SKEL):
	print('Error: ' + SKEL + ' doesn\'t exist')
	sys.exit()

LAB = 'Lab' + LAB

os.system('unzip -q ' + SKEL + ' && mkdir ' + LAB)

SKEL = SKEL[:-len('.zip')]

os.system('mv {0}/cpp {0}/check.sh {0}/tests {1}/ && rm -r {0}'.format(SKEL, LAB))

CMake = '''cmake_minimum_required(VERSION 3.13)
project({0})

set(CMAKE_CXX_STANDARD 14)

add_executable({0} main.cpp)'''.format(LAB)

for task in sorted(os.listdir(LAB + '/cpp/')):
	CMake += '\nadd_executable({0} cpp/{0}/main.cpp)'.format(task)

with open(LAB + '/CMakeLists.txt', 'w+') as CMakeFile:
	print(CMake, file = CMakeFile)

with open(LAB + '/main.cpp', 'w+') as mainFile:
	print('''#include <iostream>

int main() {
	std::cout << "BOMBOCLAT!\\n";
	return 0;
}''', file = mainFile)

os.system('clion ' + LAB + '/')