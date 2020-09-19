from unittest import TestCase

from main import HuffmanTree, Tree, PriorityQueue


class TestHuffmanTree(TestCase):
    def test_create_letter_map_empty_sentence(self):
        self.assertEqual(HuffmanTree().create_letter_map(""), {})

    def test_create_letter_map(self):
        sentence = "ddddbbaccc"
        expected = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

        self.assertEqual(HuffmanTree().create_letter_map(sentence), expected)

    def test_create_letter_map2(self):
        sentence = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff"
        expected = {'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45, 'a': 5}

        self.assertEqual(HuffmanTree().create_letter_map(sentence), expected)

    def test_create_tree_list_empty(self):
        self.assertEqual(HuffmanTree().create_tree_list({}), [])

    def test_create_tree_list_2_elements(self):
        expected = [Tree('a', 1), Tree('b', 2)]
        actual = HuffmanTree().create_tree_list({'a': 1, 'b': 2})

        self.assertEqual(actual, expected)

    def test_create_tree_list_5_elements_out_of_order(self):
        expected = [Tree('b', 9), Tree('c', 12), Tree('d', 13), Tree('e', 16), Tree('f', 45), Tree('a', 5)]
        actual = HuffmanTree().create_tree_list({'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45, 'a': 5})

        self.assertEqual(actual, expected)

    def test_huffman_tree_empty_sentence(self):
        self.assertEqual(HuffmanTree().huffman_tree, PriorityQueue())

    def test_huffman_tree_1_letter_sentence(self):
        expected = PriorityQueue([Tree('a', 1)])
        self.assertEqual(HuffmanTree("a").huffman_tree, expected)

    def test_huffman_tree_app_sentence(self):
        left = Tree('a', 1)
        right = Tree('p', 2)
        tree = Tree('', 3, left, right)
        expected = PriorityQueue([tree])

        self.assertEqual(HuffmanTree("app").huffman_tree, expected)
