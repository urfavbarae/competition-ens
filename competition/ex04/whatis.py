import sys

def is_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    if len(sys.argv) != 2:
        raise AssertionError("Exactly one argument is required")
    try:
        num = int(sys.argv[1])
    except ValueError:
        raise AssertionError("Argument must be an integer")
    
    result = is_odd_or_even(num)
    print(result)

if __name__ == "__main__":
    main()

#to test run 
#python whatis.py 2