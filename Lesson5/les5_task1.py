# 1. Пользователь вводит данные о количестве предприятий, 
# их наименования и прибыль за четыре квартала для каждого предприятия. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
# Необходимо использовать модуль collections


from collections import defaultdict


def get_comp_data():
    count = int(input("Введите количество предприятий:" ))
    companies = defaultdict(list)
    for i in range(1, count+1):
        name = input("Название компании: ")
        for j in range(1, 5):
            comp_profit = float(input(f'Прибыль за {j}-й квартал: '))
            companies[name].append(comp_profit)
    print(companies)
    return companies


def avg_sum_profit(companies):
    avg_sum = 0
    for profit in companies.values():
        avg_sum += sum(profit)
    avg_sum  /= len(companies)
    return avg_sum

def below_above_avg(companies):
    avg_year_profit = avg_sum_profit(companies)
    below_above_dict = defaultdict(list)
    for company, profit in companies.items():
        if sum(profit) < avg_year_profit:
            below_above_dict["Below average profit"].append(company)
        elif sum(profit) > avg_year_profit:
            below_above_dict["Above average profit"].append(company)
        elif sum(profit) == avg_year_profit:
            below_above_dict["Equal average profit"].append(company)
    return below_above_dict

def test():

    test_data = {
        'company 1': [8.0, 3.5, 1.5, 3.0], 
        'company 2': [10.0, 0.0, 10.0, 10.0], 
        'company 3': [5.0, 5.0, 5.0, 5.0], 
        'company 4': [7.0, 0.0, 7.0, 0.0] 
        }
    test_result = {
        'Below average profit': ['company 1', 'company 4'], 
        'Above average profit': ['company 2'], 
        'Equal average profit': ['company 3']}

    assert avg_sum_profit(test_data) == 20
    assert below_above_avg(test_data) == test_result

    # Shows how program prints result 
    below_above_companies = below_above_avg(test_data)
    for key, value in below_above_companies.items():
        print(str(key))
        print(f'\t{", ".join(value)}')
    

def main():

    companies_data = get_comp_data()
    below_above_companies = below_above_avg(companies_data)
    for key, value in below_above_companies.items():
        print(str(key))
        print(f'\t{", ".join(value)}')

    # test()


if __name__ == "__main__":
    main()    
