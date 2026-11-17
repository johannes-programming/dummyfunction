__all__: list[str] = ["main"]

import sys

from dummyfunction.tests import test


def main() -> int:
    return int(not test().wasSuccessful())


if __name__ == "__main__":
    sys.exit(main())
