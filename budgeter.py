import csv
import datetime

DATA_FILE = 'data.csv'
FIELDNAMES = ['date', 'transaction', 'amount', 'note']

def load_data():
  """Function which loads the data.csv file for use in budgeter.py"""
  
  # Opens data.csv as dctionary, for loop appends contents to import_list and then returns it
  with open(DATA_FILE, newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    import_list = [(row) for row in reader]

  return import_list

def view_previous_entries(entries):
  """Function to display previous entries in budgeter.py"""
  # For loop to iterate through load_data's return value (list of dicts)
  for entry in entries:
    # F string formatted to ensure continuity of print statement
    print(f"\n{entry['date']:<10}{entry['transaction']:^11}{'$' + entry['amount']:^10}{entry['note']:>5}")
  
def display_profit_loss(entries):
  """Function to display profit loss in budgeter.py"""
  # Sets variables for use in function
  entry = entries
  income_total = 0
  expense_total = 0
  # For loop which iterates through entry, updating income_total and expense_total accordingly
  for value in entry:
    if value['transaction'] == 'Income':
      income_total += int(value['amount'])
    elif value['transaction'] == 'Expense':
      expense_total += int(value['amount'])
  # Final calculation and print statements for the function
  loss_total = income_total - expense_total
  print(f"The total income is ${income_total}")
  print(f"The total expenses are ${expense_total}")
  print(f"The current profit is ${loss_total}")

def add_new_entry(entries):
  """Function to add new entries to data.csv in budgeter.py"""
  while True:
      # User input for transaction_date, validity of input checked via datetime module and try/except
      while True:
          transaction_date = input("Date of transaction (YYYY-MM-DD): ")
          try:
              year, month, day = transaction_date.split('-')
              datetime.datetime(int(year), int(month), int(day))
              break
          except ValueError:
              print("Invalid entry, please follow the YYYY-MM-DD format")
              continue
      # User input for income_expese, tryexcept with assertion to determine input validity
      while True:
          try:
              income_expense = input("Was this Income (Y/N): ")
              assert income_expense.lower() == 'y' or income_expense.lower() == 'n', "Invalid input"
              break
          except AssertionError as msg:
              print(msg)
              continue
      # User input for amount, try/except to determine if integer
      while True:
          amount = input("Amount: ")
          try:
              int(amount)
              break
          except ValueError:
              print("Input must be an integer")
              continue
      # User input for transaction_note, set to 100 character limit
      while True:
          try:
              transaction_note = input("Describe the transaction: ")
              assert len(transaction_note) <= 100, "Too many characters, keep character count under 100"
              break
          except AssertionError as msg:
              print(msg)
              continue

      # Determines if income_expense is income or expense, then changes the variable for proper input into the .csv file
      income_expense = 'Income' if income_expense.lower() == 'y' else 'Expense'
      break
  
  # Takes all of the user inputs, appends it to entries, then appends the file so it shows proper amount
  # when called again.      
  user_input = {'date': transaction_date, 'transaction': income_expense, 'amount': amount, 'note': transaction_note}
  entries.append(user_input)
  with open(DATA_FILE, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, FIELDNAMES)
    writer.writerow(user_input)

# ===========================================
# =    Budgeter "interface" below           =
# ===========================================

def get_menu_choice():
  choice = None
  
  while not(choice) and choice != 0:
    try:
      choice = int(input('> '))
    except ValueError as err:
      print('That was not a valid entry, please try again!')
      continue

  if choice < 1 or choice > 5:
    print('That was not a valid choice, please try again!')
    choice = None

  return choice

def print_menu():
  print('\nWhat would you like to do?\n')
  print('1) View previous entries')
  print('2) Display the current profit/loss')
  print('3) Add a new entry')
  print('4) Exit\n')

def main():
  print('====================')
  print('Welcome to Budgeter!')
  print('====================')

  entries = load_data()

  while True:
    print_menu()
    menu_choice = get_menu_choice()

    if menu_choice == 1:
      view_previous_entries(entries)
    elif menu_choice == 2:
      display_profit_loss(entries)
    elif menu_choice == 3:
      add_new_entry(entries)
    elif menu_choice == 4:
      break

main()
