from __future__ import print_function
import sys
from safety.cli import check


def main(argv):
    try:
        check.main(['--full-report'] + argv[:-1])
        return 0
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
