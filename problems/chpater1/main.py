# is unique string
#1. If the string does not contain duplicates

def is_unique(str):
    n=len(str)

    for i in range(n-1):

        for j in range(i+1,n):
            if str[i]==str[j]:
                return False
    
    return True


if __name__=="__main__":
    str='abA'

    print(is_unique(str))
