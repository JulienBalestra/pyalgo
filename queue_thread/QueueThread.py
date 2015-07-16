import threading
import Queue


class QueueThread(threading.Thread):
	q = Queue.Queue()

	def __init__(self, name, function):
		threading.Thread.__init__(self, name=name)
		self.kill = False
		self.todo = function(self)

	def run(self):
		self.q.put(self)
		self.todo()
		self.q.task_done()