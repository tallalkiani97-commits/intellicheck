"""Small, dependency-free IntelliCheck demo."""
from difflib import SequenceMatcher
import re

def tokens(text):
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def compare(a, b):
    ta, tb = tokens(a), tokens(b)
    jaccard = len(ta & tb) / max(1, len(ta | tb))
    sequence = SequenceMatcher(None, a.lower(), b.lower()).ratio()
    return {"jaccard": round(jaccard * 100, 2), "sequence": round(sequence * 100, 2)}

if __name__ == "__main__":
    first = "Artificial intelligence helps students explore data and build useful systems."
    second = "Students use artificial intelligence to explore data and create useful systems."
    print("IntelliCheck demo")
    print(compare(first, second))
