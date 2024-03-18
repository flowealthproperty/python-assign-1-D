def read_steps_file(filename):
    """
    Read the steps data from the file and return it as a list of integers.
    """
    steps_data = []
    with open(filename, 'r') as file:
        for line in file:
            steps_data.append(int(line.strip()))
    return steps_data

def calculate_monthly_averages(steps_data):
    """
    Calculate the average number of steps taken for each month.
    """
    monthly_totals = [0] * 12  # Initialize a list to store total steps for each month
    monthly_days = [0] * 12  # Initialize a list to store the number of days in each month

    # Define the number of days in each month (assuming a non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Iterate through the steps data and accumulate total steps for each month
    for day, steps in enumerate(steps_data):
        month = day // sum(days_in_month[:day + 1])  # Determine the month based on the day
        monthly_totals[month] += steps
        monthly_days[month] += 1

    # Calculate the average steps for each month
    monthly_averages = [total / days if days > 0 else 0 for total, days in zip(monthly_totals, monthly_days)]
    return monthly_averages

def count_days_above_threshold(steps_data, threshold):
    """
    Count the number of days where steps taken exceed the threshold.
    """
    count = sum(1 for steps in steps_data if steps >= threshold)
    return count

def main():
    try:
        filename = "Steps.txt"
        steps_data = read_steps_file(filename)
        
        # Calculate and display the average number of steps taken for each month
        monthly_averages = calculate_monthly_averages(steps_data)
        print("Average number of steps taken for each month:")
        for month, average_steps in enumerate(monthly_averages, 1):
            print(f"Month {month}: {average_steps:.2f}")

        # Count and display the number of days with 10,000 or more steps
        threshold = 10000
        days_above_threshold = count_days_above_threshold(steps_data, threshold)
        print(f"\nNumber of days with {threshold} or more steps: {days_above_threshold}")

    except FileNotFoundError:
        print("Error: Steps file not found.")
    except ValueError:
        print("Error: Invalid data in Steps file.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
