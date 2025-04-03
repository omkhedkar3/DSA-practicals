# Class Definition (hashtable)
class Hashtable:
    def __init__(self):  # corrected constructor
        self.m = int(input("Enter size of hash table: "))  # size of the hash table
        self.hashTable = [None] * self.m  # Initializes the hash table
        self.elecount = 0
        self.comparisons = 0  # The number of comparisons made during insertion or searching
        print(self.hashTable)  # Prints the initial empty hash table

    # Hash Function
    def hashFunction(self, key):
        return key % self.m

    # Check if the table is full
    def isfull(self):
        return self.elecount == self.m

    # Linear Probing Insert Method
    def linearprobr(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        while self.hashTable[index] is not None:  # Collision detected
            index = (index + 1) % self.m  # Linear probing
            compare += 1
        self.hashTable[index] = [key, data]  # Insert data
        self.elecount += 1  # Increment element count
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Linear Probing Search Method
    def getlinear(self, key):
        index = self.hashFunction(key)
        while self.hashTable[index] is not None:  # Traverse to find the key
            if self.hashTable[index][0] == key:  # Check if the key matches
                return index
            index = (index + 1) % self.m  # Linear step
        return None  # Key not found

    # Quadratic Probing Insert Method
    def quadraticprobr(self, key, data):
        index = self.hashFunction(key)
        compare = 0
        i = 0
        while self.hashTable[index] is not None:  # Collision detected
            i += 1
            index = (index + i * i) % self.m  # Quadratic probing
            compare += 1
        self.hashTable[index] = [key, data]  # Insert data
        self.elecount += 1  # Increment element count
        print(f"Data inserted at index {index}")
        print(self.hashTable)
        print(f"Number of comparisons: {compare}")

    # Quadratic Probing Search Method
    def getQuadratic(self, key):
        index = self.hashFunction(key)
        i = 0
        while self.hashTable[index] is not None:  # Traverse to find the key
            if self.hashTable[index][0] == key:  # Check if the key matches
                return index
            i += 1
            index = (index + i * i) % self.m  # Quadratic step
        return None  # Key not found

    # Insert Using Linear Probing
    def insertvialinear(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:  # No collision
            self.hashTable[index] = [key, data]  # Insert data
            self.elecount += 1  # Increment element count
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:  # Collision occurred
            print("Collision occurred, applying Linear probing")
            self.linearprobr(key, data)

    # Insert Using Quadratic Probing
    def insertviaQuadratic(self, key, data):
        if self.isfull():
            print("Table is full")
            return False
        index = self.hashFunction(key)
        if self.hashTable[index] is None:  # No collision
            self.hashTable[index] = [key, data]  # Insert data
            self.elecount += 1  # Increment element count
            print(f"Data inserted at index {index}")
            print(self.hashTable)
        else:  # Collision occurred
            print("Collision occurred, applying Quadratic probing")
            self.quadraticprobr(key, data)

# Menu Function
def menu():
    obj = Hashtable()  # Create an instance of the Hashtable

    while True:
        print("********")
        print("1. Linear Probe    *")
        print("2. Quadratic Probe  *")
        print("3. Exit")
        print("********")
        ch = int(input("Enter choice: "))

        if ch == 1:  # Linear Probing Mode
            while True:
                print("* Insert *")
                print("* Search *")
                print("* Exit *")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:  # Insert
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj.insertvialinear(a, b)
                elif ch2 == 2:  # Search
                    k = int(input("Enter key to be searched: "))
                    f = obj.getlinear(k)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")
                elif ch2 == 3:  # Exit
                    break

        elif ch == 2:  # Quadratic Probing Mode
            while True:
                print("* Insert *")
                print("* Search *")
                print("* Exit *")
                ch2 = int(input("Enter your choice: "))
                if ch2 == 1:  # Insert
                    a = int(input("Enter phone number: "))
                    b = str(input("Enter name: "))
                    obj.insertviaQuadratic(a, b)
                elif ch2 == 2:  # Search
                    k = int(input("Enter key to be searched: "))
                    f = obj.getQuadratic(k)
                    if f is None:
                        print("Key not found")
                    else:
                        print(f"Key found at index {f}")
                elif ch2 == 3:  # Exit
                    break

        elif ch == 3:  # Exit
            break

menu()
