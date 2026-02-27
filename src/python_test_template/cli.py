#!/usr/bin/env python3
import argparse

import logging

logging.basicConfig(
    level=logging.DEBUG,      # Minimum level to capture
    format="%(asctime)s [%(levelname)s] %(message)s",
)

from . import parse_paths
from . import template_writer

def main():
    # Define possible arguments
    parser = argparse.ArgumentParser(description="Writing functions are fun, writing test files for those functions are boring. This helps that.")
    parser.add_argument("--dest", default='tests', help="Destination subfolder where test_*.py files will be stored. Default is 'tests'.")
    parser.add_argument("--src", action='append', type=str, default=[], help="src paths. Example: src/folder/path")
    parser.add_argument("--package", action='append', type=str, default=[], help="To isolate the process to specific package names. Example: package.name")
    parser.add_argument("--module", action='append', type=str, default=[], help="To isolate the process to specific module names. Example: module_name")
    parser.add_argument("--function", action='append', type=str, default=[], help="To isolate the process to specific function names.")
    # Debug
    parser.add_argument("--debug", action="store_true", help="DEBUG MODE")

    args = parser.parse_args()

    debug = args.debug

    """
    target_modules = [
        { 'src': 'src/path', 'package': 'package.name', 'module': 'module_name' },
        ... ]
    """
    target_modules = parse_paths.get_target_modules(src=args.src, package=args.package, module=args.module, debug=debug)
    if debug:
        print(f"target_modules: {target_modules}")
    template_writer.generate_template(target_modules=target_modules, target_functions=args.function, target_dest=args.dest, debug=debug)


if __name__ == "__main__":
    main()
