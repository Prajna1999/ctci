# replace whitespaces with '%20'
# also the true length of the string is also given in the question
# convert only one space to "%20".
# if there are multiple spaces, squish them


def urlify(s, true_length):
    # strip leading.ttailing spaces
    s=s.strip()
    result=[]
    prev_was_space=False

    for char in s:
        if char==' ':
            # if precious char was not space
            if not prev_was_space:

                result.append('%20')
            prev_was_space=True
        else:
            result.append(char)
            prev_was_space=False
    
    return ''.join(result)

if __name__=="__main__":
    s="       Mr  John           Smith      "
    print(urlify(s,13))