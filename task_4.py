employees = [
{"name": "Олена", "department": "Marketing", "salary":
25000},
{"name": "Ігор", "department": "IT", "salary": 55000},
{"name": "Наталія", "department": "Marketing", "salary":
28000},
{"name": "Олег", "department": "HR", "salary": 22000},
{"name": "Андрій", "department": "IT", "salary": 48000},
{"name": "Марія", "department": "IT", "salary": 52000},
]


def get_department_stats(employee_list, target_dept):

    filtered = []
    salary_sum = 0
    top_salary = 0
    top_earner = ""

    for employee in employee_list:

        if employee["department"] == target_dept:

            filtered.append(employee)

            salary_sum += employee["salary"]

            if employee["salary"] > top_salary:
                top_salary = employee["salary"]
                top_earner = employee["name"]

    average_salary = salary_sum / len(filtered)

    return {
        "department": target_dept,
        "average_salary": average_salary,
        "top_earner": top_earner,
        "count": len(filtered)
    }

print(get_department_stats(employees, "IT"))
print(get_department_stats(employees, "Marketing"))