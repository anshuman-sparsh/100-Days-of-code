# 🔹 4.
# Print today’s date and time using datetime.datetime.now() in this format: DD-MM-YYYY HH:MM




from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("Date: %d-%m-%Y, Time: %H:%M")
print(formatted_time)