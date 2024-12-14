def selection_sort(score_list): 
    """Sort the list using Selection Sort."""

    for i in range(len(score_list) - 1): 
        min_index = i 
    for j in range(i + 1, len(score_list)): 
        if score_list[min_index] > score_list[j]: 
            min_index = j 
            score_list[i], score_list[min_index] = score_list[min_index], score_list[i] 
def bubble_sort(score_list): 
    """Sort the list using Bubble Sort.""" 
    n = len(score_list) 
    for i in range(n): 
        for j in range(n - 1): 
            if score_list[j] > score_list[j + 1]: 
                score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j] 
def top_five(score_list): 
    """Display the top five scores from the sorted list.""" 
    selection_sort(score_list)  # Ensure the list is sorted 
    top_scores = score_list[-5:]  # Get the last five scores (top scores) 
    print("Top Five Scores are:", top_scores) 
# Main program 
n = int(input("Enter the number of students present in the class: ")) 
print("Enter the scores (in floating point):") 
score_list = [] 
for i in range(n): 
    data = float(input()) 
    score_list.append(data) 
print("Unsorted Scores:", score_list) 
while True: 
    print("\nEnter \n 1. Selection Sort \n 2. Bubble Sort \n 3. Display Top Five Scores \n 4. Exit") 
    option = input("Enter option: ") 
    if option == "1": 
        selection_sort(score_list) 
        print("Sorted Scores using Selection Sort:", score_list) 
    elif option == "2": 
        bubble_sort(score_list) 
        print("Sorted Scores using Bubble Sort:", score_list) 
    elif option == "3": 
        top_five(score_list) 
    elif option == "4": 
        print("Exiting the program.") 
        break 
    else: 
        print("Invalid option! Please try again.")
