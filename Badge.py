name = input("Member_name :")
club = input("Club_name :")
member_number= 17
print("Member_number:",member_number,type(member_number))
points= 5
print("Points:",points,type(points))
active= True
print("Active:",active,type(active))

badge_code = name[0:3] + club[-1:] +str(member_number)
print("Badge code:", badge_code)

print("===CLUB BADGE===")
print("Member:" + name)
print("Club:" + club)
print("Code:" + badge_code)
print("Points:" + str(points) + " | Active:" + str(active))