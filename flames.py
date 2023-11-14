print ("Welcome to this game")

userInp1 = input ("Enter the first person name: ")
userInp2 = input ("Enter the second person name: ")

userInp1 = userInp1.lower().replace(" ", "")
userInp2 = userInp2.lower().replace(" ", "")

user_inputs1 = [char for char in userInp1]
user_inputs2 = [char for char in userInp2]


for i in user_inputs1[:]:
    if (i in user_inputs2):
        user_inputs1.remove(i)
        user_inputs2.remove(i)

userInputs1 = user_inputs1
userInputs2 = user_inputs2


count1 = len(userInputs1)
count2 = len(userInputs2)

count = count1 + count2


categories = ["Friend", "Love", "Affection", "Marriage", "Enemies", "Siblings"]


result = categories[count % len(categories) - 1]

print(f"FLAMES game result: {result}")

