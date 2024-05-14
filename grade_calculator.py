def calculate_average_grade():
    # Prompt the user for their name and store it in the student_name variable
    student_name = input('Enter Name: ')

    # Prompt the user for their scores in Math, Science, and English
    # Store the scores in the respective variables: math_score, science_score, english_score
    math_score = input("Enter Math Score: ")
    science_score = input("Enter Science Score: ")
    english_score = input("Enter English Score: ")
    try:                                                                            #for user errors
        ms = int(math_score)
        ss = int(science_score)
        es = int(english_score)
    except:
        print("Not a valid number. :(")
        quit()
    # Calculate the average grade
    average_grade = int((ms + ss + es) / 3)     #had to turn it back into an int(), I wonder that always happens when you sum because of the / . I wonder of sum() always gives back a int or float
   #maybe use round() ? Not sure if I should round up or down :o
    # Return the student's name and their average grade
    return student_name, average_grade

if __name__ == '__main__':                                  #tbh I still don't really know how this works. I think it lets you work in python environment that has this 'rule' in it. :shrug:
    # Call the calculate_average_grade function
    student_name, average_grade = calculate_average_grade()

    # Print the student's name and their average grade
    print(f"Student name: {student_name}")
    print(f"{student_name}'s average: {average_grade}")
    #Hope this was the right formatting.