name=input("Enter your name here:")
tp_number=input("Enter your TP number here:")
Gender=input("Enter your Gender here:")

score1=float(input("Enter your mark for exam 1 here;"))
score2=float(input("Enter your mark for exam 2 here:"))
score3=float(input("Enter your mark for exam 3 here:"))

average=(score1 + score2 + score3)/3

if average >=90:
    grade ='A'
elif average >=80:
    Grade ='B'
elif average >=70:
    Grade ="C"
elif average >=60:
    Grade ="D"
else:
    Grade ="F"

print(name)
print(tp_number)
print(Gender)
print(Grade)
print(round (average, 2))