from string import ascii_lowercase, ascii_uppercase


def capitalize(sentence: str) -> str:
    """
    This function will capitalize the first letter of a sentence or a word
    >>> capitalize("hello world")
    'Hello world'
    >>> capitalize("123 hello world")
    '123 hello world'
    >>> capitalize(" hello world")
    ' hello world'
    >>> capitalize("a")
    'A'
    >>> capitalize("")
    ''
    """
    if not sentence:
        return ""
    lower_to_upper = dict(zip(ascii_lowercase, ascii_uppercase))
    return lower_to_upper.get(sentence[0], sentence[0]) + sentence[1:]


if __name__ == "__main__":
    from doctest import testmod

    s1 = input("Enter a string:")
    print(capitalize(s1))
    testmod()
