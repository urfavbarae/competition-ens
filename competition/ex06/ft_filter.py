def ft_filter(function, element):
    if function is None:
        return (e for e in element)
    return (e for e in element if function(e))


def main():
    def evne(n):
        return n % 2 != 0

    numbers = [1,85,66,9,52,3]
    filtered = ft_filter(evne , numbers)

    print(list(filtered))
    
if __name__ == "__main__":
    main()

