print("Module Start")

def tax_calculator(annual_income):
    if annual_income <= 600000:
        taxable_income = 0
        tax = 0*taxable_income/100+0
    elif annual_income<=1200000:
        taxable_income = annual_income - 600000
        tax = 5*taxable_income/100 + 0
    elif annual_income<=1800000:
        taxable_income = annual_income -1200000
        tax = 10*taxable_income/100 + 30000
    elif annual_income > 1800000:
        taxable_income = annual_income -1800000
        tax = 10*taxable_income/100 + 90000
    return tax
    
def net_salary(gross):
    annual_income = gross*12
    net_salary = gross-tax_calculator(annual_income)/12
    return net_salary
    
print("Module End")