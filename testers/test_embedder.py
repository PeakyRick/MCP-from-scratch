import os
import sys
sys.path.append(os.getcwd())
import unittest
from Embedder import get_embedder

class TestEmbedder(unittest.TestCase):
    def setUp(self):
        self.embedder = get_embedder()
        self.test_query = "What is the capital of France?"
        self.query_vector = self.embedder.embed_query(self.test_query)

    def test_vector_size(self):
        """Test that the embedding vector has the correct size of 1536"""
        self.assertEqual(len(self.query_vector), 1536, "Embedding vector should have size 1536")

    def test_vector_type(self):
        """Test that the 10th element of the embedding vector is a float"""
        self.assertIsInstance(self.query_vector[10], float, "10th element should be a float")

    def test_print_vector(self):
        """Test that we can print the query vector"""
        # Print first 5 elements to keep output manageable
        print("\nFirst 50 elements of query vector:")
        print(self.query_vector[:50])
        # Verify we can print without errors
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
