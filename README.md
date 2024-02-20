# Birthday Calendar Generator

This Python script reads a list of birthdays from an Excel file in the same repository and generates an .ics calendar file with an event for each birthday. The Excel file should contain your friends' names and their birthdays. The birthdays can be in either DD/MM/YYYY or DD/MM format. If you want to add your own birthday, use the name "me" - this will create an event titled "It's my birthday!".

## Installation

1. Clone this repository.
2. Install the necessary Python packages using pip:

\```bash
pip install -r requirements.txt
\```

## Usage

1. Update the Excel file with your friends' birthdays. Remember to use "me" as a name for your own birthday.
2. Run the Python script. This will create an .ics file in the same directory.
3. Push the .ics file to your GitHub repository. This will host the .ics file on GitHub.
4. On GitHub, navigate to the .ics file, click on it, and then click on RAW. This will provide a URL.
5. Use this URL in any calendar app (Outlook, Google, Proton, etc.) to add these dates to your calendar.

This way, you can keep your calendar updated with your friends' birthdays. Just update the Excel file and run the script again whenever there's a new birthday to add.