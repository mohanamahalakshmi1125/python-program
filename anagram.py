def is_anagram(s1, s2):


    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    if len(s1) != len(s2):
        print("Not Anagram")
        return

    if sorted(s1) == sorted(s2):
        print("Anagram")
    else:
        print("Not Anagram")
s1 = "listen"
s2 = "silent"

is_anagram(s1,s2)
