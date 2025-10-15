# check if a string input is the permutation of a string.
# for an odd length string, there could be only 1-odd frequency character
# for an event length string, there could be exactly 0-odd frequency character.
# so a given string is a permutation of a palindrome if there exists AT MOST 1, odd-frequency character.
# either zero or at max 1

def is_even(number):
    return (number%2==0)

def check_palindrome_permutation(input_str):
    # create a frequency dictionary
    frequency_dict={}
    for char in input_str:
        if char in frequency_dict:
            current_char_frequency=frequency_dict.get(char, 0)
            current_char_frequency+=1
            frequency_dict[char]=current_char_frequency
        else:
            frequency_dict[char]=1

    # loop over the freq dict
    # no odd frequency charcters or only one odd frequency character
    # the execution cannot break midway, and have to run until the end of the dictionary.
    odd_frequency_character_count=0

    for char_frequency in frequency_dict.values():
        if not is_even(char_frequency):
            odd_frequency_character_count+=1
    # cannot be a palindrom if odd frquency char count exceeds 1
    return (odd_frequency_character_count<=1) 

# Test cases
def main():
    test_cases = [
        ("aab", True),           # "aba"
        ("abc", False),          # can't form palindrome
        ("aabbcc", True),        # "abccba"
        ("aabbc", True),         # "abcba" 
        ("aabbccc", True),       # "cabbbac"
        ("aabbcccd", False),     # 2 odd frequencies (a, d)
        ("racecar", True),       # already a palindrome
        ("a", True),             # single char
        ("", True),              # empty string
        ("aaaaaa", True),        # all same char
        ("tactcoa", True),       # "tacocat"
    ]
    
    print("Testing can_form_palindrome:")
    for s, expected in test_cases:
        result = check_palindrome_permutation(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s}' -> {result} (expected {expected})")


if __name__ == "__main__":
    main()

