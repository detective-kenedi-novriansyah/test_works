import unittest
import logging
import sys

from question.tests.test_question import TestsQuestion
from question.tests.tests_answer import TestsAnswer

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

if __name__ == "__main__":
    unittest.main()