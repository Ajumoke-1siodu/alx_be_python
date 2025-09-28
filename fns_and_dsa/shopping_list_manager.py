from datetime import datetime, timedelta

def main():
        # Step 1: Show current date and time
            current_date = datetime.now()
                print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

                    # Step 2: Ask user for number of days
                        try:
                                    days_to_add = int(input("Enter the number of days to add to the current date: "))
                                        except ValueError:
                                                    print("Invalid input. Please enter a number.")
                                                            return

                                                            # Step 3: Calculate future date
                                                                future_date = current_date + timedelta(days=days_to_add)
                                                                    print("Future date:", future_date.strftime("%Y-%m-%d"))

                                                                    if __name__ == "__main__":
                                                                            main()
