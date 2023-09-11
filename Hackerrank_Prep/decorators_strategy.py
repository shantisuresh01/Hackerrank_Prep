'''
Created on Aug 6, 2023

@author: shanti
'''

strategies = dict()

def handler(role):

    def wrapper(func):
        strategies[role] = func
        def inner(*args, **kwargs):
            
            return func(*args, **kwargs)
            
        return inner
        
    return wrapper


def process_role(role):
    strategy = strategies.get(role)
    strategy()


@handler(role='parent')
def process_parent(data = None):
    '''
    do_logic(data)
    do_another_logic()
    ... 
    register_parent(data)
    register_children(data)
    enroll_children_on_courses(data)
    '''
    print("Parent Process")

@handler(role='student')
def process_student(data = None):
    '''
    register_student(data)
    
    enroll_student_on_courses(data)
    '''
    print("Student Process")


def register(request):
    process_role(request.data['role'])
    
if __name__ == '__main__':
    class Object(object):
        pass
    request = Object()
    request.data = {}
    request.data['role'] = 'parent'
    print(strategies)
    register(request)