import unittest

from hash_table import HashTable
from nltk.corpus import gutenberg  # any excuse to use the NLTK!


class TestHashTable(unittest.TestCase):

    def setUp(self):
        self.TABLE = HashTable()
        self.ALICE = list(set(gutenberg.words('carroll-alice.txt')))[:400]

    def test_hash(self):
        self.assertEqual(self.TABLE.hash('Alice in Wonderland, circa 1865'), 5)
        with self.assertRaises(TypeError):
            self.TABLE.hash(1234)

        # HashTable accurately handles whatever number of containers specified:
        TABLE2 = HashTable(100)
        self.assertEqual(TABLE2.hash('Alice in Wonderland, circa 1865'), 29)

    def test_set(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
            bucket = self.TABLE.head
            for num in range(self.TABLE.hash(word)):
                bucket = bucket.next
            self.assertIsNotNone(bucket.value.search((word, word)))
        with self.assertRaises(TypeError):
            self.TABLE.set(4, 4)

    def test_get(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
            value = self.TABLE.get(word)
            self.assertEqual(value, word)
        with self.assertRaises(TypeError):
            self.TABLE.get(4)
        with self.assertRaises(KeyError):
            self.TABLE.get('Curiouser and curiouser!')

    def test_resetting_and_getting_new_values(self):
        for word in self.ALICE:
            self.TABLE.set(word, word)
        container = self.TABLE.head
        for num in range(self.TABLE.hash('Alice')):
            container = container.next
        self.assertIn(str(('ALICE', 'ALICE')), str(container.value))
        self.TABLE.set('ALICE', 'Down the Rabit-Hole')
        self.assertEqual(self.TABLE.get('ALICE'), 'Down the Rabit-Hole')
        self.assertNotIn(str(('ALICE', 'ALICE')), str(container.value))

if __name__ == '__main__':
    unittest.main()
