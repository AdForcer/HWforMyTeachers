class Worker():
    def __init__(self, ID, name, surname, age):
        self.ID = ID
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f'\nID: {self.ID}\n Name: {self.name} {self.surname}\n Age: {self.age}'
    
def startUp(path):
    Workers = []
    File = open(path,'r')
    Workers_amount = int(File.readline()[16:])
    kostil = File.readline()
    for _ in range(Workers_amount):
        ID = int(File.readline()[4:])
        fName = File.readline()[7:]
        fName = fName[:-1]
        Age = int(File.readline()[6:])
        name = ''
        surname = ''
        nameisfull = False
        for j in range(len(fName)):
            if fName[j] != ' ' and nameisfull == False:
                name += fName[j]
            else:
                nameisfull = True
            if nameisfull == True:
                surname += fName[j]
        Workers.append(Worker(ID, name, surname[1:], Age))
    return Workers

def PrintWorkersByAge(Workers,age):
    Founded_Workers = []
    for i in range(len(Workers)):
        if Workers[i].age == age:
            print(Workers[i])
            Founded_Workers.append(Workers[i])
    return Founded_Workers

def FindWorkerBySurname(Workers, surname):
    Founded_Workers = []
    for i in range(len(Workers)):
        if Workers[i].surname == surname:
            print(Workers[i])
            Founded_Workers.append(Workers[i])
    return Founded_Workers

def PrintWorkersByFirstLetterOfSurname(Workers, Letter):
    Founded_Workers = []
    for i in range(len(Workers)):
        if (Workers[i].surname)[0] == Letter:
            print(Workers[i])
            Founded_Workers.append(Workers[i])
    return Founded_Workers

def SaveFoundedInfo(tmp,path):
    File = open(path, 'w')
    for i in range(len(tmp)):
        File.write(str(tmp[i]))
    File.close()
    
def SaveWorkers(Workers,path):
    File = open(path,'w')
    File.write(f'Workers amount: {len(Workers)}\n')
    for i in range(len(Workers)):
        File.write(str(Workers[i]))
    File.close()
    
def PrintAllWorkers(Workers):
    for i in range(len(Workers)):
        print(Workers[i])

def EditWorkerByID(Workers,ID, Name, Surname, age):
    tmp_id = 0
    for i in range(len(Workers)):
        if Workers[i].ID == ID:
            tmp_id == i
            break
    Workers[tmp_id] = Worker(ID, Name, Surname, age)
    
def NewWorker(Workers,ID, Name, Surname, age):
    tmp_id = 0
    Workers.append(Worker(ID, Name, Surname, age))

def Menu(Workers,path):
    buffer = ''
    while True:
        print('1. Print All Workers\n2. Print workers by first letter of their surnames')
        print('3. Find workers by surname\n4. Print workers by age\n5. Save founded info\n6. Save workers')
        print('7. Edit worker info\n8. Delete worker\n9. New Worker\nIf you want to exit type something thats is not on the list')
        choice = int(input())
        if choice <=0 or choice > 9:
            return Workers
        else:
            match choice:
                case 1:
                    PrintAllWorkers(Workers)
                case 2:
                    letter = input('\n')
                    buffer = PrintWorkersByFirstLetterOfSurname(Workers, letter)
                case 3:
                    surname = input('\n')
                    buffer = FindWorkerBySurname(Workers,surname)
                case 4:
                    age = int(input('\n'))
                    buffer = PrintWorkersByAge(Workers, age)
                case 5:
                    yorn = input('Path by default: y or n\n')
                    if yorn == 'n':
                        thepath = input('Enter path\n')
                        filename = input('File name is...\n')
                    else:
                        thepath = 'Files'
                        filename = input('File name is...\n')
                    SaveFoundedInfo(buffer,f'{thepath}\{filename}.txt')
                case 6:
                    SaveWorkers(Workers,path)
                case 7:
                    ID = int(input('New ID\n'))
                    Name = input('New name\n')
                    Surname = input('New surname\n')
                    Age = int(input('New age\n'))
                    EditWorkerByID(Workers,ID,Name,Surname,Age)
                case 8:
                    i = int(input('ID\n'))
                    for z in range(len(Workers)):
                        if Workers[z].ID == i:
                            Workers.remove(Workers[z])
                            break
                case 9:
                    ID = int(input('ID\n'))
                    Name = input('New Name\n')
                    Surname = input('Surname\n')
                    Age = int(input('Age\n'))
                    NewWorker(Workers,ID,Name,Surname,Age)
            print()
                    
    
def Main():
    choice = input('Should I use path by default:\ny or n\n')
    if choice == 'y':
        path = 'Files\Workes.txt'
        Workers = startUp(path)
    else:
        path = input('Path:\n')
        Workers = startUp(path)
    Workers = Menu(Workers,path)
    SaveWorkers(Workers,path)
    return 0  

Main()


