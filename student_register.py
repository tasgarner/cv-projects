# recieving user input
students_id_number = ""
num_of_students = int(input("How many students are registering?"))

for i in range(1, (num_of_students + 1)):
# i put +1 instead of putting the range(0, num_of_students) as i wanted the counting to start from 1, not 0
    student_id_number = input(f"You are student number {i}. Please enter your id number: ")
    with open("reg_form.txt", "a+") as f:
        # allowing user to input id and to sign on dotted line in txt file
        f.write("\n Student ID Number: "+student_id_number+"\n Please sign here: .......................\n")