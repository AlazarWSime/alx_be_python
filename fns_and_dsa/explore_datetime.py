from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    formated_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time is : {formated_date}")
    return current_date

def calculate_future_days(days):
     current_date = datetime.now()
     future_time = current_date + timedelta(days=days)
     formatted_future = current_date.strftime("%Y-%m-%d")
     print(f"Fututre date {formatted_future}")
     return future_time

def main():
  display_current_datetime()
  days = int(input("Enter the number of days to add to the current date: "))
  calculate_future_days(days)


if __name__=="__main__":
 main()