students_in_class = [] 
n = int(input("Enter the number of students in class: ")) 
print("Enter the names of the students in class (press enter after each name):") 
for i in range(n): 
    name = input() 
    students_in_class.append(name) 
print("Students in the whole class:", students_in_class) 
# Input the students who play cricket 
cricket_players = [] 
n_cricket = int(input("Enter the number of students who play cricket: ")) 
print("Enter the names of students who play cricket:") 
for i in range(n_cricket): 
    name = input() 
    cricket_players.append(name) 
    # Validate cricket players against the class list 
cricket_players = [x for x in cricket_players if x in students_in_class] 
print("Students who play cricket from class:", cricket_players) 
# Input the students who play badminton 
badminton_players = [] 
n_badminton = int(input("Enter the number of students who play badminton: ")) 
print("Enter the names of students who play badminton:") 
for i in range(n_badminton): 
    name = input() 
    badminton_players.append(name) 
    # Validate badminton players against the class list 
badminton_players = [x for x in badminton_players if x in students_in_class] 
print("Students who play badminton from class:", badminton_players) 
# A. Students who play either cricket or badminton or not both 
only_cricket = [x for x in cricket_players if x not in badminton_players] 
only_badminton = [x for x in badminton_players if x not in cricket_players] 
either_not_both = only_cricket + only_badminton 
print("Students who play either cricket or badminton but not both:", either_not_both) 
# B. Students who play both cricket and badminton 
both_players = [x for x in cricket_players if x in badminton_players] 
print("Students who play both cricket and badminton:", both_players) 
# C. Students who play only cricket 
print("Students who play only cricket:", only_cricket) 
# D. Students who play only badminton 
print("Students who play only badminton:", only_badminton) 
# E. Number of students who play neither cricket nor badminton 
# Create a list of students who play neither sport 
neither_players = [student for student in students_in_class if student not in cricket_players and
student not in badminton_players] 
print("Number of students who play neither cricket nor badminton:", len(neither_players))
