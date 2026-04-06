#Bài 5
def count_vowels(s):
    tong = 0
    nguyen_am = "ueoaiUEOAI"
    for i in s:
        if i in nguyen_am:
            tong = tong + 1
    return tong