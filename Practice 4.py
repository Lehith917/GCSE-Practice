#Create a program to ask for the marks of 5 subjects (for example- English, Math, Science, Computer Science, and Arts). 
# Calculate and print the total marks and average(mean) of the marks.
# If the mean is between 80 and 100, print the remarks as excellent.
# If the mean is between 60 and 80, print the remarks as very good.
# If the mean is between 40 and 60, print the remarks as good.
# If the mean is less than 40, print the remarks as can do better.
English=float(input("Enter the mark you have gotten for the English subject: "))
Maths=float(input("Enter the mark you have gotten for the Maths subject: "))
Science=float(input("Enter the mark you have gotten for the Science subject: "))
Computers=float(input("Enter the mark you have gotten for the Computers subject: "))
Art=float(input("Enter the mark you have gotten for the Art subject: "))
total= English + Maths + Science + Computers + Art
average= total/5
print("The total marks you have obtained is: ",total,"/500")
print("The average of your marks is: ",average)
if 80<=average<=100:
    print("You did excellent")
elif 60<=average<=79:
    print("You did very good")
elif 40<=average<=59:
    print("You did good")
else:
    print("You can do better")
