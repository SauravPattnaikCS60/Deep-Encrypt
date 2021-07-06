import heapq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.right = None
        self.left = None

    def __eq__(self, other):
        return self.freq == other.freq

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}
        self.reverse = {}

    def count_frequency(self, text):
        frequency = {}

        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def make_heap(self, frequency):
        for key in frequency.keys():
            node = Node(key, frequency[key])
            heapq.heappush(self.heap, node)

    def merge(self):
        while len(self.heap) > 1:
            left = heapq.heappop(self.heap)
            right = heapq.heappop(self.heap)
            new_node = Node(char=None, freq=left.freq + right.freq)
            new_node.left = left
            new_node.right = right
            heapq.heappush(self.heap, new_node)

    def make_codes(self, root, cur):
        if root is None:
            return

        if root.char is not None:
            self.codes[root.char] = cur
            self.reverse[cur] = root.char
            return
        self.make_codes(root.left, cur+"0")
        self.make_codes(root.right, cur + "1")

    def startcodes(self):
        root = heapq.heappop(self.heap)
        self.make_codes(root, "")

    def encoded(self, text):
        encoded_text = ""
        for char in text:
            encoded_text += self.codes[char]
        return encoded_text

    def compress(self, text):
        frequency = self.count_frequency(text)
        self.make_heap(frequency)
        self.merge()
        self.startcodes()
        encoded = self.encoded(text)
        return encoded

    def print_codes(self):
        for key in self.codes.keys():
            print(key + "\t" + self.codes[key])

    def decode(self, encoded, reverse):
        decode_text = ""
        temp = ""
        for char in encoded:
            temp += char
            if temp in reverse:
                decode_text += reverse[temp]
                temp = ""

        return decode_text

    def return_reverse(self):
        return self.reverse


# huff = HuffmanCoding('file.txt')
# val = huff.compress()
# print(huff.print_codes())
# print(val)
# print(huff.decode(val))
