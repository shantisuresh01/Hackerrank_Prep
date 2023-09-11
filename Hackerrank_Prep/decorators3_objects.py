'''
Created on Jun 30, 2023

@author: shanti
'''
import operator
import functools
from _operator import itemgetter


def person_lister(f):
    @functools.wraps(f)
    def inner(people):
        # complete the function
        if 1 <= len(people) <= 10:

            getage = itemgetter(2)
            people_sort = sorted(people, key=lambda x : (int(getage(x))))
            peeps = list(map(f, people_sort))
            return peeps
        else:
            return []
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
    
'''
    
Let's use decorators to build a name directory! You are given some information about  people. Each person has a first name, last name, age and sex. Print their names in a specific format sorted by their age in ascending order i.e. the youngest person's name should be printed first. For two people of the same age, print them in the order of their input.

For Henry Davids, the output should be:
Mr. Henry Davids
For Mary George, the output should be:
Ms. Mary George
Input Format
The first line contains the integer , the number of people.
 lines follow each containing the space separated values of the first name, last name, age and sex, respectively.
Constraints

Output Format
Output  names on separate lines in the format described above in ascending order of age.
Sample Input
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle



TestCase #12:
6
Blossom Michael 9 F
Bubbles Kevin 666666666666666 F
Buttercup Jake 4444444444444444444444444444444444444444444444444444444444444444 F
Michael Blossom 8888 M
Kevin Bubbles 7777777 M
Jake Buttercup 555555555555555555555555555555 M


Expected:
Ms. Blossom Michael
Mr. Michael Blossom
Mr. Kevin Bubbles
Ms. Bubbles Kevin
Mr. Jake Buttercup
Ms. Buttercup Jake


'''
    
