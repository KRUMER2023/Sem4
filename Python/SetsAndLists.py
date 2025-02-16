# wap iterate all inbuilt of set and list
s1={1,1,2,3,56,"bdo"}
s2={5,6,9,2,3,56,"ev"}
print("the 1st Set:\n",s1)
print("the 1st Set:\n",s2)
print("Difference of Set:\n",s1.difference(s2))
print("Difference of Update Set:\n",s2.difference_update(s1))
print("Symmetric Difference of Set\n",s1.symmetric_difference(s2))
print("Intersection of Set\n",s1.intersection(s2))
print("Union of Set\n",s1.union(s2))
# print(s1)