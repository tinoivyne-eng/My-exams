# while True:
#     score = float(input("Enter Score: "))
#     if score >= 0 and score <= 100:
#         print("Correct")
#         break
#     else:
#         ("Invalid Score")

students = {}

# input for seven students

for i in range (7):
    name = input("Enter student name: ")

# while loop

    while True:
      score=float(input("Enter score (from 0 to 100): "))

      if score <= 0 and score >= 100:
          break
      else:
          print("invalid score! enter between 0 and 100.")

    students[name]=score

# output

print("\n class report ")

total = 0


# top perfomer

top_name=""
top_score=0

for name in students:
    score = students[name]

    if score > top_score:
        top_score = score
        top_name = name

print(f"\n top student is : {top_name} with {top_score} / 100")







