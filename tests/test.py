from pyconf.conf import PyConfig

def function():
    print('function print')

config = PyConfig('test_config.py')
config.provide('test_function', function)
out = config.run()
print(out)
