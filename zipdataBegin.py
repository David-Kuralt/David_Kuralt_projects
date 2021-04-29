import csv
from io import TextIOWrapper
from zipfile import ZipFile

serList = [] #for tracking serial numbers

with open("harddrive_begin_status", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["start_date", "serial_number", "model"])
    with ZipFile("data_Q4_2019.zip") as zf:
        fileList = ZipFile.namelist(zf)
        for i in fileList:
            with zf.open(i, "r") as infile:
                reader = csv.reader(TextIOWrapper(infile))
                for row in reader:
                    if row[2] == "ST12000NM0008" or \
                            row[2] == "TOSHIBA MG07ACA14TA":
                        if row[1] not in serList:
                            serList.append(row[1])
                            writer.writerow([row[0], row[1], row[2]])


rest_files_list = ["data_Q1_2020.zip", "data_Q2_2020.zip", \
                    "data_Q3_2020.zip"]


with open("harddrive_begin_status", "a", newline="") as file:
    for j in rest_files_list:
        writer = csv.writer(file)
        with ZipFile(j) as zf:
            fileList = ZipFile.namelist(zf)
            for i in fileList:
                with zf.open(i, "r") as infile:
                    reader = csv.reader(TextIOWrapper(infile))
                    for row in reader:
                        if row[2] == "ST12000NM0008" or \
                                row[2] == "TOSHIBA MG07ACA14TA":
                            if row[1] not in serList:
                                serList.append(row[1])
                                writer.writerow([row[0], row[1], row[2]])
