# Create a list to store data
heart_rate = []
print(heart_rate)

# Take in the name of the participant
name = input("Enter your name: ")

# Capitalize their name
name = "Diaby"
capitalized_name = name.title()
print(capitalized_name)

# greet them with their name: "Hello 'name', please prepare your heart rate data."
print("Hello " + name + ", please prepare your heart rate data.")

# Take in hour one heart rate
hour1_hrt = input("Enter your hour 1 heart rate: ")

# Append this integer value to the list
heart_rate.append(37)
print(heart_rate)

# Take in hour two heart rate
hour2_hrt = input("Enter your hour 2 heart rate: ")

# Append this integer value to the list
heart_rate.append(40)
print(heart_rate)

# Take in hour three heart rate
hour3_hrt = input("Enter your hour 3 heart rate: ")


# Append this integer value to the list
heart_rate.append(45)
print(heart_rate)

# Take in hour four heart rate
hour4_hrt = input("Enter your hour 4 heart rate: ")


# Append this integer value to the list
heart_rate.append(32)
print(heart_rate)

# Take in hour five heart rate
hour5_hrt = input("Enter your hour 5 heart rate: ")


# Append this integer value to the listheart_rate.append(42)
heart_rate.append(41)
print(heart_rate)

# Take in hour six heart rate
hour6_hrt = input("Enter your hour 6 heart rate: ")


# Append this integer value to the list
heart_rate.append(36)
print(heart_rate)

# Take in hour seven heart rate
hour7_hrt = input("Enter your hour 7 heart rate: ")


# Append this integer value to the list
heart_rate.append(33)
print(heart_rate)

# Take in hour eight heart rate
hour8_hrt = input("Enter your hour 8 heart rate: ")


# Append this integer value to the list
#heart_rate.append(50)


# Thank them: "Thank you 'name', we will now calculate your health metrics."
print("Thank you Diaby, we will now calculate your health metrics.")

# Get the maximum heart rate from your list, save into a variable
maximum = max(heart_rate)
print("Maximum heart rate:", maximum)
# print out the patients maximum heart rate during sleep
print("Maximum heart rate:", maximum)

# Get the minimum heart rate from your list, save into a variable
minimum = min(heart_rate)
# print out the patients minimum heart rate during sleep
print("Minimum heart rate:", minimum)

# Calculate the difference between these values
...
# print out this difference
...

# if this difference is greater than 30, print that they experienced waking during sleep
...
# if this difference is greatert han 20, print that their HRV is in a healthy range
...
# otherwise, print out that their HRV is low and might indicate sleep issues
...

# print out their entire heart rate data
...
