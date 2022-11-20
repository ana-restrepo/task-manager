# This program is a task manager for a small business.
# It asks the user to login and checks their credentials. Then shows them a menu according to their permissions.
# A regular user can add a new task, see all the tasks on the system and see their own tasks.
# The admin user can also register new users and consult the total of tasks and users on the linked data files.

# =====Importing Libraries===========
from datetime import datetime


# =====Function Definition===========

# Function to read data from the users file and create a dictionary with usernames as key and passwords as value.
def user_dictionary():

    # Read data from the users file and create a dictionary with usernames as key and passwords as value.
    users = {}

    with open("user.txt", "r") as users_file:
        for item in users_file:
            data = str(item)
            data = data.replace(" ", "")
            data = data.strip("\n")
            user = data.split(",")
            users[user[0]] = user[1]

    # This function returns a dictionary of users in the following format: {user: password}
    return users


# Function to read the task file and create a list with all the items in it.
def task_list():

    # Open the task file and loop through the lines organizing them into lists.
    # Append each task list onto a list.
    all_tasks = []

    with open("tasks.txt", "r") as tasks_file:
        for item in tasks_file:
            item = item.strip("\n")
            item = item.split(", ")
            all_tasks.append(item)

    # This functions returns a list of lists. Each nested list in the following format:
    # ["user", "title", "description", "date generated (dd Mon yyyy)", "date due (dd Mon yyyy)", "completed (Yes/No)"]
    return all_tasks


# Function for login.
def user_login(users):

    # Ask user to enter their username and validate that it exists in the database.
    # If user exists, ask for their password and validate it is correct.
    while True:
        username = input("Please enter your username: ")
        if username in users.keys():
            while True:
                password = input("Please enter your password: ")
                if password == users[username]:
                    break
                else:
                    print("Incorrect password.\n")
            break
        else:
            print("Username doesn't exist.\n")

    # This function returns the username of the using that has logged in as a string.
    return username


# Function to register a new user.
def reg_user():

    # Call function to retrieve update dictionary of users in the database: {user: password}
    users = user_dictionary()

    # Ask user to enter the new username and validate that it doesn't exist in the database.
    while True:
        new_user = input("\nPlease enter the username you want to add to the data base: ")
        if new_user not in users.keys():

            # Ask user to enter a new password and to confirm the entry by typing it again.
            # If the passwords coincide, write username and password into the user.txt file.
            # Otherwise, ask the user to enter the new password again.
            while True:
                new_password = input("Please enter the password for the new user: ")
                confirm_password = input("Please confirm the password, by entering it once more: ")
                if new_password == confirm_password:
                    with open("user.txt", "a+") as user_registry:
                        user_registry.write(f"\n{new_user}, {new_password}")
                    users[new_user] = new_password
                    print("\nThe new user has been successfully registered.")
                    break
                else:
                    print("Passwords do not match. Please try again.\n")
            break
        else:
            print("This username already exists. Please enter a different username.")


# Function to check that a date is in the future.
# The format for check_date should be a list of three integers: [day, month, year]
def is_future(check_date):

    # Retrieve current date.
    current_date_time = datetime.now()

    # Compare parameter with current time to establish if the date has passed.
    if check_date[2] > current_date_time.year:
        future_date = True
    elif check_date[2] == current_date_time.year:
        if check_date[1] > current_date_time.month:
            future_date = True
        elif check_date[1] == current_date_time.month:
            if check_date[0] >= current_date_time.day:
                future_date = True
            else:
                future_date = False
        else:
            future_date = False
    else:
        future_date = False

    # This function returns True if the date is in the future, and False if it has passed.
    return future_date


# Function to enter a due date, validate that the input is appropriate and the date is in the future.
def date_entry():

    # Ask user to enter the desired due date.
    due_date = input("Please enter the due date for the task (dd-mm-yyyy): ")

    while True:
        due_date = due_date.split("-")

        # Validate that the list with the due date entered has three items.
        while True:
            if len(due_date) != 3:
                due_date = input("Invalid date. Please enter the due date for the task (dd-mm-yyyy): ")
                due_date = due_date.split("-")
            else:
                break

        # Check that the info on the date list can be cast as an integer.
        if due_date[0].isdigit() and due_date[1].isdigit() and due_date[2].isdigit():
            due_date = [int(num) for num in due_date]

            # Call function to validate date entered is a future date.
            future_date = is_future(due_date)

            # Validate date entered has a day within the valid range for each month, i.e. 33 december is not valid.
            # If the date is in the future and is valid:
            # Cast all elements into strings and replace month with first three letters of month's name.
            if future_date:
                if due_date[1] == 1 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Jan"
                    break
                elif due_date[1] == 2:
                    if due_date[0] <= 29 and due_date[2] % 4 == 0:
                        due_date = [str(item) for item in due_date]
                        due_date[1] = "Feb"
                        break
                    elif due_date[0] <= 28:
                        due_date = [str(item) for item in due_date]
                        due_date[1] = "Feb"
                        break
                    else:
                        due_date = input("Invalid date. Please enter due date (dd-mm-yyy): ")
                elif due_date[1] == 3 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Mar"
                    break
                elif due_date[1] == 4 and due_date[0] <= 30:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Apr"
                    break
                elif due_date[1] == 5 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "May"
                    break
                elif due_date[1] == 6 and due_date[0] <= 30:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Jun"
                    break
                elif due_date[1] == 7 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Jul"
                    break
                elif due_date[1] == 8 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Aug"
                    break
                elif due_date[1] == 9 and due_date[0] <= 30:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Sep"
                    break
                elif due_date[1] == 10 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Oct"
                    break
                elif due_date[1] == 11 and due_date[0] <= 30:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Nov"
                    break
                elif due_date[1] == 12 and due_date[0] <= 31:
                    due_date = [str(item) for item in due_date]
                    due_date[1] = "Dic"
                    break
                else:
                    due_date = input("Invalid date. Please enter due date (dd-mm-yyy): ")
            else:
                due_date = input("This date has passed. Please enter due date (dd-mm-yyy): ")
        else:
            due_date = input("Invalid date. Please enter due date (dd-mm-yyy): ")

    # Transform the due date into the correct format for writing in the tasks file.
    due_date = " ".join(due_date)

    # This function returns a date in the following format "dd Mon yyyy"
    return due_date


# Function to add a new task.
# This function requires a username parameter as a string.
def add_task(username):

    # Ask user to enter a title and description for a task, a due date for the task and retrieve the current date.
    title_task = input("Please enter a title for the task: ")
    task_description = input("Please enter a task description: ")

    # Call functions to: enter and check the due date, and return the current date in the right format for the file.
    due_date = date_entry()
    current_date = format_current_date()

    # Write information in the task file in the correct format and notify the user when the process is complete.
    with open("tasks.txt", "a") as tasks_file:
        tasks_file.write(f"{username}, {title_task}, {task_description}, "
                         f"{current_date}, {due_date}, No\n")

    print("\nNew task has been successfully added to the task file.")


# Function to view all the tasks on file.
def view_all():

    # Open the task file and extract the information in each line, then print it in an organised manner.
    print(f"\nTask list"
          f"\n{'-' * 120}")
    tasks = task_list()
    for task in tasks:
        print(f"User:\t\t\t\t{task[0]}"
              f"\nTitle:\t\t\t\t{task[1]}"
              f"\nDescription:\t\t{task[2]}"
              f"\nDate assigned:\t\t{task[3]}"
              f"\nDue date :\t\t\t{task[4]}"
              f"\nCompleted?:\t\t\t{task[5]}"
              f"\n{'-' * 120}")


# Function to view the tasks assigned to the user logged in.
# This function requires the username of the person logged in as a string.
def view_mine(logged_in_user):

    # Declare variables.
    no_tasks_assigned = 0
    user_tasks = {}
    counter = 0
    task_number = 0

    # Open task file, check each line to see if the user has any tasks assigned.
    # If the current user and the task user coincide, print the task information.
    print("\nMy Tasks")
    tasks = task_list()
    for task in tasks:
        counter += 1
        if task[0] == logged_in_user:
            task_number += 1
            print(f"{'-' * 120}"
                  f"\nTask number:\t\t{task_number}"
                  f"\nUser:\t\t\t\t{task[0]}"
                  f"\nTitle:\t\t\t\t{task[1]}"
                  f"\nDescription:\t\t{task[2]}"
                  f"\nDate assigned:\t\t{task[3]}"
                  f"\nDue date :\t\t\t{task[4]}"
                  f"\nCompleted?:\t\t\t{task[5]}")
            user_tasks[str(task_number)] = task
        else:
            no_tasks_assigned += 1

    # If no tasks are found for the user logged in, print a message letting them know.
    if no_tasks_assigned == counter:
        print("\nYou don't have any tasks assigned at the moment.")
    else:
        print(f"{'-' * 120}")

    # This function returns a list of the tasks assigned to the current user.
    return user_tasks


# Function to format date from file into integer date for functions.
# This function takes a date in the following format: ["dd", "Mon", "yyyy"]
def format_file_date(due_date):

    # Replace the info in the month position with numbers instead of the three first letters of the month.
    if due_date[1] == "Jan":
        due_date[1] = "1"
    elif due_date[1] == "Feb":
        due_date[1] = "2"
    elif due_date[1] == "Mar":
        due_date[1] = "3"
    elif due_date[1] == "Apr":
        due_date[1] = "4"
    elif due_date[1] == "May":
        due_date[1] = "5"
    elif due_date[1] == "Jun":
        due_date[1] = "6"
    elif due_date[1] == "Jul":
        due_date[1] = "7"
    elif due_date[1] == "Aug":
        due_date[1] = "8"
    elif due_date[1] == "Sep":
        due_date[1] = "9"
    elif due_date[1] == "Oct":
        due_date[1] = "10"
    elif due_date[1] == "Nov":
        due_date[1] = "11"
    else:
        due_date[1] = "12"

    # Cast each element into the list to an integer.
    due_date = [int(item) for item in due_date]

    # This function returns a date of three integers in the following format: [dd, mm, yyyy]
    return due_date


# Function to format the current date into an appropriate string to write in output files.
def format_current_date():

    current_date_time = datetime.now()

    # Find current month and assign the three first letters of its name to a variable called month.
    # Then rewrite current date in the correct format to be written on the task file.
    if current_date_time.month == 1:
        month = "Jan"
    elif current_date_time.month == 2:
        month = "Feb"
    elif current_date_time.month == 3:
        month = "Mar"
    elif current_date_time.month == 4:
        month = "Apr"
    elif current_date_time.month == 5:
        month = "May"
    elif current_date_time.month == 6:
        month = "Jun"
    elif current_date_time.month == 7:
        month = "Jul"
    elif current_date_time.month == 8:
        month = "Aug"
    elif current_date_time.month == 9:
        month = "Sep"
    elif current_date_time.month == 10:
        month = "Oct"
    elif current_date_time.month == 11:
        month = "Nov"
    else:
        month = "Dec"

    # This function returns the current date as a string in the following format: "dd Mon yyyy".
    return f"{current_date_time.day} {month} {current_date_time.year}"


# Function to create task report.
def task_overview():

    # Call function to retrieve a list of tasks from the task file.
    tasks = task_list()

    # Define variables.
    completed_tasks = 0
    unfinished_tasks = 0
    overdue_tasks = 0
    task_total = 0

    # Loop through the task list counting: total of tasks, tasks completed, incomplete tasks and overdue tasks.
    for task in tasks:
        task_total += 1
        if task[5] == "Yes":
            completed_tasks += 1
        else:
            unfinished_tasks += 1
            date_file = task[4].split()
            if is_future(format_file_date(date_file)):
                continue
            else:
                overdue_tasks += 1

    # Create or overwrite the task overview report with the information collected above.
    with open("task_overview.txt", "w") as task_report:
        task_report.write(f"Task Overview Report\t\t\tDate generated: {format_current_date()}\n"
                          f"\n\tTotal number of tasks:\t\t\t\t{task_total}"
                          f"\n\tTotal number of completed tasks:\t{completed_tasks}"
                          f"\n\tTotal number of unfinished tasks:\t{unfinished_tasks}"
                          f"\n\tTotal number of overdue tasks:\t\t{overdue_tasks}"
                          f"\n\tPercentage of incomplete tasks:"
                          f"\t\t{round((unfinished_tasks * 100) / task_total, 2)}%"
                          f"\n\tPercentage of overdue tasks:"
                          f"\t\t{round((overdue_tasks * 100) / task_total, 2)}%")


# Function to create user report.
def user_overview():

    # Call functions to retrieve a list of tasks from the task file and the user dictionary from the user file.
    tasks = task_list()
    users = user_dictionary()

    # Declare variables.
    report_text = ""

    # Create or overwrite user report file and print general information.
    with open("user_overview.txt", "w") as user_report:
        user_report.write(f"User Overview Report\t\t\t\t\t\t\tDate generated: {format_current_date()}\n"
                          f"\n\tTotal number of users on the system:\t{len(users)}"
                          f"\n\tTotal number of tasks on the system:\t{len(tasks)}"
                          f"\n\n{'-' * 120}")

    # For each user loop through the task list counting:
    # Total of tasks, tasks completed, incomplete tasks and overdue tasks.
    for user in users.keys():
        user_completed = 0
        user_unfinished = 0
        user_overdue = 0
        user_task_total = 0

        for task in tasks:
            if user == task[0]:
                user_task_total += 1

                if task[5] == "Yes":
                    user_completed += 1
                else:
                    user_unfinished += 1
                    date_file = task[4].split()
                    if is_future(format_file_date(date_file)):
                        continue
                    else:
                        user_overdue += 1

        # If the user has no tasks assigned, add a message to the report text stating so.
        # Else, add a message containing all the information from above plus some percentage calculations.
        if user_task_total == 0:
            report_text = report_text + f"\n\tUser: {user}\n\t\tThis user has no tasks assigned.\n{'-' * 120}"
        else:
            report_text = report_text + f"\n\tUser: {user}" \
                                        f"\n\t\tTotal number of tasks:\t\t\t\t\t\t\t\t\t\t{user_task_total}"\
                                        f"\n\t\tPercentage of all tasks assigned to user:" \
                                        f"\t\t\t\t\t{round((user_task_total * 100) / len(tasks), 2)}%" \
                                        f"\n\t\tPercentage of completed tasks from all assigned to user:" \
                                        f"\t{round((user_completed * 100) / user_task_total, 2)}%" \
                                        f"\n\t\tPercentage of incomplete tasks:"\
                                        f"\t\t\t\t\t\t\t\t{round((user_unfinished * 100) / user_task_total, 2)}%"\
                                        f"\n\t\tPercentage of overdue tasks:"\
                                        f"\t\t\t\t\t\t\t\t{round((user_overdue * 100) / user_task_total, 2)}%" \
                                        f"\n{'-' * 120}"

    # Append the user information to the user report file.
    with open("user_overview.txt", "a") as user_report:
        user_report.write(report_text)


# Function to retrieve statistics from the report files and display them.
def display_statistics():

    # Call functions to create task and user overview reports.
    task_overview()
    user_overview()
    print(f"\n{'-' * 120}")

    # Read task overview report and print all the lines.
    with open("task_overview.txt", "r") as task_file:
        tasks = task_file.readlines()
        for line in tasks:
            line = line.strip("\n")
            print(line)
        print(f"\n{'-' * 120}")

    # Read user overview report and print the title line and the line with total number of users.
    with open("user_overview.txt", "r") as user_file:
        users = user_file.readlines()
        for line in users[: 3]:
            line = line.strip("\n")
            print(line)
        print(f"\n{'-' * 120}")


""" Source: https://www.w3schools.com/python/ref_file_readlines.asp
On one of the discord support threads, someone mentioned a method that returns the content of a text file as a list,
where each line is a list item. I read a bit more about it on the link above. 
I have used this method for the display_statistics function in my program.
"""


# Function to display statistics from the user report file for one or more users.
def user_statistics():

    # Call function to retrieve user dictionary.
    users = user_dictionary()

    # Declare variables.
    users_check = []

    # Ask user to enter the username of each of the users they want to see a report for.
    # Check the data entered is on the user dictionary. And add to list users_check if it is.
    while True:
        username = input("\nPlease enter a username you want to see a report for (-1 to exit): ")
        if username in users.keys() and username not in users_check:
            print("Username added to the list of names to check, you may add more names if required.")
            users_check.append(username)
        elif username in users.keys() and username in users_check:
            print("This username is already on the list.")
        elif username == "-1":
            break
        else:
            print("Username doesn't exist.")

    # Call function to create user overview report, divide it by sections using {'-' * 120} and store result on a list.
    user_overview()
    with open("user_overview.txt", "r") as user_file:
        file_info = user_file.read().split(f"{'-' * 120}")

    # For each username entered, print the corresponding statistics from the user report file.
    if not users_check:
        print("No usernames were entered for checking statistics.")
    else:
        print(f"{'-' * 120}")
        for item in file_info:
            for user in users_check:
                if f"User: {user}\n" in item:
                    item = item.strip("\n")
                    print(f"{item}\n{'-' * 120}")


# ====Login Section====

# Call function user_dictionary to update the list of users.
user_list = user_dictionary()

# Print welcome message and instructions.
print("\nWelcome to your business' Task Management application!"
      "\nPlease login to access your options.\n")

# Call login function and return the username of the current user.
current_user = user_login(user_list)

# Print menu and ask user to select an option.
while True:

    # Check user's privileges. If user is admin, show them the full menu.
    # Otherwise, show the user a menu without the option to register new users.
    if "admin" in current_user:
        menu = input("\nSelect one of the following Options below: "
                     "\n\t\tr\t-\tRegistering a user"
                     "\n\t\ta\t-\tAdding a task "
                     "\n\t\tva\t-\tView all tasks "
                     "\n\t\tvm\t-\tView my task"
                     "\n\t\tgr\t-\tGenerate reports"
                     "\n\t\tvs\t-\tView statistics"
                     "\n\t\tus\t-\tUser statistics"
                     "\n\t\te\t-\tExit"
                     "\n").lower()

    else:
        menu = input("\nSelect one of the following Options below: "
                     "\n\t\ta\t-\tAdding a task "
                     "\n\t\tva\t-\tView all tasks "
                     "\n\t\tvm\t-\tView my task "
                     "\n\t\te\t-\tExit"
                     "\n").lower()

    # If user selects 'r' and they are 'admin' start the process to register a new user.
    if menu == 'r' and "admin" in current_user:

        # Call function reg_user.
        reg_user()

    # If user selects 'gr' and they are 'admin' show them the total number of tasks and the total number of users.
    elif menu == 'gr' and "admin" in current_user:

        # Call functions to generate reports and let the user know when they have been generated successfully.
        task_overview()
        print("\nThe Task Overview Report has been successfully generated.")
        user_overview()
        print("\nThe User Overview Report has been successfully generated.")

    # If user selects 'ds' and they are 'admin' show them the total number of tasks and the total number of users.
    elif menu == 'vs' and "admin" in current_user:

        # Call function to show statistics from the reports.
        display_statistics()

    # If user selects 'us' and they are 'admin' show them the statistics for one or more selected users.
    elif menu == 'us' and "admin" in current_user:

        # Call function to show statistics from the reports.
        user_statistics()

    # If user selects 'a' start the process to insert a new line in the tasks file.
    elif menu == 'a':

        # Call function user_dictionary to update the list of users.
        user_list = user_dictionary()

        # Ask user to enter the username of the person to whom the task will be assigned and check that username exists.
        user_task = input("\nPlease enter the user name of the person you want to assign a task to: ")
        while True:
            if user_task in user_list.keys():
                break
            else:
                user_task = input("Username not in the data base. Please enter a different user: ")

        # Call function to add a new task.
        add_task(user_task)

    # If user selects 'va' display full list of tasks.
    elif menu == 'va':

        # Call function to view all the tasks on file.
        view_all()

    # If the user selects 'vm' display the tasks assigned to them in the task file.
    elif menu == 'vm':

        # Call function to view all the tasks assigned to the current user.
        my_tasks = view_mine(current_user)

        # Allow user to select a task.
        task_selection = input("\nIf you want to select a task please enter the task number (-1 to go to main menu): ")
        main_menu = False

        # Validate that the user has selected a task or -1 to exit.
        # If the user has selected a task within the list, check that the task is not complete and can be edited.
        while True:
            if task_selection == "-1":
                main_menu = True
                break
            elif task_selection not in my_tasks.keys():
                task_selection = input("Invalid selection. Please enter a task number or '-1' to go to main menu: ")
            else:
                if my_tasks[task_selection][5] == "Yes":
                    task_selection = input("This task is completed and can't be changed. Please select another task: ")
                else:
                    break

        # If user has selected -1 redirect them to the main menu.
        if main_menu:
            continue

        # Ask user to select an action from the menu.
        option = input(f"\nWhat action would you like to perform:"
                       f"\n\tc\t-\tmark the task as complete"
                       f"\n\te\t-\tedit task"
                       f"\n").lower()

        while True:

            # If the user has selected 'c' mark task as completed.
            if option == "c":
                my_tasks[task_selection][5] = "Yes"
                print(f"Task {task_selection} has been marked as completed.")
                break

            # If the user has selected 'e' ask them to choose between editing the user or the date of the task.
            elif option == "e":

                while True:
                    field_selection = input(f"\nWhat field would you like to change:"
                                            f"\n\tu\t-\tuser"
                                            f"\n\td\t-\tdue date"
                                            f"\n").lower()

                    # If the user selects 'u', ask them to enter a username.
                    # Verify that the user exists, if not ask the user to select another username.
                    if field_selection == "u":
                        changed_user = input("\nWhat user do you want to assign this task to?: ")
                        while True:
                            if changed_user not in user_dictionary().keys():
                                changed_user = input("User not in the database. Please enter a different username: ")
                            else:
                                break

                        # Verify the username entered is different to the one assigned to the task and change it.
                        # If it is the same, print the appropriate message.
                        if changed_user == my_tasks[task_selection][0]:
                            print(f"\nThis task is already assigned to {changed_user}.")
                            break
                        else:
                            my_tasks[task_selection][0] = changed_user
                            print(f"\nThis task has been assigned to {changed_user} successfully.")
                            break

                    # If the user selects option 'd'. Call the function to enter a due date.
                    # Change the date of the task and print a message alerting the user.
                    elif field_selection == "d":
                        date = date_entry()
                        my_tasks[task_selection][4] = date
                        print(f"\nThe due date for task {task_selection} has been changed to {date}.")
                        break

                    # If the user doesn't enter 'u' or 'd', print an error message and ask for a new selection.
                    else:
                        print("Invalid selection. Please enter 'u' or 'd': ")
                break

            # If user enters anything else that 'c' or 'e' ask them to enter a new selection.
            else:
                option = input("Invalid selection. Please enter 'c' or 'e': ")

        # Once the user's task have been updated, call the function to retrieve all tasks on file.
        # Then change all the information for the user's tasks.
        every_task = task_list()

        for value in my_tasks.values():
            for entry in every_task:
                if value[1] == entry[1] and value[2] == entry[2] and value[3] == entry[3]:
                    entry[0] = value[0]
                    entry[4] = value[4]
                    entry[5] = value[5]

        # Write the updated tasks in the task file, overwriting the previous information.
        with open("tasks.txt", "w") as file:
            for entry in every_task:
                file.write(f"{entry[0]}, {entry[1]}, {entry[2]}, {entry[3]}, {entry[4]}, {entry[5]}\n")

    # If the user selects 'e' exit the program.
    elif menu == 'e':
        print('\nGoodbye!')
        exit()

    else:
        print("\nYou have made a wrong choice. Please Try again.")
