from datetime import datetime
import os

def generate_log(data):
  # TODO: Implement log generation logic

  # STEP 1: Validate input
  if not isinstance(data, list): # checks if input is a list
    raise ValueError("Data must be a list.") # stops function with an error message
  # Hint: Check if data is a list

  # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
  # Hint: Use datetime.now().strftime("%Y%m%d")
  today = datetime.now().strftime("%Y%m%d") # gets today's date in YYYYMMDD format
  filename = f"log_{today}.txt" # generates the filename using today's date

  # STEP 3: Write the log entries to a file using File I/O
  # Use a with open() block and write each line from the data list
  # Example: file.write(f"{entry}\n")
  with open(filename, 'w') as file: # creates a new log file using write mode
    for entry in data: # loops through each entry in list
      file.write(f"{entry}\n") # writes each entry to file with a new line

  # STEP 4: Print a confirmation message with the filename
  print(f"Log written to {filename}") # prints confirmation message with filename
  return filename

if __name__ == "__main__": # runs code only if script is executed directly
  log_data = [
    "User logged in",
    "User updated profile",
    "User logged out"
  ]

  generate_log(log_data)