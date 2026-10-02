import unittest
from analyzer import analyze

class Cases(unittest.TestCase):
    def test_security_behavior(self):
        self.assertEqual(analyze({"resources":[{"id":"x","encrypted":True}]}), [])
        self.assertEqual(analyze({"resources":[{"id":"x"}]})[0]["severity"], "UNKNOWN")
        self.assertEqual(analyze({"keys":[{"id":"x","rotation_supported":False,"rotation_enabled":False}]}), [])

if __name__ == "__main__":
    unittest.main()

