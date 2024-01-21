import unittest
from raptor import *


class Test(unittest.TestCase):
    def test_raptor_invalid_exam_format(self):
        """
        Проверка раптора на умение работы с форматом билетов.
        Поскольку раптор использует модуль random, тестируются только ожибки (не все).
        """
        self.assertRaises(InvalidExamFormatError, GenerateBills, "cd-1000")
        self.assertRaises(InvalidExamFormatError, GenerateBills,
                          "what_the_hell_am_i_doing_at_2_am-1000")
        self.assertRaises(InvalidExamFormatError, GenerateBills, "ab-2 ab-1")

    def test_raptor_boring_exam_error(self):
        """
        Проверка чуйки раптора на скучный экзамен.
        Поскольку раптор использует модуль random, тестируются только ожибки (не все).
        """
        self.assertRaises(BoringExamError, GenerateBills, "cd-3")
        self.assertRaises(BoringExamError, GenerateBills, "cd-0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
