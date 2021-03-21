#imported datetime to get current date and time
import datetime;

#created variable currentTime and used "now" to get the current time
currentTime = datetime.datetime.now();

#printing out the date and time to the terminal
print("The date on the VM is: ");
print (currentTime.month, "/", currentTime.day, "/", currentTime.year )

print("The time on the VM is: ");
print(currentTime.hour, ":", currentTime.minute);