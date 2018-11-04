import unittest
import filecmp
import subprocess
from huffman import *
class TestList(unittest.TestCase):
    def test_01_textfile(self):
        huffman_encode("file1.txt", "file1_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file1_out.txt file1_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_02_textfile(self):
        huffman_encode("declaration.txt", "declaration_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb declaration_out.txt declaration_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_03_textfile(self):
        huffman_encode("multiline.txt", "multiline_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb multiline_out.txt multiline_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_04_textfile(self):
        huffman_encode("empty.txt", "empty_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb empty_out.txt empty_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_05_textfile(self):
        huffman_encode("single.txt", "single_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb single_out.txt single_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_06_textfile(self):
        huffman_encode("file2.txt", "file2_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file2_out.txt file2_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_07_textfile(self):
        huffman_encode("file3.txt", "file3_out.txt")
        # capture errors by running 'diff' on your encoded file with a *known* solution file
        err = subprocess.call("diff -wb file3_out.txt file3_soln.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_1(self):
        huffman_decode("file1_soln.txt","file1_decode.txt")
        err = subprocess.call("diff -wb file1.txt file1_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_2(self):
        huffman_decode("file2_soln.txt","file2_decode.txt")
        err = subprocess.call("diff -wb file2.txt file2_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_3(self):
        huffman_decode("file3_soln.txt","file3_decode.txt")
        err = subprocess.call("diff -wb file3.txt file3_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_4(self):
        huffman_decode("empty.txt","empty_decode.txt")
        err = subprocess.call("diff -wb empty.txt empty_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_5(self):
        huffman_decode("single_soln.txt","single_decode.txt")
        err = subprocess.call("diff -wb single.txt single_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_6(self):
        huffman_decode("multiline_soln.txt","multiline_decode.txt")
        err = subprocess.call("diff -wb multiline.txt multiline_decode.txt", shell = True)
        self.assertEqual(err, 0)

    def test_decode_7(self):
        huffman_decode("declaration_soln.txt","declaration_decode.txt")
        err = subprocess.call("diff -wb declaration.txt declaration_decode.txt", shell = True)
        self.assertEqual(err, 0)


if __name__ == '__main__': 
   unittest.main()
