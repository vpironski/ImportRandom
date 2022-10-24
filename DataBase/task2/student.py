from datetime import date
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

            while True:
                self.name = input("Student's name: ")
                self.name = self.name.lower()
                self.name = self.name.capitalize()

                if len(self.name) > 15:
                    print("Error: Exeded limit ot characters")
                    continue
                elif len(self.name) < 15:
                    self.diffName = '_' * (15 - len(self.name))
                    break
                else:
                    break

            while True:
                self.family = input("Student's name: ")
                self.family = self.family.lower()
                self.family = self.family.capitalize()

                if len(self.family) > 20:
                    print("Error: Exeded limit ot characters")
                    continue
                elif len(self.family) < 20:
                    self.diffFamily = '_' * (20 - len(self.family))
                    break
                else:
                    break
            
            while True:
                self.number = int(input("Student's course number: "))
                check = str(self.number)

                if len(check) != 5:
                    print("Error: This is not a correct course number")
                    continue
                else:
                    break
            
            while True:
                self.town = input("Student's town: ")
                self.town = self.town.lower()
                self.town = self.town.capitalize()

                if len(self.town) > 20:
                    print("Error: Exeded limit ot characters")
                    continue
                elif len(self.town) < 20:
                    self.diffTown ='_' * (20 - len(self.town))
                    break
                else:
                    break

            while True:
                self.gender = input("The gender of the student is (m or f): ")

                if self.gender == 'm' or self.gender == 'f':
                    break
                else: 
                    print("Error: You have enter the wrong input for gender")
                    continue

            while True:
                self.room = int(input("Student's room: "))
                check = str(self.room)

                if len(check) != 3:
                    print("Error: This is an invalid room number")
                    continue
                else:
                    break

            while True:
                try:
                    date_comp = input("Student's birth date ('YYYY-MM-DD'): ")
                    year, mounth, day = map(int, date_comp.split('-'))
                    self.birth_date = date(year, mounth, day)  
                except ValueError:
                    print("Error: Invalid date value (must be yyyy-mm-dd)")
                    continue
                else:
                    break 

            while True:
                self.score = float(input("Student's score: "))
                check = str(self.score)
                if self.score > 6 or self.score < 2:
                    print("Error: This is an incorrect grade")

                if len(check) > 4:
                    print("Error: This is an incorrect grade")
                    continue
                else:
                    break

            '''Organises the values of the student into a line'''
            return f"{self.name}{self.diffName}{self.family}{self.diffFamily}{self.number}_{self.town}{self.diffTown}{self.gender}_{self.room}_{self.birth_date}_{self.score}"

