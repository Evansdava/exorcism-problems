"""
* Implement run-length encoding and decoding.
*
* Run-length encoding (RLE) is a simple form of data compression, where runs
* (consecutive data elements) are replaced by just one data value and count.
*
* For example we can represent the original 53 characters with only 13.
*
* "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
*
* RLE allows the original data to be perfectly reconstructed from the
* compressed
* data, which makes it a lossless data compression.
*
* "AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
*
* For simplicity, you can assume that the unencoded string will only contain
* the letters A through Z (either lower or upper case) and whitespace. This way
* data to be encoded will never contain any numbers and numbers inside data to
* be decoded always represent the count for the following character.
"""


def rl_encode(string):
    """Encode a string of data with RLE"""
    """
    for each character in the string
        count the number of times it stays the same after iterating
        on a new character, add the count and char to a result list
    return the result list concatenated to a string
    """
    result = []
    count = 1
    i = 1
    curr_letter = string[0]
    while i < len(string):
        if string[i] == curr_letter:
            count += 1

        if (i == len(string) - 1) or (string[i] != curr_letter):
            if count > 1:
                result.append(f"{count}{curr_letter}")
            else:
                result.append(f'{curr_letter}')
            curr_letter = string[i]
            count = 1
        i += 1

    return "".join(result)


def rl_decode(string: str):
    """Decode a string of RLE data"""
    """
    Split the string into substrings based on letters/whitespace
    For each substring
        Remove the last character
        Convert the rest to an int
        Add the character to a result string <int> times
    return result string
    """
    sub_start_index = 0
    i = 0
    substrings = []
    while i < len(string):
        if string[i].isalpha() or string[i].isspace():
            substrings.append(string[sub_start_index:i + 1])
            sub_start_index = i + 1
        i += 1

    result = ""
    for substring in substrings:
        num, char = substring[0:-1], substring[-1]
        if num == '':
            num = 1
        for _ in range(int(num)):
            result += char

    return result


if __name__ == '__main__':
    # Expected output: '2AB3CD4E', '13A'
    good_test_cases = ['AABCCCDEEEE', 'AAAAAAAAAAAAA']

    # Expected output: Error, ""
    bad_test_cases = [500, "39194444"]

    # Expected output: '2a2A2a3A', 'A w2e2 li2tle lad'
    edge_cases = ['aaAAaaAAA', 'A  wee  little lad']

    print("Good test cases:")
    for case in good_test_cases:
        print(f"Testing '{case}'")
        encoded = rl_encode(case)
        print(f'Encoded: \'{encoded}\'')
        print(f'Decoded: \'{rl_decode(encoded)}\'')

    print("\nBad test cases:")
    for case in bad_test_cases:
        print(f"Testing '{case}'")
        try:
            encoded = rl_encode(case)
            print(f'Encoded: \'{encoded}\'')
            print(f'Decoded: \'{rl_decode(encoded)}\'')
        except TypeError:
            print("Error")

    print("\nEdge cases:")
    for case in edge_cases:
        print(f"Testing '{case}'")
        encoded = rl_encode(case)
        print(f'Encoded: \'{encoded}\'')
        print(f'Decoded: \'{rl_decode(encoded)}\'')
