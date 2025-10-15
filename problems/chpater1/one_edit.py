# check if two strings is one edit (insertion,deletion or replacement) away
# return True if they are zero or One edit away
def check_one_edit_away(s1,s2):

    # if length difference is more than 1, then terminate the looping
    # and return false
    len1, len2=len(s1), len(s2)
    if abs(len1-len2) >1:
        return False

    # ensure s1 is the shorter or equal length
    if len1>len2:
        s1,s2, len1, len2=s2,s1,len2, len1

    i=j=0
    found_difference=False

    while i<len1 and j<len2:

        if s1[i]!=s2[j]:
            # if first found difference already crossed

            if found_difference:
                # found second difference
                return False
            found_difference=True

            if len1!=len2:
                # insert/delete operation
                j+=1
            else:
                # replace operation
                i+=1
                j+=1
        else:
            # both chars match
            # move both pointers
            i+=1
            j+=1
    

    return True


def main():
    test_cases = [
        ("pale", "ple", True),      # delete
        ("pales", "pale", True),    # insert
        ("pale", "bale", True),     # replace
        ("pale", "bae", False),     # 2 operations
        ("pale", "ealb", False),    # not one edit
        ("", "a", True),            # insert into empty
        ("a", "", True),            # delete to empty
        ("", "", True),             # no edit needed
        ("abc", "abc", True),       # identical
        ("abc", "abcd", True),      # insert at end
        ("abc", "adc", True),       # replace middle
        ("abc", "def", False),      # all different
        ("bale", "balee", True)        
    ]
    
    print("Testing one_edit_away:")
    for s1, s2, expected in test_cases:
        result = check_one_edit_away(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{s1}' & '{s2}' -> {result} (expected {expected})")


if __name__ == "__main__":
    main()
