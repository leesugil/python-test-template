import os
from pathlib import Path

from . import parse_code

def compose_path(module: dict) -> str:
    """
    module: { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' }

    Return: 'src/path/package/name/module_name.py'
    """
    src = module['src']
    package = module['package'].replace('.', '/')
    modulef = module['module']+'.py'
    return f"{src}/{package}/{modulef}"

def case_and_test_statement(function, module):
    """
    function: {
                'name': function_name,
                'args': *[{'name': arg_name, 'type': arg_type, 'default': arg_default}, ...],
                'return':,
                'line':
                }
    """
#   def args_statement(arguments):
#       """
#       'args': [{'name': arg_name, 'type': arg_type, 'default': arg_default}, ...]

#       why did i write this??
#       """
#       if not arguments:
#           return ''
#       output = []
#       for a in arguments:
#           ar = f"{a['arg']}"
#           if a['type']:
#               ar += f": {a['type']}"
#           if a['default']:
#               ar += f"={a['default']}"
#           output.append(ar)
#       output = ', '.join(output)
#       return output

    output = f"def test_{function['name']}():"
    
    def case_list(args, return_type):
        """
        'args': *[{'name': arg_name, 'type': arg_type, 'default': arg_default}, ...]
        """
        output = """
    cases = [
                {
                'args': {"""
        output += f"""
                    #{args}"""
#       for a in args:
#           output += f"""
#                   '{a['name']}': ,"""
        output += """
                    },"""
        output += f"""
                #{return_type}"""
        output += """
                'expected': ,
                },
            ]
"""
        return output

    output += case_list(function['args'], function['return'])
    output += f"""
    for case in cases:
        assert {module}.{function['name']}(case['args']) == case['expected']

"""

    return output

def compose_template(module: str, functions: list[dict]):
    """
    module: { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' }
    functions: [{
                'name': function_name,
                'args': *[{'name': arg_name, 'type': arg_type, 'default': arg_default}, ...],
                'return':,
                'line':
                }, ... ]

    Return should contain proper \t, \n
    """
    output = f"""
from {module['package']} import {module['module']}

"""
    for f in functions:
        output += case_and_test_statement(function=f, module=module['module'])

    return output

def generate_template(target_modules: list[str], target_functions: list[str], target_dest: str='.', debug=False):
    """
    target_modules: [ module: { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' }, ... ]
    target_functions: [ 'fc1', 'fc2', ... ]
    target_dest: 'tests/path'
    """
    modules = []
    for m in target_modules:
        # generate template per each module
        module_path = compose_path(module=m)
        functions = parse_code.parse_functions(filepath=module_path, target_functions=target_functions, debug=debug)
        template_body = compose_template(module=m, functions=functions)

        # create tests/src/package/ folder if it doesn't exist (the directory path to {m})
        # create test_{module}.py in the folder
        # forge template using the relevant functions
        module_path = Path(module_path).relative_to(Path(m['src']))
        dest_path = Path(target_dest) / Path(module_path.parent) / Path('test_'+module_path.name)
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dest_path.touch(exist_ok=False)
        dest_path.write_text(template_body)
