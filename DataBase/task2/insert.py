class INSERT:
    from values import insertValues
# initialization of the variables
    name= ""
    diffName= 0
    family = ""
    diffFamily= 0
    number = 0
    town = ""
    diffTown = ""
    gender = ''
    room = 0
    birth_date = ""
    score = 0.00

    #Calling of the class


    student = insertValues(name,diffName,family,diffFamily,number,town,diffTown,gender,room,birth_date,score)
    print(student)
    # THIS IS WHERE WE ADD TO DB