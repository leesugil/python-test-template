
from python_test_template import parse_paths

def test_confirm_src():
    cases = [
                {
                'args': {
                    #src: list[str]
                    },
                #
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_paths.confirm_src(case['args']) == case['expected']

def test_path2package():
    cases = [
                {
                'args': {
                    #path: Path
                    },
                #str
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_paths.path2package(case['args']) == case['expected']

def test_confirm_package_module():
    cases = [
                {
                'args': {
                    #src: list[str], package: list[str]
                    },
                #dict
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_paths.confirm_package_module(case['args']) == case['expected']

def test_get_target_modules():
    cases = [
                {
                'args': {
                    #src: list[str], package: list[str], module: list[str], debug=False
                    },
                #list[str]
                'expected': ,
                },
            ]

    for case in cases:
        assert parse_paths.get_target_modules(case['args']) == case['expected']

