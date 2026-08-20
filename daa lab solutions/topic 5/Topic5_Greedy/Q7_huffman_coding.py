import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman(characters, frequencies):
    heap = [Node(f, c) for c, f in zip(characters, frequencies)]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        heapq.heappush(heap, Node(a.freq + b.freq, None, a, b))
    return heap[0]

def get_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}
    if node.char is not None:
        codes[node.char] = prefix or "0"
        return codes
    get_codes(node.left, prefix + "0", codes)
    get_codes(node.right, prefix + "1", codes)
    return codes
# Note: Huffman codes are not unique -- any tree built by repeatedly merging
# the two lowest-frequency nodes is optimal (minimizes expected code length),
# even if the exact 0/1 assignment differs from another valid solution.

if __name__ == "__main__":
    root = build_huffman(['a','b','c','d'], [5,9,12,13])
    print(sorted(get_codes(root).items()))

    root2 = build_huffman(['f','e','d','c','b','a'], [5,9,12,13,16,45])
    print(sorted(get_codes(root2).items()))
