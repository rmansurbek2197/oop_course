class Course:
    def __init__(self):
        self.students = []

    def enroll(self, name):
        if name not in self.students:
            self.students.append(name)

    def remove(self, name):
        if name in self.students:
            self.students.remove(name)

    def show(self):
        print("Students:")
        for s in self.students:
            print(s)


def menu():
    c = Course()

    while True:
        print("\n1.Enroll 2.Remove 3.Show 0.Exit")
        choice = input(">> ")

        if choice == "1":
            c.enroll(input("Name: "))
        elif choice == "2":
            c.remove(input("Name: "))
        elif choice == "3":
            c.show()
        elif choice == "0":
            break


if __name__ == "__main__":
    menu()
