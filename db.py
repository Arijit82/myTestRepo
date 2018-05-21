import pymongo
from pymongo import MongoClient

def main():
    while (1):
        # chossing option to do CRUD operations
        selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')

        if selection == '1':
            insert()
        elif selection == '2':
            update()
        elif selection == '3':
            read()
        elif selection == '4':
            delete()
        else:
            print('\n INVALID SELECTION \n')


# Function to insert data into mongo db
def insert():
    try:
        employeeId = input('Enter Employee id :')
        employeeName = input('Enter Name :')
        employeeAge = input('Enter age :')
        employeeCountry = input('Enter Country :')

        print(employeeId,employeeName,employeeAge,employeeCountry)
        db.Employees.insert_one(
            {
                "id": employeeId,
                "name": employeeName,
                "age": employeeAge,
                "country": employeeCountry
            })
        return (print('\nInserted data successfully\n'))

    except Exception as e:
        print(str(e))


client = MongoClient('localhost:27017')

db = client.EmployeeData

# function to read records from mongo db
def read():
        try:
            empCol = db.Employees.find()
            print ('\n All data from EmployeeData Database \n')
            for emp in empCol:
                return print (emp)

        except Exception as e:
                return (print (str(e)))


# Function to update record to mongo db
def update():
    try:
        criteria = input('\nEnter id to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        country = input('\nEnter country to update\n')

        db.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name": name,
                    "age": age,
                    "country": country
                }
            }
        )
        return (print("\nRecords updated successfully\n"))

    except Exception as e:
           return (print(str(e)))

# Function to delete record from mongo db
def delete():
    try:
        criteria = input('\nEnter employee id to delete\n')
        db.Employees.delete_many({"id":criteria})
        return (print ('\nDeletion successful\n'))
    except Exception as e:
        return (print (str(e)))

# if __name__ == '__main__':
main()
