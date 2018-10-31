import unittest
import filecmp
import subprocess
from huffman import *

class TestList(unittest.TestCase):
    def test_comes_before(self):
        a = HuffmanNode(97, 5)
        b = HuffmanNode(99, 2)
        self.assertFalse(comes_before(a,b))

    def test_cnt_freq(self):
        freqlist = cnt_freq("file2.txt")
        anslist = [2, 4, 8, 16, 0, 2, 0] 
        self.assertListEqual(freqlist[97:104], anslist)

    def test_cnt_freq1(self):
        freqlist = cnt_freq("single.txt")
        anslist = [93] 
        self.assertListEqual(freqlist[112:113], anslist)

    def test_cnt_freq2(self):
        freqlist = cnt_freq("empty.txt")
        anslist = [0]
        self.assertListEqual(freqlist[0:1], anslist)

    def test_create_huff_tree(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 32)
        self.assertEqual(hufftree.char, 97)
        left = hufftree.left
        self.assertEqual(left.freq, 16)
        self.assertEqual(left.char, 97)
        right = hufftree.right
        self.assertEqual(right.freq, 16)
        self.assertEqual(right.char, 100)

    def test_create_huff_tree1(self):
        freqlist = cnt_freq("single.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 93)
        self.assertEqual(hufftree.char, 112)

    def test_create_huff_tree2(self):
        freqlist = cnt_freq("multiline.txt")
        hufftree = create_huff_tree(freqlist)
        self.assertEqual(hufftree.freq, 56)
        self.assertEqual(hufftree.char, 10)
        left = hufftree.left
        self.assertEqual(left.freq, 24)
        self.assertEqual(left.char, 10)
        right = hufftree.right
        self.assertEqual(right.freq, 32)
        self.assertEqual(right.char, 32)
        
    def test_create_header(self):
        freqlist = cnt_freq("file2.txt")
        self.assertEqual(create_header(freqlist), "97 2 98 4 99 8 100 16 102 2")

    def test_create_header1(self):
        freqlist = cnt_freq("empty.txt")
        self.assertEqual(create_header(freqlist), "")

    def test_create_header2(self):
        freqlist = cnt_freq("declaration.txt")
        self.assertEqual(create_header(freqlist), "10 166 32 1225 38 1 39 1 44 109 45 3 46 36 49 1 52 1 54 1 55 2 58 10 59 10 65 22 66 7 67 19 68 5 69 3 70 17 71 15 72 24 73 8 74 5 75 1 76 15 77 3 78 8 79 6 80 23 82 9 83 23 84 15 85 3 87 13 97 466 98 88 99 171 100 253 101 875 102 169 103 116 104 331 105 451 106 12 107 13 108 216 109 144 110 487 111 518 112 116 113 6 114 420 115 460 116 640 117 211 118 74 119 84 120 9 121 82 122 4")

    def test_create_header3(self):
        freqlist = cnt_freq("single.txt")
        self.assertEqual(create_header(freqlist), "112 93")

    def test_create_header4(self):
        freqlist = cnt_freq("file3.txt")
        self.assertEqual(create_header(freqlist), "10 5 32 1 33 1 37 1 39 1 40 1 41 2 42 2 43 1 44 2 46 1 47 1 50 1 52 1 59 1 64 1 91 1 92 1 93 1 95 1 96 1 97 5 98 2 101 2 102 3 103 5 104 2 105 3 106 1 107 2 108 3 109 2 110 5 111 2 112 1 113 1 114 5 115 2 116 2 117 1 119 4 121 1 122 1 126 1")

    def test_create_code(self):
        freqlist = cnt_freq("file2.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('d')], '1')
        self.assertEqual(codes[ord('a')], '0000')
        self.assertEqual(codes[ord('f')], '0001')

    def test_create_code1(self):
        freqlist = cnt_freq("single.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('p')], '')

    def test_create_code2(self):
        freqlist = cnt_freq("file1.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord(' ')], '00')
        self.assertEqual(codes[ord('a')], '11')
        self.assertEqual(codes[ord('b')], '01')
        self.assertEqual(codes[ord('c')], '101')
        self.assertEqual(codes[ord('d')], '100')

    def test_create_code3(self):
        freqlist = cnt_freq("file3.txt")
        hufftree = create_huff_tree(freqlist)
        codes = create_code(hufftree)
        self.assertEqual(codes[ord('@')], '1111001')
        self.assertEqual(codes[ord('~')], '100001')
        self.assertEqual(codes[ord('.')], '1110100')
        self.assertEqual(codes[ord('%')], '1101010')
        self.assertEqual(codes[ord(' ')], '1101000')
        self.assertEqual(codes[ord('g')], '1001')

    def test_file_missing(self):
        self.assertRaises(FileNotFoundError, huffman_encode, "file1234.txt", "file1_134.txt")


  

if __name__ == '__main__': 
   unittest.main()
