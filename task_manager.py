
#==========Login Section=============
# creating an empty dictionary
users = {}

#opening and reading user.txt file for valid usernames & splitting the line into usernames & passwords
with open ('user.txt', 'r', encoding='utf-8') as username_in_file:
    for line in username_in_file:
        username_in_file, password_in_file = line.split(", ")
        users[username_in_file.strip()] = password_in_file.strip()

# allowing user input for login, printing a response message
username = input("Please enter your username: ")
while username not in users:
    print("Error: Incorrect username.")
    username = input("Please enter your username: ")
if username in users:
            print("Valid username!")

# repeating the above for the password entry
with open('user.txt', 'r', encoding='utf-8') as password_in_file:
     for line in password_in_file:
        username_in_file, password_in_file = line.split(", ")
        users[password_in_file.strip()] = username_in_file.strip()

user_password = input("Please enter your password: ")
while user_password not in users:
     print("Error: Incorrect password.")
     user_password = input("Please enter a valid password: ")
if user_password in users:
    valid_password = print("Correct password!")

# allowing user to access menu
while True:
    menu = input('''Select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()

    # setting 'r' as an admin only option, which leads onto a new menu
    if menu == "r":
        if username != "admin":
            print("Only admins can register new users.")
            
        elif username == "admin":
            admin_options = (input(""" Please choose from the options below:
            r - register a new user
            d - display statistics (Total number of tasks & users)
            e - exit
            """))
            
            # admin can add new users, by entering name and chosen password (twice)
            if admin_options == "r":
                added_user = (input("Enter the username you\'d like to add: "))
                added_user_password = (input("Enter the password for this user: "))
                new_password = False
        
                while new_password == False:   
                    password_confirm = input("Please retype your password to confirm: ")

                    if added_user_password == password_confirm:
                        new_password = True
            
                    elif new_password == False:
                        print("Passwords do not match. Try again.")
        
                with open ('user.txt', 'a')as user_file:
                    user_file.write(f"\n{added_user}, {added_user_password}")

            #admin can access display stats
            elif admin_options == 'd':
                num_of_tasks = 0
                num_of_users = 0
                
                # taking the number of lines in the 2 txt files to present the stats for tasks and users
                with open("tasks.txt", "r") as task_file:
                    num_of_tasks = len(task_file.readlines())
                    print (f"Total number of tasks: {num_of_tasks}")

                with open("user.txt", "r") as username_in_file:
                    num_of_users = len(username_in_file.readlines())
                    print (f"Total number of users: {num_of_users}")

            # allowing user to exit admin menu
            elif admin_options == 'e':
                exit

    # regular menu for other users, appending tasks to the task.txt file
    elif menu == "a":
        task_file = open("tasks.txt", "a+")
        added_username_task = input("Enter the username of the assignee: ")
        
        added_task_title = input("Enter the title of the task: ")
        added_task_description = input("Give a description of the task:\n")
        task_due_date = input("Enter the due date [in format dd-mm-yyyy]:\n")
        task_status = input("Has the task been completed? [Yes or No]: ") 
        
        task_file.write(f"\n{added_username_task}, {added_task_title}, {added_task_description}, {task_due_date}, {task_status}")
        task_file.close()

    # allowing users to view all tasks
    elif menu == "va":
        task_file = open("tasks.txt", "r")
        
        # stripping and splitting the lines for formatting purposes
        for line in task_file:
            task_file_content = line.strip().split(",")
            
            # using indexing to print the correct information in a clear format
            print(f"""
            Task username:          {task_file_content[0]}
            Task tile:              {task_file_content[1]}
            Task description:       {task_file_content[2]}
            Task due date:          {task_file_content[3]}
            Task completion:        {task_file_content[4]}
            """)

    # repeating the above for the 'vm' option
    elif menu == "vm":
        
        # asking user to confirm the username of the tasks they would like to be checked
        with open("tasks.txt", "r") as task_file:
            username_search = input("What user\'s tasks are you looking for?:")
            lines = task_file.readlines()

            for line in lines:
                task_file_content = line.strip().split(",")
                if line.find(username_search) != -1: 
                    print(f"""
                    Task username:          {task_file_content[0]}
                    Task tile:              {task_file_content[1]}
                    Task description:       {task_file_content[2]}
                    Task due date:          {task_file_content[3]}
                    Task completion:        {task_file_content[4]}
                    """)
    
    elif menu == 'e':
        print('Closing program')
        exit()

    # printing corresponding error message for invalid choice 
    else:
        print("Error: You have made an invalid choice, please try again")