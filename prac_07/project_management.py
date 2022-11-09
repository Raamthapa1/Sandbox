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


def filter_project():
    """Filter project by date"""
    pass


def add_project():
    """Add new project"""
    pass


def update_project():
    """Update project"""
    projects = load_project(PROJECT_FILE)
    project = load_project(PROJECT_FILE)
    for i, project in enumerate(project, 0):
        print(f'{i} {project}')
    project_number = int(input("Enter the number of project you want to update: "))
    print(f'{projects[project_number]}')
    new_percentage = int(input("New_percentage: "))
    projects[project_number].update(new_percentage)


def load_project(project_file):

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
            project_file = input("Please input the name of project file")
            load_project(project_file)
        elif choice == "S":
            pass
        elif choice == "D":
            projects = load_project(PROJECT_FILE)
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
            update_project()

        else:
            print('Invalid menu choice')
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Thank you for using custom-built project management software.")


if __name__ == '__main__':
    main()
