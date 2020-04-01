from pyconf.conf import PyConfig

def test_function():
    print('test_function print')

config = PyConfig('test_config.py')
config.provide('c', test_function)
out = config.run()
print(out)
