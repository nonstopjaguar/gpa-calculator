class gpacalculator():
    '''Declare the variables'''
    count = 0
    units   = 0
    coursecode = "coursecode"
    yearandterm = "yearandterm"
    numberofsubjects =0
    totalUnits = 0
    totalPoints = 0.0
    gpa = 0.0
    '''Prompt the user for the number of subjects taking per term'''
    yearandterm = input("Year and Term: ")
    numberofsubjects = int(input("Enter number of  subjects: "))

    '''use for to loop '''
    for count in range(count, numberofsubjects):
        '''This is to keep track of the number of subjects per term (Optional)'''
        print("For subject # ", count+1)

        '''Prompt user for course code'''
        coursecode = input("Course Code: ")

        '''Prompt user for number of number of units per class'''
        units = int(input("Number of Units: "))

        '''Prompt user to enter the grade'''
        grade = input("Enter the grade: ")

        '''Use if statement to check the grade and increment points and total units'''

        if grade == '4' or grade == '4.0':
            totalPoints = totalPoints + (units * 4)
            totalUnits = totalUnits + units
        elif grade == '3.5' or grade == '3.50':
            totalPoints += (units * 3.5)
            totalUnits += units
        elif grade == '3' or grade == '3.0':
            totalPoints += (units * 3.0)
            totalUnits += units
        elif grade == '2.5' or grade == '2.50':
            totalPoints += (units * 2.5)
            totalUnits += units
            
        elif grade == '2' or grade == '2.0':
            totalPoints += (units * 2.0)
            totalUnits += units

        elif grade == '1.5' or grade == '1.50':
            totalPoints += (units * 1.5)
            totalUnits += units

        elif grade == '1.0' or grade == '1.0':
            totalPoints += (units * 1.0)
            totalUnits += units
            '''If not 4, 3.5, 3, 2.5, 2, 1.5, 1 then it must be R.'''
            
        else:
            totalPoints += (units * 0.0)
            totalUnits += units
    '''Calculate GPA based on the total points and total units'''
    gpa = totalPoints / totalUnits
    print("Your General Point Average (GPA) is:", gpa)

def main():
    gpa = gpacalculator()

if __name__ == '__main__':main()
