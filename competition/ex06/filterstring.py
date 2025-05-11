import sys

def filter_string(s, n):
    assert len(sys.argv) == 3 and isinstance(s, str) and isinstance(n, int), "the arguments are bad"
    words = [word for word in s.split() if all(c.isalnum() for c in word) and len(word) > n]
    filtered = list(map(lambda x: x, words))
    return filtered

if __name__ == "__main__":
    s = sys.argv[1]
    n = int(sys.argv[2])
    result = filter_string(s, n)
    print(result)