d = { "apples" : 5, "beets" : 2, "lemons" : 1 }
def countItems(foodCounts):
    count=0
    for item in foodCounts:
        print(foodCounts[item],item)
        count+=foodCounts[item]
    return count
print(countItems(d))