from pathlib import Path

def confirm_src(src: list[str]):
    if src == []:
        src.append('.')
    return src

def path2package(path: Path) -> str:
    """
    path: Path('aaa/bbb/ccc')

    Return: 'aaa.bbb.ccc'
    """
    return '.'.join(path.parts)

def confirm_package_module(src: list[str], package: list[str]) -> dict:
    assert src != []
    if package == []:
        for s in src:
            for pa in Path(s).rglob('*'):
                if pa.is_file() and (pa.suffix == '.py'):
                    # Only when p is a module file like *.py, then we can assume the package exists.
                    pa_rel_to_src = pa.relative_to(Path(s))
                    pack = pa.parent
                    package_name = path2package(path=pack)
                    module_name = pa.stem
    return (package, module)

def get_target_modules(src: list[str], package: list[str], module: list[str], debug=False) -> list[str]:
    """
    src: Relative src folder names to look for.
    package: Package names to look for.
    module: Module names to look for.

    Returns: [
        { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' },
        ... ]

    IMPORTANT ASSUMPTION: modules are assumed to exist as a *.py file.
    """
    src = confirm_src(src=src)
    assert src != []
    output_draft = []
    for s in src:
        for pa in Path(s).rglob('*'):
            if pa.is_file() and (pa.suffix == '.py'):
                # Only when p is a module file like *.py, then we can assume the package exists.
                pa_rel_to_src = pa.relative_to(Path(s))
                pack = pa_rel_to_src.parent
                scanned_package_name = path2package(path=pack)
                scanned_module_name = pa.stem
                d = { 'src': s, 'package': scanned_package_name, 'module': scanned_module_name }
                output_draft.append(d)
    output = []
    for d in output_draft:
        if debug:
            print(f"output_draft d: {d}")
        # d = { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' }
        if (package == []) or (d['package'] in package):
            if (module == []) or (d['module'] in module):
                output.append(d)

    return output
