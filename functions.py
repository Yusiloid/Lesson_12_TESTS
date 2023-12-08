def hello_who(name):
    return f'Hello,{name}'

def salary(hours,salary_by_hour):
    '''
    Рассчет зп сотрудника
    :param hours: количество часов
    :param salary_by_hour: зарплата за час
    :return: итоговая сумма
    '''
    k = 2*1
    return hours * salary_by_hour* k