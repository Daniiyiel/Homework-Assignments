while True:
    try:
        Weight = float(input("Enter your weight in kilogram:"))
        if Weight > 0:
            break
        print("Invalid input.Weight must be greater the 0")
    except ValueError:
        print("Please enter numeric values only")
while True:
    try:
        height = float(input("Enter your height in metres:"))
        if Weight > 0:
            break
        print("Invalid input.Height must be greater than 0")
    except ValueError:
        print("please enter numeric values only")
BMI = Weight/ (height**2)
print("BMI:", round(BMI,2))





while True:
    try:
        Correct_Answer = int(input("Enter your correct Answer:"))
        if Correct_Answer >=0:
            break
        print("Invalid input.Correct Answers must be greater than 0")
    except ValueError:
        print("please enter numeric values only")
while True:
    try:
        Total_Questions = int(input("Enter Total Questions"))
        if Total_Questions > 0:
            break
        print("Invalid input.Total questions must be greater than 0")
    except ValueError:
        print("Please enter numeric value only")
if Correct_Answer > Total_Questions:
    print("Invalid input.total score cant be less")
else:
    Test_score = (Correct_Answer * 100)/Total_Questions
    print("Test score:", round(Test_score,2))



  while True:
      try:
          Alpha_left = float(input("Enter Alpha left:"))
          if 0 < Alpha_left <= 1000:
              break
          else:
              print("Alpha(left) wave power must be greater than zero and less than 1000")
      except ValueError:
          print("Invalid input.please enter a numerical value.")
while True:
      try:
          Alpha_Right = float(input("Enter alpha right:"))
          if 0 < Alpha_Right <= 1000:
              break
          else:
              print("Alpha(Right) must be greater than zero and less than 1000")
      except ValueError:
          print("Invalid input.please enter a numerical value.")
Avg_Alpha_pwr = (Alpha_left + Alpha_Right) / 2
print("Avg_Alpha_pwr:",round(Avg_Alpha_pwr, 2))


while True:
    try:
        Alpha_power = float(input("Enter Alpha Power:"))
        if 0 < Alpha_power <= 1000:
            break
        else:
            print("Alpha power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input. please enter a Numerical value")
while True:
    try:
        Beta_power = float (input("Enter Beta power:"))
        if 0 < Beta_power <= 1000:
            break
        else:
            print("Beta power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input.Please enter a Numerical value.")
Ratio = Alpha_power / Beta_power
print("Ratio:",round(Ratio, 2))


while True:
    try:
        Delta_power = float(input("Enter Delta power:"))
        if 0 < Delta_power <= 1000:
            break
        else:
            print("Delta power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input.Please enter a Numerical value.")
while True:
    try:
        Theta_power = float(input("Enter Theta Power:"))
        if 0 < Theta_power <= 1000:
            break
        else:
             print("Theta power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input.Please enter a Numerical value.")
while True:
    try:
        Alpha_power = float(input("Enter alpha power;"))
        if 0 < Alpha_power <= 1000:
            break
        else:
             print("Alpha power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input.Please enter a Numerical value.")
while True:
    try:
        Beta_power = float(input("Enter Beta power"))
        if 0 < Beta_power <= 1000:
            break
        else:
             print("Beta power must be greater than zero and less than 1000")
    except ValueError:
        print("Invalid input.Please enter a Numerical value.")
Total_power = Delta_power + Theta_power + Alpha_power + Beta_power
Alpha_Contribution = (Alpha_power * 100) / Total_power
print("Alpha contribution:" , round(Alpha_Contribution, 2))

#6
while True:
    try:
        Walk_Calories = float(input("Enter calories expended while walking: "))
        if Walk_Calories > 0:
            break
        else:
            print("Walk_Calories can't be zero or negative. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

while True:
    try:
        Run_Calories = float(input("Enter calories expended while running: "))
        if Run_Calories > 0:
            break
        else:
            print("Run_Calories can't be zero or negative. Try again.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

while True:
    try:
        Walk_Hour = int(input("Enter walking hours: "))
        Walk_Minute = int(input("Enter walking minutes: "))
        if Walk_Hour >= 0 and 0 <= Walk_Minute < 60:
            Walk_time = (Walk_Hour * 60) + Walk_Minute
            break  # Exit loop after valid input
        else:
            print("Walking hours must be 0 or more, and minutes must be between 0 and 59.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

while True:
    try:
        Run_Hour = int(input("Enter running hours: "))
        Run_Minute = int(input("Enter running minutes: "))
        if Run_Hour >= 0 and 0 <= Run_Minute < 60:
            Run_Time = (Run_Hour * 60) + Run_Minute
            break  # Exit loop after valid input
        else:
            print("Running hours must be 0 or more, and minutes must be between 0 and 59.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

Total_calories = (Walk_Calories * Walk_time) + ( Run_Calories * Run_Time)
print(f"Total calories burned: {Total_calories}")


#7
while True:
    try:
        N = int(input("Input a number"))
        if N > 0:
            break
        else:
            print("Please input a positive integer")
    except ValueError:
        print("Please enter valid input")
total = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        total += i ** 3
    else:
        total += i ** 2
print(f"Result:{total}")

#8
while True:
    direction = input("Enter direction (left or right): ").strip().lower()
    if direction in {"left", "right"}:
        break
    print("Invalid input! Please enter 'left' or 'right'.")

while True:
    try:
        d = int(input("Enter number of elements to rotate: ").strip())
        if d >= 0:
            break
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

arr_input = input("Enter a list of numbers separated by spaces or commas: ").strip()
arr = [int(num) for num in arr_input.replace(",", " ").split()]

n= len(arr)
if n > 0 and d > 0:
    d %= n
    if direction == "left":
        arr = arr[d:] + arr[ :d]
    else:
        arr = arr[-d:] + arr[ :-d]
print("Rotated list:" , arr)


#9
shift_type = input("Enter 'row' or 'column': ").strip().lower()


direction = input("Enter direction ('left'/'right' for row, 'up'/'down' for column): ").strip().lower()


index = int(input(f"Enter index of the {shift_type} to shift (0-based index): ").strip())


shift_count = int(input("Enter number of elements to shift: ").strip())


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


print("\nOriginal Matrix:")
for row in matrix:
    print(row)
if shift_type == "row":
    row = matrix[index]
    shift_count %= len(row)
    if direction == "left":
        matrix[index] = row[shift_count:] + row[:shift_count]
    else:
        matrix[index] = row[-shift_count:] + row[:-shift_count]
else:
    col = [matrix[i][index] for i in range(len(matrix))]
    shift_count %= len(col)
    if direction == "up":
        col = col[shift_count:] + col[:shift_count]
    else:
        col = col[-shift_count:] + col[:-shift_count]
    for i in range(len(matrix)):
        matrix[i][index] = col[i]


print("\nShifted Matrix:")
for row in matrix:
    print(row)




