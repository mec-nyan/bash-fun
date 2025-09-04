#!/usr/bin/env python3
'''test_mkproject.py'''

import unittest
from mkproject import ansify


class TestFunc(unittest.TestCase):

    def test_ansify(self):
        for style in range(9):
            for colour in range(30, 40):
                want = f"[{style};{colour}m"
                got = ansify([style, colour])

                self.assertEqual(want, got)


if __name__ == "__main__":
    unittest.main()
