def rank_employees(employee_salaries):
    salary_list = list()
    # change the dictionary into a list of tuples(key, value)
    
    # for (k, v) in employee_salaries.items():
    #     salary_list.append((k, v))

    # or by using list comprehension
    salary_list = [(k, v) for (k, v) in employee_salaries.items()]

    salary_list = sorted(salary_list, reverse=True, key=lambda each: each[1])
    salary_list = [i[0] for i in salary_list]
    return salary_list


print(rank_employees({'Alice': 50000, 'Bob': 45000, 'Eve': 50000}))