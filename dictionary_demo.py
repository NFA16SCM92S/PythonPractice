#like hash having key and a value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",


}

month = input("Enter month: ")
#print(monthConversions[month])
#or get the value of a key like below:
print(monthConversions.get(month, "Invalid key"))