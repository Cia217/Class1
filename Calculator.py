team1= 158
team2= 109
team3= 87
team4= 95
team5= 120
Total = team1 + team2 + team3 + team4 + team5
Average =Total/5

print("Total points:", Total)
print("Average per team:", Average)

stars_per_point= 2
reward_stars= Total * stars_per_point
print("Total reward stars:", reward_stars)

boxes = reward_stars//25
leftover = reward_stars%25
print("Full boxes packed:", boxes)
print("Leftoves boxes:", leftover)

last_week= 500
print("Better than last week? :", Total > last_week)
print("Same as last week? :", Total==last_week)
print("At least  as good? :", Total >= last_week)

Total +=30
print("After bonus points:", Total)

Total -=15
print("After missed tasks:", Total)

reward_stars = Total * stars_per_point
boxes = reward_stars//25
print("Final boxes packed:", boxes)