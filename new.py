lst=[[2,2],[2,3],[3,4],[5,6]]
count=0
l=list(map(lambda x: 1 if(3 in x) else 0,lst))
print(lst.count(3))