# This file is a mockup of a configuration file, the user does not need to know
# where the objects come from or how to init them. As such, it has no imports,
# and no objects are defined within it. They are provided at run time by the
# PyConfig class.

function()

print('in test_config,py: ', params.parameters)
params.add_parameter('c')

print('in test_config,py: ', test_dict)
test_dict['e'] = 10
