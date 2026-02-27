import re
from pathlib import Path

def parse_args(args: str) -> list[dict]:
    """
    args: 'x: int=0, y: str'+"='nice'"+', z: str="hell yeah"'
    Return: [{'name': some_argument_name, 'type': data type if specified, 'default': default value if specified}, ...]
    """
    if not args:
        return []
    pattern = r'\s*(\w+):\s*([\w\[\]\(\)]+)=?(.*?)\s*,?'
    match_tuples = re.findall(pattern, args)
    output = []
    for name, typ, default in match_tuples:
        d = {
                'name': name,
                'type': typ,
                'default': default,
                }
        output.append(d)

    return output

def parse_return(return_obj: str) -> str:
    """
    return_obj: ' -> list[str]'
    Return: some_data_type
    """
    if not return_obj:
        return ''
    pattern = r'^\s*([\w\[\]\(\)]+)\s*$'
    match = re.match(pattern, return_obj)
    if match:
        return (match.group(1) or '').strip()
    else:
        return ''

def parse_functions(filepath: str, target_functions: list[str]) -> list[dict]:
    """
    Return: [ {
                'name': function_name,
                'args': [{'name': arg_name, 'type': arg_type, 'default': arg_default}, ...],
                'return':,
                'line':
                }, ... ]
    """
    content = Path(filepath).read_text(encoding='utf-8')

    output = []
    pattern = fr'^\s*def\s+(\w+)\s*\((.*?)\)\s*(.*?)\s*:$'
    if target_functions:
        f_names = '|'.join(target_functions)
        pattern = fr'^\s*def\s+({f_names})\s*\((.*?)\)\s*(.*?)\s*:$'
    lines = content.splitlines()
    for ln, line in enumerate(lines, start=1):
        match = re.match(pattern, line)
        if match and match.group(1):
            d = {
                    'name': match.group(1),
                    'args': parse_args(match.group(2)),
                    'return': parse_return(match.group(3)),
                    'line': ln
                    }
            output.append(d)

    return output
