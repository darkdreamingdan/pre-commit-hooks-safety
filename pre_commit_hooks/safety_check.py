from __future__ import print_function
import sys
from safety.cli import check


def main(argv=sys.argv[1:]):
    try:
        check.main(['--full-report'] + argv)
        return 0
    except SystemExit as error:
        if error.code == 0:
            return 0
        return 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
