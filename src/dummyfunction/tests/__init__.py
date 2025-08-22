import unittest

__all__ = ["test"]


def test() -> unittest.TextTestResult:
    "This function runs all the tests."
    loader: unittest.TestLoader = unittest.TestLoader()
    tests: unittest.TestSuite = loader.discover(start_dir="dummyfunction.tests")
    runner: unittest.TextTestRunner = unittest.TextTestRunner()
    result: unittest.TextTestResult = runner.run(tests)
    return result
