from project import Project

# constants
PROJECT_FILE = 'projects.txt'
MENU = """Menu:
(L)oad projects
(S)ave projects 
(D)isplay projects
(F)ilter projects by date
(A)dd new project 
(U)pdate project
(Q)uit"""


def load_project():
    project_file = 'projects.txt'
    """Read file project details, return a list of project"""
    projects = []
    # Open the file for reading
    in_file = open(project_file, 'r')

    # File format is like: Name	Start Date	Priority	Cost Estimate	Completion Percentage
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()

    # All other lines are language data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split('\t')

        # priority should be an int
        # estimate should be a float
        # completion should be an int

        project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))

        # Add the project we've just made to the list
        projects.append(project)

    # Close the file as soon as we've finished reading it
    in_file.close()

    return projects


def main():
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            projects = load_project()
            print("Incomplete project: ")
            for project in projects:
                if not project.is_complete():
                    print(project)
            print("Completed projects: ")
            for project in projects:
                if project.is_complete():
                    print(project)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass

        else:
            print('Invalid menu choice')
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("byee")


if __name__ == '__main__':
    main()
