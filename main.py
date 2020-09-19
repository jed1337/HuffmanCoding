from collections import defaultdict
from functools import cmp_to_key


class PriorityQueue():
    def __init__(self, queue=None):
        if queue is None:
            self.queue = []
        else:
            self.queue = queue

    def __len__(self):
        return len(self.queue)

    def all_elements(self):
        return self.queue

    def insert(self, value):
        self.queue.append(value)
        compare = cmp_to_key(lambda t1, t2: t1.frequency - t2.frequency)

        self.queue = sorted(self.queue, key=compare)

    def dequeue(self):
        return self.queue.pop(0)

    def __eq__(self, other):
        if isinstance(other, PriorityQueue):
            return self.queue == other.queue
        return False

    def __ne__(self, other):
        return not self.__eq__(other)


class Tree():
    def __init__(self, letter, frequency, left=None, right=None):
        self.letter = letter
        self.frequency = frequency
        self.left = left
        self.right = right

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Tree):
            return self.letter == other.letter \
                   and self.frequency == other.frequency \
                   and self.left == other.left \
                   and self.right == other.right
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "{}:{}, left:({}), right:({})".format(self.letter, self.frequency, self.left, self.right)


class HuffmanTree():
    def __init__(self, sentence=""):
        letter_map = self.create_letter_map(sentence)
        tree_list = self.create_tree_list(letter_map)

        self.huffman_tree = PriorityQueue(tree_list)
        while len(self.huffman_tree) > 1:
            left = self.huffman_tree.dequeue()
            right = self.huffman_tree.dequeue()

            tree = Tree('', left.frequency + right.frequency, left=left, right=right)
            self.huffman_tree.insert(tree)

    @staticmethod
    def create_letter_map(sentence):
        letter_map = defaultdict(lambda: 0)
        for letter in sentence:
            letter_map[letter] += 1

        return letter_map

    @staticmethod
    def create_tree_list(letter_map):
        tree_list = []
        for k, v in letter_map.items():
            tree_list.append(Tree(k, v))

        return tree_list


if __name__ == '__main__':
    sentence = "aaaaabbbbbbbbbccccccccccccdddddddddddddeeeeeeeeeeeeeeeefffffffffffffffffffffffffffffffffffffffffffff"
    main = HuffmanTree(sentence)
