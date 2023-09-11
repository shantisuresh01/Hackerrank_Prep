'''
Created on Jun 30, 2023

@author: shanti
'''
import re
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        print(f"Calling {func.__name__} {args} {kwargs}")
        value = func(*args, **kwargs)
        return value
    return wrapper_debug
    
@debug
def score_words(l):
    m = map(lambda x: 2 if len(re.findall(r'[aeiouy]', x)) % 2 == 0 else 1, l)
    s = sum(m)
    return s
    
    
if __name__ == '__main__':
    l = ['prgm' 'is','awesome']
    l = ['hacker', 'book']
    score_words(l)