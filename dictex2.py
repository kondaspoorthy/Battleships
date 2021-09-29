string="do you have a voting plan for the election happening next month?"
def mostCommonFirstLetter(string):
    dict = { }
    list=string.split()
    for word in list:
        if(word[0] not in dict):
            dict[word[0]] = 0
        dict[word[0]]+=1
    large=0
    for letter in dict:
        if(dict[letter] > large):
            large=dict[letter]
            string=letter
    return string
print(mostCommonFirstLetter(string))
