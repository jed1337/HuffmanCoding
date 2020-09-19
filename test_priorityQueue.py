from unittest import TestCase

from main import PriorityQueue, Tree


class TestPriorityQueue(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.priorityQueue = PriorityQueue()

    def test_get(self):
        self.assertEqual(self.priorityQueue.all_elements(), [])

    def test_insert_single_element(self):
        self.priorityQueue.insert(self.tree(3))
        self.assertEqual(self.priorityQueue.all_elements(), self.tree_list([3]))

    def test_length_new_queue(self):
        self.assertEqual(len(self.priorityQueue), 0)

    def test_length_queue_with_one_element(self):
        self.priorityQueue.insert(self.tree(5))
        self.assertEqual(len(self.priorityQueue), 1)

    def test_sort_elements_upon_insert(self):
        self.priorityQueue.insert(self.tree(5))
        self.priorityQueue.insert(self.tree(2))
        self.assertEqual(self.priorityQueue.all_elements(), self.tree_list([2, 5]))

    def test_dequeue(self):
        self.priorityQueue.insert(self.tree(5))
        self.assertEqual(self.priorityQueue.dequeue(), self.tree(5))
        self.assertEqual(self.priorityQueue.all_elements(), [])

    def test_dequeue_multiple_elements(self):
        self.priorityQueue.insert(self.tree(5))
        self.priorityQueue.insert(self.tree(2))
        self.priorityQueue.insert(self.tree(10))

        self.assertEqual(self.priorityQueue.dequeue(), self.tree(2))
        self.assertEqual(self.priorityQueue.all_elements(), self.tree_list([5, 10]))
        self.assertEqual(self.priorityQueue.dequeue(), self.tree(5))
        self.assertEqual(self.priorityQueue.all_elements(), self.tree_list([10]))
        self.assertEqual(self.priorityQueue.dequeue(), self.tree(10))
        self.assertEqual(self.priorityQueue.all_elements(), self.tree_list([]))

    def test_queue_with_initial_elements(self):
        pq = PriorityQueue([1, 2, 3])
        self.assertEqual(pq.all_elements(), [1, 2, 3])

    def tree(self, value):
        return Tree('', value)

    def tree_list(self, values):
        return list(map(lambda v: Tree('', v), values))
