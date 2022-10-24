from datetime import date
class INSERT:

    class Student:
        def __init__(self,name,diffName,family,diffFamily,number,town,diffTown,gender,room,birth_date,score):
            '''Gets fed the values of the student'''
            self.name = name
            self.diffName = diffName
            self.family = family
            self.diffFamily = diffFamily
            self.number = number
            self.town = town
            self.diffTown = diffTown
            self.gender = gender
            self.room = room
            self.birth_date = birth_date
            self.score = score

        def __str__(self):
            '''Organises the values of the student into a line'''
            return f"{self.name}{self.diffName}{self.family}{self.diffFamily}{self.number}_{self.town}{self.diffTown}{self.gender}_{self.room}_{self.birth_date}_{self.score}"


#Gets the first name of the student (Input of name)
    while True:
        name = input("Student's name: ")
        name = name.lower()
        name = name.capitalize()

        if len(name) > 15:
            print("Error: Exeded limit ot characters")
            continue
        elif len(name) < 15:
            diffName = '_' * (15 - len(name))
            break
        else:
            break


    #Gets the last name of the student (Input of family)
    while True:
        family = input("Student's family name: ")
        family = family.lower()
        family = family.capitalize()

        if len(family) > 20:
            print("Error: Exeded limit ot characters")
            continue
        elif len(family) < 20:
            diffFamily ='_' * (20 - len(family))
            break
        else:
            break
    

    #Gets the course number of the student (Input of number)
    while True:
        number = int(input("Student's course number: "))
        check = str(number)

        if len(check) != 5:
            print("Error: This is not a correct course number")
            continue
        else:
            break

    #Gets the town of the student (Input of town)
    while True:
        town = input("Student's town: ")
        town = town.lower()
        town = town.capitalize()

        if len(town) > 20:
            print("Error: Exeded limit ot characters")
            continue
        elif len(town) < 20:
            diffTown ='_' * (20 - len(town))
            break
        else:
            break

    #Gets the gender of the student (Input of student)
    while True:
        gender = input("The gender of the student is (m or f): ")

        if gender == 'm' or gender == 'f':
            break
        else: 
            print("Error: You have enter the wrong input for gender")
            continue

    #Gets the room of the student (Input of room)
    while True:
        room = int(input("Student's room: "))
        check = str(room)

        if len(check) != 3:
            print("Error: This is an invalid room number")
            continue
        else:
            break

    #Gets the birth date of the student (Input of birth date)
    while True:
        try:
            date_comp = input("Student's birth date ('YYYY-MM-DD'): ")
            year, mounth, day = map(int, date_comp.split('-'))
            birth_date = date(year, mounth, day)  
        except ValueError:
            print("Error: Invalid date value (must be yyyy-mm-dd)")
            continue
        else:
            break

    #Gets the score of the student (Input score)
    while True:
        score = float(input("Student's score: "))
        check = str(score)
        if score > 6 or score < 2:
            print("Error: This is an incorrect grade")

        if len(check) > 4:
            print("Error: This is an incorrect grade")
            continue
        else:
            break


    

    #Calling of the class
    student = Student(name,diffName,family,diffFamily,number,town,diffTown,gender,room,birth_date,score)
    print(student)

    # THIS IS WHERE WE ADD TO DB