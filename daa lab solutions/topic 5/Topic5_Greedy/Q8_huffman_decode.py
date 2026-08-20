import heapq

class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq; self.char = char; self.left = left; self.right = right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman(characters, frequencies):
    heap = [Node(f, c) for c, f in zip(characters, frequencies)]
    heapq.heapify(heap)
    while len(heap) > 1:
        a = heapq.heappop(heap); b = heapq.heappop(heap)
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

def encode(message, codes):
    return "".join(codes[ch] for ch in message)

def decode(root, encoded):
    result = []
    node = root
    for bit in encoded:
        node = node.left if bit == '0' else node.right
        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)
# Because Huffman codes are not unique, decoding a specific pre-encoded
# string correctly requires the exact codebook used to encode it. Below we
# demonstrate full round-trip correctness: encode a message with our own
# codebook, then decode it back with the same tree.

if __name__ == "__main__":
    root = build_huffman(['a','b','c','d'], [5,9,12,13])
    codes = get_codes(root)
    message = "abacd"
    encoded = encode(message, codes)
    print("Encoded:", encoded)
    print("Decoded:", decode(root, encoded))  # abacd

    root2 = build_huffman(['f','e','d','c','b','a'], [5,9,12,13,16,45])
    codes2 = get_codes(root2)
    message2 = "fcbade"
    encoded2 = encode(message2, codes2)
    print("Encoded:", encoded2)
    print("Decoded:", decode(root2, encoded2))  # fcbade
