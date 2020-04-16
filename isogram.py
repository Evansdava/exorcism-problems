"""
* Determine if a word or phrase is an isogram.
*
* An isogram (also known as a "nonpattern word") is a word or phrase without a
* repeating letter, however spaces and hyphens are allowed to appear multiple
* times.
*
* Examples of isograms:
*
*     lumberjacks
*     background
*     downstream
*     six-year-old
*
* The word isograms, however, is not an isogram, because the s repeats.
"""


def is_isogram(word):
    """Determine if a word is an isogram"""
    """
    Declare a set to hold letters
    For each letter in the string
        if it's in the set
            return false, it's a duplicate
        otherwise
            add it
    return true if the whole loop finishes
    """
    letters = set()

    for letter in word:
        if letter in letters and letter != '-' and letter != ' ':
            return False
        else:
            letters.add(letter)
    return True


if __name__ == '__main__':
    # Expected outputs: True, False
    good_test_cases = ["lumberjacks", "isograms"]

    # Expected outputs: Error, Error
    bad_test_cases = [55, None]

    # Expected outputs: True, True
    edge_cases = ["", "      "]

    print("Good test cases:")
    for case in good_test_cases:
        print(f"Testing '{case}'")
        print(is_isogram(case))

    print("\nBad test cases:")
    for case in bad_test_cases:
        print(f"Testing '{case}'")
        try:
            print(is_isogram(case))
        except TypeError:
            print("Error")

    print("\nEdge cases:")
    for case in edge_cases:
        print(f"Testing '{case}'")
        print(is_isogram(case))
