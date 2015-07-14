

class Grades(object):
	def __init__(self, *args):
		self.grades = [grade for grade in args]
		
	@property
	def average(self):
		if len(self.grades):
			return sum(self.grades) / len(self.grades)
		else:
			return 0

	@property
	def last_grade(self):
		if len(self.grades):
			return self.grades[-1]
		else:
			return None
	
	@last_grade.setter
	def last_grade(self, grade):
		self.grades.append(grade)
		
	@last_grade.deleter
	def last_grade(self):
		self.grades.pop()