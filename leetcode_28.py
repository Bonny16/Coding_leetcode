'''Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
 or -1 if needle is not part of haystack'''

def occur(haystack: str, neddle: str):
    m = len(haystack)
    n = len(neddle)

    for j in range(m-n+1):
        for i in range(n):
            if neddle[i] != haystack[j+i]:
                break
            if i == n-1:
                return j
            
haystack = "kjkleetcode"
neddle = "leetc"

print(occur(haystack, neddle))
