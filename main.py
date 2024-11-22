# Create a list to store data
heart_rate = []
print(heart_rate)

# Take in the name of the participant
name = input("Enter your name: ")
print("Hello, " + str(name) + "!")

# Capitalize their name
capitalized_name = name.title()
print(capitalized_name)

# greet them with their name: "Hello 'name', please prepare your heart rate data."
print("Hello " + name + ", please prepare your heart rate data.")

# Take in hour one heart rate
hour1_hrt = int(input("Enter your hour 1 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour1_hrt)
print(heart_rate)

# Take in hour two heart rate
hour2_hrt = int(input("Enter your hour 2 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour2_hrt)
print(heart_rate)

# Take in hour three heart rate
hour3_hrt = int(input("Enter your hour 3 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour3_hrt)
print(heart_rate)

# Take in hour four heart rate
hour4_hrt = int(input("Enter your hour 4 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour4_hrt)
print(heart_rate)

# Take in hour five heart rate
hour5_hrt = int(input("Enter your hour 5 heart rate: "))

# Append this integer value to the listheart_rate.append(42)
heart_rate.append(hour5_hrt)
print(heart_rate)

# Take in hour six heart rate
hour6_hrt = int(input("Enter your hour 6 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour6_hrt)
print(heart_rate)

# Take in hour seven heart rate
hour7_hrt = int(input("Enter your hour 7 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour7_hrt)
print(heart_rate)

# Take in hour eight heart rate
hour8_hrt = int(input("Enter your hour 8 heart rate: "))

# Append this integer value to the list
heart_rate.append(hour8_hrt)
print(heart_rate)

# Thank them: "Thank you 'name', we will now calculate your health metrics."
print("Thank you Diaby, we will now calculate your health metrics.")

# Get the maximum heart rate from your list, save into a variable
maximum = max(heart_rate)

# print out the patients maximum heart rate during sleep
print("Maximum heart rate:", maximum)

# Get the minimum heart rate from your list, save into a variable
minimum = min(heart_rate)

# print out the patients minimum heart rate during sleep
print("Minimum heart rate:", minimum)

# Calculate the difference between these values
diff = (maximum - minimum)

# print out this difference
print("difference:", diff)

# if this difference is greater than 30, print that they experienced waking during sleep
if diff > 30:
    print("they experienced waking during sleep")

# if this difference is greatert han 20, print that their HRV is in a healthy range
elif 20 < diff < 30:
    print("their HRV is in a healthy range")
    
# otherwise, print out that their HRV is low and might indicate sleep issues
else:
    print("their HRV is low and might indicate sleep issues")

# print out their entire heart rate data
print("The entire list of heart rate data enter by the user is: ", heart_rate)
print("The user's maximum heart rate is: ", maximum)
print("The user's minimum heart rate is: ", minimum)
print("The difference between the maximum and the minimum heart rate is: ", diff)
print("The user's potential sleep quality is bad or good depending on the value of their HRV")
