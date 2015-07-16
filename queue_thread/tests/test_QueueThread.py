import unittest
from time import sleep

from queue_thread import QueueThread

BUFFER = []


def create_function(thread):
	def function():
		for i in range(0, 5):
			if thread.kill is True:
				BUFFER.append("K %s" % thread.getName())
				break

			BUFFER.append("%i %s" % (i, thread.getName()))
			sleep(0.25)

	return function


class TestQueueThread(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.t1 = QueueThread.QueueThread("t1", create_function)
		cls.t2 = QueueThread.QueueThread("t2", create_function)

	def test_00(self):
		self.assertFalse(self.t1.isAlive())
		self.assertFalse(self.t2.isAlive())
		self.assertEqual([], BUFFER)

	def test_01(self):
		self.t1.start()
		self.assertTrue(self.t1.isAlive())
		self.t2.start()
		self.assertTrue(self.t2.isAlive())
		self.assertNotEqual([], BUFFER)

	def test_02(self):
		self.t1.kill = True
		sleep(0.5)
		self.assertFalse(self.t1.isAlive())
		self.assertTrue(self.t2.isAlive())
		self.assertNotEqual([], BUFFER)

	def test_03(self):
		self.t1.q.join()
		self.assertEqual(
			['0 t1', '0 t2', 'K t1', '1 t2', '2 t2', '3 t2', '4 t2'],
			BUFFER)