def get_even_list(list): 
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)
        else:
            pass
    return even_list

print(get_even_list([1,2,3,4,5,6,7]))

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_of_month(list):
    max_hours = 0
    employee_of_month = ''
    for employee, hour in list:
        if hour > max_hours:
            max_hours = hour
            employee_of_month = employee
        else:
            pass
    return (f'employee of month is {employee_of_month} with {max_hours}hours of working')

print(employee_of_month(work_hours))