#varable names consisting the group members name, age, and weekly allowance
Mem1Name = "Esperanza, Mark Chester Dulay"
Mem1Age = "22"
Mem1Allowance = 1000

Mem2Name = "Gorospe, Christian Nemis"
Mem2Age = "20"
Mem2Allowance = 600

Mem3Name = "Sumao-i, Beverly Bumatnong"
Mem3Age = "20"
Mem3Allowance = 1000

#variable name declaring the Team Name
TeamName = "Angular"

#print the Name, Age, and Allowance per member using concat
print("Team Name:" , TeamName)
print("Member 1: " , Mem1Name, ", his age is" , Mem1Age , ", allowance per week is " , Mem1Allowance)
print("Member 2: " , Mem2Name, ", his age is" , Mem2Age , ", allowance per week is " , Mem2Allowance)
print("Member 3: " , Mem3Name, ", her age is" , Mem3Age , ", llowance per week is " , Mem3Allowance)

#get all the length of the name members
Mem1NameLength = len(Mem1Name)
Mem2NameLength = len(Mem2Name)
Mem3NameLength = len(Mem3Name)

#print the result of length
print(Mem1NameLength)
print(Mem2NameLength)
print(Mem3NameLength)

#convert the string into int
Age1 = int(Mem1Age)
Age2 = int(Mem1Age)
Age3 = int(Mem1Age)

#add the age of all members
AddAge = (Age1 + Age2 + Age3)
#subtract the age of all members
SubAge = (Age1 - Age2 - Age3)
#multiply the age of all members
MultiAge = (Age1 * Age2 * Age3)

print(AddAge)
print(SubAge)
print(MultiAge)