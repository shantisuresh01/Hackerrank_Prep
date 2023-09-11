'''
Created on Jun 29, 2023

@author: shanti
'''

import string

def get_num_lines(size):
    num_lines = 2 * size - 1
    return num_lines
def get_width(size):
    width = 4 * size - 3
    return width

def get_dashes(distance):
    # 2 * distance
    dashes = '-' * (distance * 2)
    return dashes
def get_welcome_line(width):
    dashes = get_dashes((width - 7) / 2)
    welcome_line = dashes + 'WELCOME' + dashes
    return welcome_line
def get_letters(size):
    letters = string.ascii_lowercase[:size]
    # reverse the lettters
    return letters[::-1]
    
def get_pattern(row_index, letters):
    pattern = ''
    if row_index == 0:
        pattern = pattern + letters[row_index]
        return pattern
    for i in range(row_index + 1):
        pattern = pattern + '-' if i != 0 else pattern
        pattern = pattern + letters[i]
    for i in range(row_index, 0, -1):
        pattern = pattern + '-' + letters[i-1]
    return pattern
def get_lines(size):
    lines = {}
    center_index = size - 1
    letters = get_letters(size)
    for i in range(center_index + 1):
        distance = abs((center_index - i))
        dashes = get_dashes(distance)
        pattern = get_pattern(i, letters)
        #print(f"i:{i}")
        lines[i] = dashes + pattern + dashes
    return lines
        
def print_lines(size, lines):
    center_index = size - 1
    for i in range(center_index + 1):
        print(lines[i])
    for i in range(center_index-1, -1, -1):
        print(lines[i])

def print_rangoli(size):
    nLines = get_num_lines(size = size)
    width = get_width(size = size)
    lines = get_lines(size = size)
    print_lines(size = size, lines = lines)
    
 
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)