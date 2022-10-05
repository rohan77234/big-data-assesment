# importing the necessary modules
import xmltodict
import csv

# lost data detection
lost_data = []

# PARSE XML FILE
with open("/Users/rohansharma/Documents/PycharmProjects/intern15/DLTINS_20210117_01of01.xml") as xmlfile:
    xml = xmltodict.parse(xmlfile.read())


# CREATE CSV FILE
csvfile = open("data2.csv", 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD HEADER
csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id", "FinInstrmGnlAttrbts.FullNm", "FinInstrmGnlAttrbts.ClssfctnTp",
                         "FinInstrmGnlAttrbts.CmmdtyDerivInd", "FinInstrmGnlAttrbts.NtnlCcy", "Issr"])

# count for lost data
count = 0

# LOOP THROUGH XML FILE AND ADD DATA TO CSV FILE where FinInstrmGnlAttrbts.Id is not null
for employee in xml['BizData']["Pyld"]["Document"]["FinInstrmRptgRefDataDltaRpt"]["FinInstrm"]:

    # try for KEYERROR detection
    try:
        csv_line = [employee['TermntdRcrd']['FinInstrmGnlAttrbts']["Id"],
                    employee['TermntdRcrd']['FinInstrmGnlAttrbts']["FullNm"],
                    employee['TermntdRcrd']['FinInstrmGnlAttrbts']["ClssfctnTp"],
                    employee['TermntdRcrd']['FinInstrmGnlAttrbts']["CmmdtyDerivInd"],
                    employee['TermntdRcrd']['FinInstrmGnlAttrbts']["NtnlCcy"],
                    employee['TermntdRcrd']["Issr"]]
    except:
        # if KEYERROR is detected, then add the data to lost_data list and continue
        lost_data.append(count)
        continue

    # printing every successful data
    print(csv_line)
    # incrementing count
    count += 1

    # ADD A NEW ROW TO CSV FILE
    csvfile_writer.writerow(csv_line)

# CLOSE CSV FILE
csvfile.close()

# PRINTING LOST DATA
print(len(lost_data))






