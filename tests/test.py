from pyconf import PyConfig

def function():
    print('function print')

class Parameters:
    def __init__(self, parameters=[]):
        self.parameters = parameters

    def add_parameter(self, param: str):
        self.parameters.append(param)

test_dict = {'d': 5}

params = Parameters(['a', 'b'])
config = PyConfig('test_config.py')
# providing the objects
config.provide('function', function)
config.provide('params', params)
config.provide('test_dict', test_dict)
# running the file
out = config.run()
# our objects are modified !
print('in test.py: ', out)
print('in test.py: ', params.parameters)
print('in test.py: ', test_dict)
