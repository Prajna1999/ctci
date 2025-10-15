# This script runs a benchmark of substring copying vs directly accessing by indices
# also how find() works in python

import timeit
import pandas as pd


# copy the slicing 
def is_unique_slice(str):
    n=len(str)
    for i in range(n-1):
        current_char=str[i]
        remaining_chars=str[i+1:]
        for search_char in remaining_chars:
            if current_char==search_char:
                return False
    
    return True

def is_unique_index(s):
    n = len(s)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False
    return True

def is_unique_find(s):
    for i, char in enumerate(s):
        if s.find(char, i+1)!=-1: #O(n)
            return False
    
    return True


# 1) Early-exit case (duplicate very early)
s_early = "a" + "a" + "b" * 10000

# 2) Mid-exit case (duplicate in the middle)
s_mid = "abcdefg" * 800 + "Z" + "abcdefg" * 800 + "Z"

# 3) Worst-case (all unique) — use a range of unique code points
s_unique = ''.join(chr(i) for i in range(10000))



if __name__=="__main__":

    # benchmarking
    def bench(label, s):
        t_slice=timeit.timeit(lambda:is_unique_slice(s),number=5)
        t_index=timeit.timeit(lambda:is_unique_index(s), number=5)
        t_find=timeit.timeit(lambda:is_unique_find(s), number=5)
        return [label, t_slice, t_index,t_find , t_slice/t_index if t_index else float('inf'), t_find/t_index if t_index else float('inf')]

    rows = [
        bench("Early exit (dup at start)", s_early),
        bench("Mid exit (dup mid)", s_mid),
        bench("Worst case (all unique)", s_unique),
        
    ]
    df=pd.DataFrame(rows, columns=["Case",  "Sice Based (s)","Index Based (s)","Find Method Based (s)", "Slice/Index ratio", "Find/Index ratio"])
    print(df)
    df.to_csv('problems/chpater1/benchmarking.csv')

