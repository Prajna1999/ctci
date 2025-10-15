# compare two strings and figure out if one is the permutation of the other.
# For two strings out of which one to be the permutation of other, they must have
# 1. Same number of characters.
# 2. Same: the frequency of each chars should be the same across the two strings.
# Example: "abcdf" <---> "cdfba" are permutations while
# "abcdf" <----> "fcdbb" is not

def string_frequency_map_builder(s):
    h={}
    for char in s:
        if char not in h:
            h[char]=1
        else:
            char_count=h.get(char,0)
            char_count+=1
            h[char]=char_count
    return h

def compare_strings_permutation(s1,s2):
    # if string lengths do not match, then return False
    n1=len(s1)
    n2=len(s2)
    if n1!=n2:
        return False
    
    # create both hashmap.
    h1=string_frequency_map_builder(s1)
    h2=string_frequency_map_builder(s2)

    # iterate over one map and compare the freq with the other.
    # at first mismatch return 
    for char in h1:
        char_frequency_h1= h1.get(char)
        char_frequency_h2=h2.get(char)

        if char_frequency_h1!=char_frequency_h2:
            return False
    
    return True

  
if __name__=="__main__":
    s1='ad'
    s2='da'
    print(compare_strings_permutation(s1,s2))
    


