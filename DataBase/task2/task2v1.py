choice = input("What do you want to do (SELECT or INSERT): ")
choice = choice.lower()

if choice == "insert":
    from insert_v_1 import INSERT
