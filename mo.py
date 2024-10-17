#เมนูตัวเลือก
def menu():
    print("1. เพิ่มการใช้จ่าย")
    print("2. เพิ่มรายได้")
    print("3. ดูรายงาน")
    print("4. ออก")
    choice = input("เลือกตัวเลือก: ")
    return choice
#การนำเข้าข้อมูล
def add_expense(expenses):
    amount = float(input("กรุณากรอกจำนวนการใช้จ่าย: "))
    description = input("กรุณากรอกรายละเอียดการใช้จ่าย: ")
    expenses.append({'type': 'expense', 'amount': amount, 'description': description})
def add_income(incomes):
    amount = float(input("กรุณากรอกจำนวนรายได้: "))
    description = input("กรุณากรอกรายละเอียดรายได้: ")
    incomes.append({'type': 'income', 'amount': amount, 'description': description})
def add_expense(expenses):
    amount = float(input("กรุณากรอกจำนวนการใช้จ่าย: "))
    description = input("กรุณากรอกรายละเอียดการใช้จ่าย: ")
    expenses.append({'type': 'expense', 'amount': amount, 'description': description})
def add_income(incomes):
    amount = float(input("กรุณากรอกจำนวนรายได้: "))
    description = input("กรุณากรอกรายละเอียดรายได้: ")
    incomes.append({'type': 'income', 'amount': amount, 'description': description})
#ส่วนการคำนวณและเงื่อนไข
def calculate_balance(expenses, incomes):
    total_expenses = sum(item['amount'] for item in expenses)
    total_income = sum(item['amount'] for item in incomes)
    balance = total_income - total_expenses
    return balance
#ส่วนการแสดงผลลัพธ์
def display_report(expenses, incomes):
    print("\nรายงานการใช้จ่าย:")
    for expense in expenses:
        print(f"การใช้จ่าย: {expense['amount']} - {expense['description']}")
    
    print("\nรายงานรายได้:")
    for income in incomes:
        print(f"รายได้: {income['amount']} - {income['description']}")
    
    balance = calculate_balance(expenses, incomes)
    print(f"\nยอดคงเหลือ: {balance}")

