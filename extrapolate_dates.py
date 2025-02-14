from datetime import datetime, timedelta

# Function to add days to a date and format the result
def add_days_and_format_compatible(start_date, days_to_add, time):
    new_date = start_date + timedelta(days=days_to_add)
    return new_date.strftime("%Y | %m | %d | ") + time

# Starting point
start_date = datetime(2023, 1, 12)
time_patterns = ["05:03:07", "16:54:46", "17:03:03", "16:54:46", "17:03:03", "04:55:00", "05:03:07", "04:55:00"]  # Observed time patterns
day_increments = [5, 13, 5, 7, 5, 13, 5, 7]  # Observed day increments

# Initialize the list of extrapolated entries
extrapolated_entries = []
current_time_pattern_index = 0
current_day_increment_index = 0

# Extrapolating with the corrected function
while start_date < datetime(2025, 9, 1):
    next_entry = add_days_and_format_compatible(
        start_date,
        day_increments[current_day_increment_index],
        time_patterns[current_time_pattern_index]
    )
    extrapolated_entries.append(next_entry)

    # Update the start date
    start_date += timedelta(days=day_increments[current_day_increment_index])

    # Rotate through the time patterns and day increments
    current_time_pattern_index = (current_time_pattern_index + 1) % len(time_patterns)
    current_day_increment_index = (current_day_increment_index + 1) % len(day_increments)


# Printing the extrapolated entries
for entry in extrapolated_entries:
    print(entry)