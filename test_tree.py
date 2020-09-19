from unittest import TestCase

from main import Tree


class TestTree(TestCase):
    def test_with_default_values(self):
        tree = Tree('a', 3)
        self.assertEqual(tree.letter, 'a')
        self.assertEqual(tree.frequency, 3)
        self.assertEqual(tree.left, None)
        self.assertEqual(tree.right, None)

    def test_with_all_values(self):
        left = Tree('a', 3)
        right = Tree('b', 2)

        tree = Tree('', 5, left=left, right=right)

        self.assertEqual(tree.frequency, 5)
        self.assertEqual(tree.left.letter, 'a')
        self.assertEqual(tree.right.letter, 'b')
