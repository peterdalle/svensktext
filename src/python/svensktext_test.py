import unittest
from svensktext import SvenskText


class RunTest(unittest.TestCase):

    def test_jobs(self):
        # all genders
        for job in SvenskText.jobs():
            gender = job[1]
            self.assertIn(gender, ["unknown", "male", "female"])
        # males
        for job in SvenskText.jobs(gender="male"):
            gender = job[1]
            self.assertEqual(gender, "male")
        # females
        for job in SvenskText.jobs(gender="female"):
            gender = job[1]
            self.assertEqual(gender, "female")
        # incorrect input parameter
        self.assertRaises(ValueError, SvenskText.jobs, gender="WRONG INPUT VALUE")

    def test_names(self):
        # all genders
        for name in SvenskText.first_names():
            gender = name[1]
            self.assertIn(gender, ["unknown", "male", "female"])
        # males
        for name in SvenskText.first_names(gender="male"):
            gender = name[1]
            self.assertEqual(gender, "male")
        # females
        for name in SvenskText.jobs(gender="female"):
            gender = name[1]
            self.assertEqual(gender, "female")
        # incorrect input parameter
        self.assertRaises(ValueError, SvenskText.first_names, gender="WRONG INPUT VALUE")

    def test_print_summary(self):
        SvenskText.print_summary()


if __name__ == '__main__':
    unittest.main()
