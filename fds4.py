def main(): 
    # Get the number of students 
    N = int(input("Enter the number of students: ")) 
     
    marks = [] 
    absent_students = [] 
 
    # Input marks for each student 
    for _ in range(N): 
        name = input("Enter the student's name: ") 
        mark = input(f"Enter marks for {name} (or 'A' if absent): ") 
 
        if mark.upper() == 'A': 
            absent_students.append(name) 
        else: 
            marks.append(int(mark))  # Store marks as integers 
 
    # Calculate average, highest, lowest, and mode 
    if marks: 
        average_score = sum(marks) / len(marks) 
        highest_score = max(marks) 
        lowest_score = min(marks) 
 
        # Find mode (most common score) 
        mode_score = max(set(marks), key=marks.count) 
 
        # Display results 
        print(f"\nAverage score: {average_score:.2f}") 
        print(f"Highest score: {highest_score}") 
        print(f"Lowest score: {lowest_score}") 
        print(f"Most common score: {mode_score}") 
    else: 
        print("No marks entered.") 
 
    # List of absent students 
    if absent_students: 
        print("Absent students:") 
        for student in absent_students: 
            print(student) 
    else: 
        print("No students were absent.");
main()  # Call the main function directly
