__all__: list[str] = ["dummyfunction", "main", "parse_args", "run"]

import sys

from dummyfunction.core import dummyfunction, main, parse_args, run

if __name__ == "__main__":
    sys.exit(main())
