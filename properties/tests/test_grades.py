import unittest

from properties import grades


class TestGrades(unittest.TestCase):
	def test_00(self):
		classroom = grades.Grades(8, 12)
		self.assertEqual(10, classroom.average)
		
	def test_01(self):
		classroom = grades.Grades(8, 12)
		classroom.last_grade = 20
		self.assertEqual(20, classroom.last_grade)
		self.assertEqual(13, classroom.average)		
		
	def test_02(self):
		classroom = grades.Grades(8, 12)
		classroom.last_grade = 20
		self.assertEqual(20, classroom.last_grade)
		self.assertEqual(13, classroom.average)
		del classroom.last_grade
		self.assertEqual(10, classroom.average)