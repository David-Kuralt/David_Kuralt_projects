import csv
from io import TextIOWrapper
from zipfile import ZipFile

serList = [] #for tracking serial numbers

with open("harddrive_end_status", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["date", "serial_number", "model", "fail_status", \
        "hours_running", "smart_5", "smart_187", "smart_188", "smart_197", \
        "smart_198"])
    with ZipFile("data_Q3_2020.zip") as zf:
        fileList = ZipFile.namelist(zf)
        n = len(fileList)
        for i in range(n):
            with zf.open(fileList[n-1-i], "r") as infile:
                reader = csv.reader(TextIOWrapper(infile))
                for j in reader:
                    if j[2] == "ST12000NM0008" or \
                            j[2] == "TOSHIBA MG07ACA14TA":
                        if j[1] not in serList:
                            serList.append(j[1])
                            writer.writerow([j[0], j[1], j[2], j[4], j[20], \
                            j[14], j[64], j[66], j[84], j[86]])

rest_files_list = ["data_Q2_2020.zip", "data_Q1_2020.zip", \
                    "data_Q4_2019.zip"]


with open("harddrive_end_status", "a", newline="") as file:
    for k in rest_files_list:
        writer = csv.writer(file)
        with ZipFile(k) as zf:
            fileList = ZipFile.namelist(zf)
            n = len(fileList)
            for i in range(n):
                with zf.open(fileList[n-1-i], "r") as infile:
                    reader = csv.reader(TextIOWrapper(infile))
                    for j in reader:
                        if j[2] == "ST12000NM0008" or \
                                j[2] == "TOSHIBA MG07ACA14TA":
                            if j[1] not in serList:
                                serList.append(j[1])
                                writer.writerow([j[0], j[1], j[2], j[4], j[20], \
                                j[14], j[64], j[66], j[84], j[86]])
