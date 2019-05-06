def change_date(date, op, value):
    #Function para modificar uma data, adicionando ou removendo minutos
    if not is_valid_op(op):
        raise ValueError('Use only the following operators: - and +')
    
    # usado dicionario para armazenar as informacoes da data recebida
    # devido a organizacao e facilidade de acessar os dados
    data = get_data_from_date(date)
    value = abs(value)
    if op == '+':
        increment_date(data, value)
    else:
        decrement_date(data, value)
    
    return format_data_to_string(data)


def format_data_to_string(data):
    #Function para formatar um dict contendo as informacoes de uma data
    hours = data['minutes'] // 60
    minutes = data['minutes'] - hours * 60
    return '{:02d}/{:02d}/{:04d} {:02d}:{:02d}'.format(data['day'], data['month'], data['year'], hours, minutes)


def increment_date(data, value):
    #Function para incrementar um valor em uma data
    minutes_in_day = 1440
    while value > 0:
        minutes = data['minutes']
        # caso a adicao dos minutos seja maior que 1 dia
        if(minutes + value >= minutes_in_day):
            add_day(data)
            value = value - (minutes_in_day - minutes)
        # caso a adicao dos minutos acabe no mesmo dia
        else:
            data['minutes'] = minutes + value
            value = 0


def add_day(data):
    #Function para adicionar 1 dia na data
    data['minutes'] = 0
    new_day = data['day'] + 1
    # faz a verificacao de mudanca de mes
    if new_day > get_days_in_month(data['month']):
        new_day = 1
        add_month(data)
    
    data['day'] = new_day


def add_month(data):
    #Function para adicionar 1 mes na data
    new_month = data['month'] + 1
    # faz a verificacao de mudanca de ano
    if new_month > 12:
        new_month = 1
        add_year(data)
    
    data['month'] = new_month


def add_year(data):
    #Function para adicionar 1 ano na data
    data['year'] = data['year'] + 1


def decrement_date(data, value):
    #Function para decrementar 1 valor de uma dataS
    while value > 0:
        minutes = data['minutes']
        # caso o decremento dos minutos seja maior que 1 dia
        if(minutes - value < 0):
            decrement_day(data)
            value = value - minutes
        # caso o decremento dos minutos acabe no mesmo dia
        else:
            data['minutes'] = minutes - value
            value = 0


def decrement_day(data):
    #Function para decrementar 1 dia da data
    minutes_in_day = 1440
    data['minutes'] = minutes_in_day
    new_day = data['day'] - 1
    # verifica a mudanca de mes
    if new_day < 1:
        decrement_month(data)
        new_day = get_days_in_month(data['month'])
    
    data['day'] = new_day


def decrement_month(data):
    #Function para decrementar 1 mes da dataS
    new_month = data['month'] - 1
    # verifica a mudanca de ano
    if new_month < 1:
        new_month = 12
        decrement_year(data)
    
    data['month'] = new_month


def decrement_year(data):
    #Function para decrementar 1 ano da data
    data['year'] = data['year'] - 1 


def is_valid_op(op):
    #Function para verificar se uma operacao e valida
    return (op == '-' or op == '+')


def get_data_from_date(date):
    #Function para montar o dicionario que vai ser usado para manipular a data
    just_date, just_time = date.split(' ')
    day, month, year = just_date.split('/')
    hours, minutes = just_time.split(':')
    data = {
        'day': int(day),
        'month': int(month),
        'year': int(year),
        'minutes': (int(hours) * 60 + int(minutes)) 
    }
    return data


def print_dict(my_dict):
    #Function auxiliar para printar os dados do dicionario
    for k, v in my_dict.items():
        print(k, v)


def get_days_in_month(month):
    #Function para retornar a quantidade de dias em um determinado mes
    # utilizado dicionario, para evitar if/else ou switch
    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    return days_in_month[month]

