score= 39
if score==100:
    print("Excellent")
elif score>= 80:
    print("Amazing") 
elif score>= 60:
    print("Average")    
elif score>= 50:
    print("Good")    
else:
    print("Try again")    
    
    weather= "yes"
    homework= "yes"
print(weather=="yes" and homework=="yes" )
print("After school; Go to the park")

party= "Birthday"
grade= "pass"
if grade=="pass"or party=="no Birthday":
   print("I will have a birthday party")

homework= "no"
if not (homework=="yes"):
  print("Homework: you can go play")  

day= "Tuesday"  
if day!= ("Saturday"):
    print("It is not a weekend")

weather="sunny"
homework="no"
day="Thursday"
# Topic 5 - Combining AND + OR + NOT
if weather == "rainy" and not (homework == "yes"):
    print("Best plan : Stay in, finish homework first.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan : All set for a great school day!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan : Perfect weekend - head outside!")
else:
    print("Best plan : Take it one step at a time!")