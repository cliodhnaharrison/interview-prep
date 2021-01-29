from collections import defaultdict
import re

def most_common_word(paragraph, banned):

    freq = defaultdict(int)

    paragraph = re.findall(r"[\w]+", paragraph.lower())

    print (paragraph)

    for word in paragraph:
        if word not in banned:
            freq[word] += 1

    return max(freq, key=freq.get)
