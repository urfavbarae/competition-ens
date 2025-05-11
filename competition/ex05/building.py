import sys
import string

def nb_characters(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    total = len(text)

    print(f"le text contient {total} characters:, {upper} upper letters,{lower} lower letters ,{punct} punctuation,{spaces} spaces,{digits} digits")


def main():
    args = sys.argv[1:]

    if len(args) == 0:
        text = input("Entrer un text: ")
    elif len(args) > 1:
        raise AssertionError("un et un seul text en argument")
    else:
        text = args[0]
    nb_characters(text)

if __name__ == "__main__":
    main()

# to test run 
# python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."