import unittest
import os
from myFunctions import read_file

class ReadFileTest(unittest.TestCase):
    def test_read_file_with_content(self):
        # Goal: Test if the function correctly reads the content from a file

        # Test Methodology:
        # 1. Create a temporary file with some content
        # 2. Call the function and store the returned result
        # 3. Assert that the returned result matches the expected content
        # 4. Clean up the temporary file

        file_path = 'test_file.txt'
        content = 'Hello, World!'
        with open(file_path, 'w') as f:
            f.write(content)

        result = read_file(file_path)

        self.assertEqual(result, content)

        os.remove(file_path)

    def test_read_file_with_empty_file(self):
        # Goal: Test if the function correctly handles an empty file

        # Test Methodology:
        # 1. Create a temporary empty file
        # 2. Call the function and store the returned result
        # 3. Assert that the returned result is an empty string
        # 4. Clean up the temporary file

        file_path = 'empty_file.txt'
        open(file_path, 'w').close()

        result = read_file(file_path)

        self.assertEqual(result, '')

        os.remove(file_path)

    def test_read_file_with_nonexistent_file(self):
        # Goal: Test if the function correctly handles a non-existent file path

        # Test Methodology:
        # 1. Call the function with a non-existent file path
        # 2. Assert that the function raises either FileNotFoundError or IOError
        file_path = 'non_existent_file.txt'
        with self.assertRaises((FileNotFoundError, IOError)):
            read_file(file_path)


if __name__ == '__main__':
    unittest.main()

