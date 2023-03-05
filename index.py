total_hours = int(input("Enter the total number of hours conducted : "))
total_abs_hours = int(input("Enter the total number of hours absent : "))

total_attended_hours = total_hours - total_abs_hours

percent_attended = ((total_attended_hours / total_hours) * 100)

percent_attended = round(percent_attended, 2)

print("Percent Absent : " + str(percent_attended))

ans = round((100 - percent_attended), 2)

print("Percent Attended : " + str(ans))
#adios