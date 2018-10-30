class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char   # stored as an integer - the ASCII character code value
        self.freq = freq   # the freqency associated with the node
        self.left = None   # Huffman tree (node) to the left
        self.right = None  # Huffman tree (node) to the right

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node

def comes_before(a, b):
    """Returns True if tree rooted at node a comes before tree rooted at node b, False otherwise"""
    if a.freq < b.freq:
        return True
    elif a.freq > b.freq:
        return False
    else:
        if a.char < b.char:
            return True
        return False

def combine(a, b):
    """Creates and returns a new Huffman node with children a and b, with the "lesser node" on the left
    The new node's frequency value will be the sum of the a and b frequencies
    The new node's char value will be the lesser of the a and b char ASCII values"""
    if a.char<b.char:
        nnchar = a.char
    else:
        nnchar = b.char
    leftnode = a
    rightnode = b
    newNode = HuffmanNode(nnchar, a.freq+b.freq)
    newNode.set_left(leftnode)
    newNode.set_right(rightnode)
    return newNode

def cnt_freq(filename):
    """Opens a text file with a given file name (passed as a string) and counts the 
    frequency of occurrences of all the characters within that file"""
    file = open(filename, 'r')
    frequency = [0]*256
    for line in file:
        for ch in line:
            frequency[ord(ch)] += 1
    file.close()
    return frequency

def create_huff_tree(char_freq):
    """Create a Huffman tree for characters with non-zero frequency
    Returns the root node of the Huffman tree"""
    node_list = []
    for i in range(len(char_freq)):
        newNode = HuffmanNode(i, char_freq[i])
        if char_freq[i] != 0:
            j = 0 
            while j < len(node_list) and comes_before(node_list[j], newNode):
                j +=1
            node_list.insert(j, newNode)
    if len(node_list) == 0:
        return None
    #for k in range(len(node_list)):
        #print(node_list[k].freq)
    
    while len(node_list) > 1:
        interNode = combine(node_list[0],node_list[1])
        del node_list[0]
        del node_list[0]
        k = 0
        while k < len(node_list) and comes_before(node_list[k], interNode):
            k +=1
        node_list.insert(k, interNode)
    return node_list[0]


def create_code(node):
    """Returns an array (Python list) of Huffman codes. For each character, use the integer ASCII representation 
    as the index into the arrary, with the resulting Huffman code for that character stored at that location"""
    return _create_code(node,'',['']*256)

def _create_code(node, huffcode, code_list):
    if node == None:
        return []
    if node.left != None and node.right != None:
        _create_code(node.left, huffcode + '0', code_list)
        _create_code(node.right, huffcode + '1', code_list)
    else:
        code_list[node.char] = huffcode
    return code_list

def create_header(freqs):
    """Input is the list of frequencies. Creates and returns a header for the output file
    Example: For the frequency list asscoaied with "aaabbbbcc, would return “97 3 98 4 99 2” """
    returnstring = ''
    for i in range(len(freqs)):
        if freqs[i] != 0:
            returnstring = returnstring + " " + str(i) + " "  + str(freqs[i])
    #print(returnstring[1:])
    return returnstring[1:]

def huffman_encode(in_file, out_file):
    """Takes inout file name and output file name as parameters
    Uses the Huffman coding process on the text from the input file and writes encoded text to output file
    Take note of special cases - empty file and file with only one unique character"""
    code_list = create_code(create_huff_tree(cnt_freq(in_file)))
    header = create_header(cnt_freq(in_file))

    with open(in_file, 'r') as INFILE, open(out_file, 'w') as OUTFILE:
        if header != '':
            OUTFILE.write(header + "\n")
        for line in INFILE:
            for ch in line:
                OUTFILE.write(code_list[ord(ch)])
