# concatenate the string along with their frequencies 
# when the previous character is different from the current one


def string_compression(s):

    compressed_string ="" 
    count_consecutive=0

    for i in range(len(s)):

        # increment the counter for any character encountered.
        count_consecutive+=1

        # if index exceeds of equates string length;
        # next character is different from the current one
        if(i+1>=len(s) or (s[i+1]!=s[i])):
            compressed_string+=s[i]+str(count_consecutive)
            count_consecutive=0
    
    # if len(compressed_string) <len(s):
    #     return compressed_string
    
    # return s

    result=compressed_string if len(compressed_string) < len(s) else s
    return result


def main():
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),    # compression helps
        ("abcdef", "abcdef"),            # no compression (a1b1c1d1e1f1 is longer)
        ("aabbcc", "aabbcc"),            # no compression (a2b2c2 same length)
        ("aaaa", "a4"),                  # compression helps
        ("a", "a"),                      # single char
        ("", ""),                        # empty string
        ("aaa", "a3"),                  # a3 same length
        ("aaab", "aaab"),                # a3b1 same length
        ("aaaab", "a4b1"),               # compression helps
        ("aabbccdd", "aabbccdd"),        # a2b2c2d2 same length
        ("aabbbcccc", "a2b3c4"),         # compression helps
    ]
    
    print("Testing string_compression:")
    for input_str, expected in test_cases:
        result = string_compression(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{input_str}' -> '{result}' (expected '{expected}')")


if __name__ == "__main__":
    main()
