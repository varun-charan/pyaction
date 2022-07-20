"""
Entrypoint module, in case you use `python -mmfs`.


Why does this file exist, and why __main__? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/2/using/cmdline.html#cmdoption-m
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""
import sys

from devops.cli import cli

if __name__ == "__main__":
    # https://click.palletsprojects.com/en/7.x/commands/#nested-handling-and-contexts
    sys.exit(cli(obj={}))
