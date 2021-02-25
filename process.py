log_file = open("um-server-01.txt") # opens the text file named 'um-server-01.txt' and assigns it to log_file


def sales_reports(log_file):        # creating a function named sales_reports which takes in one argument: log_file
    for line in log_file:           # iterate through each line of the log_file. for each line:
        line = line.rstrip()        #   strip spaces from the beginning and end (?)
        day = line[0:3]             #   assign the first 3 characters of the line to the variable day (e.g. 'Sat')
        # if day == "Tue":            #   check if the day is tuesday ('Tue')
        #     print(line)             #       if the day is tuesday, print that log entry
        if day == "Mon":            #   check if the day is monday ('Mon')
            print(line)             #       if the day is monday, print that log entry


sales_reports(log_file)             # call the function to execute the code
