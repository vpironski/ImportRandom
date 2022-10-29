import os


class CreateDatabase:

    def __init__(self, file_name):
        self.file_name = file_name

        # Creates the file
        # with open(file_name, 'w', encoding='utf-8') as f:
        #     print("The file has been created")
        #     pass

        if not os.path.exists(file_name):
            colons_count = int(input("How many rows will the db have: "))
            colums = []

            for i in range(colons_count):
                col = input("Input column (format name size or name|data type| ): ")
                colums.append(col)

            with open(file_name, 'w', encoding='utf-8') as f:
                for i in colums:
                    f.write(i + ',')
                    # f.write(',')
                f.write('!')
                print("the colums have been created !")
                pass
        else:
            print(f'{file_name} already exists')
