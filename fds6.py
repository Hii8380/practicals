def insertion_sort(arr):
    """Sort the array using Insertion Sort."""
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    """Sort the array using Shell Sort."""
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def display_top_five(scores):
    """Display the top five scores."""
    top_five = scores[:5]
    print("Top 5 scores (ascending order):")
    for score in top_five:
        print(f"{score:.2f}")

def main():
    # Take input from the user (second-year percentages of students)
    n = int(input("Enter the number of students: "))
    scores = []
    
    for i in range(n):
        score = float(input(f"Enter the percentage of student {i+1}: "))
        scores.append(score)
    
    # Choose sorting algorithm
    print("\nSorting using Insertion Sort...")
    insertion_sort(scores)
    display_top_five(scores)
    
    # Re-enter the input and sort using Shell Sort
    print("\nRe-enter the scores for Shell Sort...")
    scores.clear()  # Clear previous scores
    for i in range(n):
        score = float(input(f"Enter the percentage of student {i+1}: "))
        scores.append(score)
    
    print("\nSorting using Shell Sort...")
    shell_sort(scores)
    display_top_five(scores)

if __name__ == "__main__":
    main()
