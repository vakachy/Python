
import view
import model

def program():
    while True:
        option = view.show_menu()
        employees = model.Get_employees()

        if option == 1:
            employee = view.Look_for_employee()
            result = model.Find_employee(employees, employee)
            view.Show_employee(result)

        if option == 2:
            criterion = view.Get_selection_criterion_for_occupation()
            result = model.Pick_employee(employees, criterion)
            view.Show_employee(result)

        if option == 3:
            criterion = view.Get_selection_criterion_for_salary()
            selection_1, selection_2 = model.Select_employee(employees, criterion)
            view.Show_employee_selection(selection_1, selection_2)

        if option == 4:
            employee = view.Addition_of_employee()
            model.Add_employee(employee)

        if option == 5:
            model.Remove_employee(employees)

        if option == 6:
            model.Update_employee(employees)

        if option == 7:
            model.write_json(employees,file_name= 'db.json')

        if option == 8:
            model.write_csv(employees,file_name= 'db.csv')

        if option == 9:
            break
# -------------------------------------------------------------------- #
