total_classes = int(input("Enter total number of classes held: "))
attended_classes = int(input("Enter number of classes attended: "))

attendance_percentage = (attended_classes / total_classes) * 100

print(f"Attendance Percentage: {attendance_percentage:.2f}%")

if attendance_percentage >= 75:
    print("You are eligible to appear for the exam.")
else:
    print("You are NOT eligible to appear for the exam.")