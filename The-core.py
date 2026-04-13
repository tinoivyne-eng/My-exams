Students={}

# loop runs exactly 7 times
for i in range (7):
    name=input("Enter student name (or 'done')to quit): ")
    if name == "done":
       break
    
    score = float(input("Enter score (out of 50): "))

    Students[name]=score
    
print("\n class report ")

# output
total = 0
for name in Students:
   score=Students[name]
   print(f"{name}: {score} / 50")
   total += score

average = total/7
print(f"\n Total Score: {total} / 350")
print(f"Class Average: {average} / 50")