from ics import Calendar, Event
from ics.grammar.parse import ContentLine
from datetime import datetime
import pandas as pd

# Read the Excel file
df = pd.read_excel("birthdays-excel.xlsx")

# Create a new calendar
cal = Calendar()

# Iterate over each row in the Excel table
for index, row in df.iterrows():
    name = row["Name"]
    birthdate = row["Birthday"]
    
    # Check if birthdate is not a datetime object
    if not isinstance(birthdate, datetime):
        # Try to parse the birthdate string to a datetime object
        try:
            birthdate = datetime.strptime(birthdate, "%d/%m/%Y")
        except ValueError:
            # If the above fails, it means the year is not provided
            # So we'll use the current year
            birthdate = datetime.strptime(f"{birthdate}/{datetime.now().year}", "%d/%m/%Y")
    
    # Create a new event for the birthday
    event = Event()
    
    # Set the event name based on the name
    if name.lower() == "me":
        event.name = "It's my birthday!"
    else:
        event.name = f"{name}'s birthday!"
    
    event.begin = birthdate
    event.make_all_day()

    # Make the event repeat annually
    event.extra.append(ContentLine(name="RRULE", value="FREQ=YEARLY"))
    
    # Add the event to the calendar
    cal.events.add(event)

# Save the calendar to an .ics file
with open("birthdays.ics", "w") as f:
    f.write(cal.serialize())