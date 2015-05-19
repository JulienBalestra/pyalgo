from unittest import TestCase

from linked_list.linked_list import Link, LinkedList

from contextlib import contextmanager
from StringIO import StringIO
import sys


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestLinkedList(TestCase):
    def setUp(self):
        self.my_linked_list = LinkedList()

    def test_0_is_empty(self):
        self.assertTrue(self.my_linked_list.is_empty())

    def test_1_insert_start(self):
        self.my_linked_list.insert_start(10)
        self.assertFalse(self.my_linked_list.is_empty())
        self.assertEqual(10, self.my_linked_list.get_value(0))
        self.my_linked_list.insert_start(20)
        self.assertEqual(20, self.my_linked_list.get_value(0))
        self.assertEqual(10, self.my_linked_list.get_value(1))

    def test_2_insert_end(self):
        self.my_linked_list.insert_start(2)
        self.my_linked_list.insert_start(1)
        self.my_linked_list.insert_end(3)
        self.assertEqual(3, self.my_linked_list.get_value(2))

    def test_3_insert_index(self):
        self.my_linked_list.insert_start(10)
        self.my_linked_list.insert_end(30)
        self.my_linked_list.insert_index(20, 1)
        self.assertEqual(20, self.my_linked_list.get_value(1))

    def test_4_delete(self):
        self.my_linked_list.insert_start(10)
        self.my_linked_list.insert_start(20)
        self.my_linked_list.insert_start(30)
        self.my_linked_list.delete(1)
        self.assertEqual(30, self.my_linked_list.get_value(0))
        self.assertEqual(10, self.my_linked_list.get_value(1))
        self.assertFalse(self.my_linked_list.get_value(2))

    def test_5_get_value(self):
        self.assertFalse(self.my_linked_list.get_value(0))
        self.my_linked_list.insert_start(10)
        self.assertEqual(10, self.my_linked_list.get_value(0))

    def test_6_show(self):
        self.my_linked_list.insert_start(1)
        self.my_linked_list.insert_end(2)
        with captured_output() as (out, err):
            self.my_linked_list.show()
            self.assertEqual(out.getvalue().strip(), '1\n2')
            self.assertEqual(err.getvalue().strip(), "")