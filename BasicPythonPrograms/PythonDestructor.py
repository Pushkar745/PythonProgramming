class Employee:
    #Initializaing
    def __init__(self):
        print('Employee created ')

        #Deleting (Calling destructor)
        def __del__(self):
            print('Destructor called,Employee deleted')
obj=Employee()
del obj            