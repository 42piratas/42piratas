import unittest
from cdd_data_grabber import connects_cdd_local


class TestConnectsCddLocal(unittest.TestCase):
    def test_inexisting_files(self):
        self.assertEqual(connects_cdd_local("fake/fake/inexisting.csv"),
                         "COULD NOT FIND THE FILE!")


if __name__ == "__main__":
    unittest.main()
