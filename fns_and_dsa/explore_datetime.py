# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
        """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
            current_date = datetime.now()  # save into variable
                print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
                    return current_date

                def calculate_future_date(current_date):
                        """Ask user for number of days and display the future date."""
                            try:
                                        days_to_add = int(input("Enter the number of days to add to the current date: "))
                                                future_date = current_date + timedel

