import sys

def filter_string(s, n):
    assert len(sys.argv) == 3 and isinstance(s, str) and isinstance(n, int), "bad arugments"
    words = [word for word in s.split() if word.isalnum() and len(word) > n]
    return words

if __name__ == "__main__":
    s = sys.argv[1]
    n = int(sys.argv[2])
    result = filter_string(s, n)
    print(result)