# Andrew Wong, awong827@usc.edu
# ITP 115, Spring 2020
# Lab 12-1


MAX_COURSES = 6


class Student(object):
    def __init__(self, studentName, studentID):
        self.name = studentName
        self.idNumber = studentID
        self.courses = list()

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getID(self):
        return self.idNumber

    def setID(self, newID):
        self.idNumber = newID

    def getCourses(self):
        return self.courses

    def getNumberOfCourses(self):
        return len(self.courses)

    def addCourse(self, course):
        if self.getNumberOfCourses() < MAX_COURSES:
            self.courses.append(course)
            return True
        else:
            return False


def printStudents(studentList):
    count = 1
    for student in studentList:
        print("\t" + str(count) + ")", student.getName())
        count += 1


def main():
    studentList = list()
    studentList.append(Student("Tiffany", 40))
    studentList.append(Student("Isaaca", 41))
    studentList.append(Student("Huy", 42))
    studentList.append(Student("Brandon", 43))

    print("Welcome to the student registration system!")
    stopRegister = False
    while not stopRegister:
        print("\nStudents:")
        printStudents(studentList)
        student = int(input("Select a student from the list (1-4): "))
        course = input("Enter the course the student is registering for: ")
        if studentList[student - 1].addCourse(course):
            print("Course registration successful.")
        else:
            print("Course registration unsuccessful.")
        option = input("Would you like to continue registering? (y/n): ").lower()
        if option == "n":
            stopRegister = True

    for student in studentList:
        print("Student: " + student.getName() + ", ID: " + str(student.getID()), end="")
        print(" enrolled in", student.getNumberOfCourses(), "courses:")
        for course in student.getCourses():
            print("\t-", course)


main()
