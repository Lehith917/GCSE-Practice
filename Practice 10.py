#Create a program that calculates and returns the area of a square
# def square():
#     side=float(input("Enter one of the sides the square: "))
#     square_area=side*side
#     return square_area

# area=square()
# print(area)


# def rectangle(s1,s2):
#     area=s1*s2
#     return area
# answer=rectangle(2,3)
# print(answer)

#Return area of circle
# PI=3.71
# def circle():
#     radius=float(input("Enter the radius"))
#     area=radius*radius*PI
#     return area
# answer=circle()
# print(answer)

#Create a Marksheet program and add the procedure that:
# Takes input for basic details like name, age and scores in English, Maths and Computer Science.
# Calculates the total score and the average score/ mean of the score.
# Assigns remark based on the average score. (Excellent / very good / good / can do better).
# Print all the details including the total score, the average score and the remark.

def score():
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    E_score=float(input("Enter your score in English: "))
    M_score=float(input("Enter your score in Maths: "))
    C_score=float(input("Enter your score in Computers: "))
    total=E_score+M_score+C_score
    average=total/3
    remark=""
    if average>=85:
        remark="Excellent"
    elif 70<=average<=84:
        remark="Very good"
    elif 50<=average<=69:
        remark="Good"
    else:
        remark="Can do better"
    print(name, "\n",age,"\n your total score is \n",total,"\n your average for all the subjects is \n",average,"\n you did \n",remark)
score()