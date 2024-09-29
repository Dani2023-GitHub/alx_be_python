from datetime import datetime, timedelta
current_date = None
def display_current_datetime():
    global current_date
    current_date = datetime.now()
    print("Current date and time: ",current_date.strftime("%Y-%m-%d %H:%M:%S"))


def calculate_future_date():
    date_to_add = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + timedelta(days = date_to_add)
    print(f'Future date: {future_date.strftime("%Y-%m-%d")}')
display_current_datetime()
calculate_future_date()
