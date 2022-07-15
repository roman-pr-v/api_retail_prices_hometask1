import csv

syslog_file = "D:\\Work\\work_folder\\PythonWorkshop\\syslog"
my_syslog_file = "D:\\Work\\work_folder\\PythonWorkshop\\my_syslog_file.csv"

with open(syslog_file, "r", encoding="utf8") as syslog_file, open(my_syslog_file, "w", newline='') as csv_file:
    lines = syslog_file.readlines()
    my_type_source = "WARNING kernel"
    for string in lines:
        if my_type_source in string:
            date_colum = string.split(',')[0]
            message_colum = string.split(':')[3:]
            writer = csv.writer(csv_file)
            writer.writerow([date_colum, message_colum])

            colum1 = "Colum_1: {date}".format(date=date_colum)
            colum2 = "Colum_2: {message}".format(message=message_colum)
            print(colum1 + ", " + colum2)
