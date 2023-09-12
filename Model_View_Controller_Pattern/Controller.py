from Model import Person
import View


def showAll():
    # gets list of all Person objects
    people_in_db = Person.getAll()
    # calls View
    return View.showAllView(people_in_db)


def start():
    View.startView()
    Input = input()
    if Input == 'y':
        return showAll()
    else:
        return View.endView()


if __name__ == "__main__":
    # running controller function
    start()
