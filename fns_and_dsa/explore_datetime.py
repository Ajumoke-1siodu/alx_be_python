from datetime import datetime, timedelta

def display_current_datetime():
        """Display the current date and time in YYYY-MM-DD HH:MM:SS format."""
            current_date = datetime.now()
                print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
                    return current_date

                def calculate_future_date(current_date):
                        """Ask user for number of days and display the future date.
                            Returns the formatted future date string.
                                """
                                    try:
                                                days_to_add = int(input("Enter the number of days to add to the current date: "))
                                                        future_date = current_date + timedelta(days=days_to_add)
                                                                formatted_future = future_date.strftime("%Y-%m-%d")
                                                                        print("Future date:", formatted_future)
                                                                                return formatted_future
                                                                                except ValueError:
                                                                                            print("Please enter a valid integer for the number of days.")
                                                                                                    return None

                                                                                                if __name__ == "__main__":
                                                                                                    current_date = display_current_datetime()
                                                                                                        calculate_future_date(current_date)
