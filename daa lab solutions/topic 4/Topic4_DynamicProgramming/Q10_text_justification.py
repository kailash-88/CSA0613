def full_justify(words, maxWidth):
    result = []
    line = []
    line_len = 0
    for word in words:
        if line_len + len(line) + len(word) > maxWidth:
            spaces_needed = maxWidth - line_len
            if len(line) == 1:
                result.append(line[0] + ' ' * spaces_needed)
            else:
                gaps = len(line) - 1
                base, extra = divmod(spaces_needed, gaps)
                built = ""
                for i, w in enumerate(line[:-1]):
                    built += w + ' ' * (base + (1 if i < extra else 0))
                built += line[-1]
                result.append(built)
            line, line_len = [], 0
        line.append(word)
        line_len += len(word)
    last_line = ' '.join(line)
    last_line += ' ' * (maxWidth - len(last_line))
    result.append(last_line)
    return result

if __name__ == "__main__":
    words = ["This","is","an","example","of","text","justification."]
    for l in full_justify(words, 16):
        print(repr(l))
    words2 = ["What","must","be","acknowledgment","shall","be"]
    for l in full_justify(words2, 16):
        print(repr(l))
