def main():
    name = input("Enter employee's name: ")
    hours = float(input("Enter number of hours worked in a week: "))
    hourly_pay_rate = float(input("Enter hourly pay rate: "))
    federal_tax = float(input("Federal tax withholding rate(e.g., 20% = 0.2): "))
    state_tax = float(input("Enter state tax withholding rate(e.g., 9% = 0.09): "))

    gross_pay = hourly_pay_rate * hours
    federal_deduction = gross_pay * federal_tax
    state_deduction = gross_pay * state_tax
    total_deduction = federal_deduction + state_deduction
    net_pay = gross_pay - total_deduction

    print(f"Employee Name: {name}")
    print(f"Hours Worked: {hours}")
    print(f"Pay Rate: ${hourly_pay_rate}")
    print(f"Gross Pay: ${gross_pay}")
    print(f"Deductions:")
    print(f"\tFederal Withholding ({federal_tax * 100}%): ${federal_deduction:.2f}")
    print(f"\tState Withholding ({state_tax * 100}%): ${state_deduction:.2f}")
    print(f"\tTotal Deduction: ${total_deduction:.2f}")
    print(f"Net Pay: ${net_pay:.2f}")

if __name__ == "__main__":
    main()

