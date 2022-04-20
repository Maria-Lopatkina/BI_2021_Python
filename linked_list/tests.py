import unittest
from linked_list import LinkedList


class Test(unittest.TestCase):
    def test_add(self):
        obj = LinkedList()
        with self.assertRaises(IndexError):
            obj.add(30, 100)
        obj.add(10)
        self.assertEqual(obj._last_added_value, 10)
        obj.add(20, 0)
        self.assertEqual(obj._last_added_value, 20)
        with self.assertRaises(IndexError):
            obj.add(30, 100)

    def test_add_all(self):
        obj = LinkedList()
        test_list = [1, 2, 3]
        obj.add_all(test_list)
        self.assertEqual(obj._last_added_value, 3)

    def test_pop(self):
        obj = LinkedList()
        obj.add(1)
        obj.add(2)
        obj.add(3)
        self.assertEqual(obj.pop(), 3)
        self.assertEqual(obj.pop(0), 1)
        with self.assertRaises(IndexError):
            obj.pop(100)

    def test_in(self):
        obj = LinkedList()
        obj.add(10)
        obj.add(20, 1)
        self.assertTrue(10 in obj)
        self.assertFalse(100 in obj)

    def test_remove_last_occurrence(self):
        obj = LinkedList()
        obj.add(1)
        obj.add_all([1, 2, 3, 1, 1, 5])
        obj.remove_last_occurrence(1)
        obj_list = []
        for el in range(6):
            obj_list.append(obj[el])
        self.assertEqual(obj_list, [1, 1, 2, 3, 1, 5])

    def test_first(self):
        obj = LinkedList()
        obj.add(100)
        obj.add(200)
        obj.add(300)
        self.assertEqual(obj.first(), 100)

    def test_last(self):
        obj = LinkedList()
        obj.add(100)
        obj.add(200)
        obj.add(300)
        self.assertEqual(obj.last(), 300)


if __name__ == '__main__':
    unittest.main()
