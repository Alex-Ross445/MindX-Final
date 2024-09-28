city = [["BD", 9.224, 247100], ["BTL", 43.35, 333330], ["CG", 12.04, 266800], ["DD", 9.96, 420900], ["HBT", 10.09,318000]]
district = [city[i][0] for i in city]
sorted_district = district.sort()
print(sorted_district)