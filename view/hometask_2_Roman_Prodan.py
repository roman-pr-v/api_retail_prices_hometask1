import csv

SYS_LOG_FILE = "D:\\Work\\work_folder\\PythonWorkshop\\syslog"
MY_SYSLOG_FILE = "D:\\Work\\work_folder\\PythonWorkshop\\my_syslog_file.csv"

with open(SYS_LOG_FILE, "r", encoding="utf8") as syslog_file, open(MY_SYSLOG_FILE, "w", newline='') as csv_file:
    lines = syslog_file.readlines()
    MY_TYPE_SOURCE: str = "WARNING kernel"
    for string in lines:
        if MY_TYPE_SOURCE in string:
            date_colum = string.split(',')[0]
            message_colum = string.split(':')[3:]
            writer = csv.writer(csv_file)
            writer.writerow([date_colum, message_colum])

            COLUM1 = "Colum_1: {date}".format(date=date_colum)
            COLUM2 = "Colum_2: {message}".format(message=message_colum)
            print(COLUM1 + ", " + COLUM2)
