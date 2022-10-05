# from xml.etree import ElementTree
# import csv
#
# # PARSE XML
# xml = ElementTree.parse("DLTINS_20210117_01of01.xml")
#
# # CREATE CSV FILE
# csvfile = open("data.csv", 'w', encoding='utf-8')
# csvfile_writer = csv.writer(csvfile)
#
# # ADD THE HEADER TO CSV FILE
# csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id", "FinInstrmGnlAttrbts.FullNm", "FinInstrmGnlAttrbts.ClssfctnTp","FinInstrmGnlAttrbts.CmmdtyDerivInd", "FinInstrmGnlAttrbts.NtnlCcy", "Issr"])
#
# # LOOP THROUGH THE XML FILE AND ADD THE DATA TO CSV FILE
# for node in xml.findall("TermntdRcrd"):
#     print(node.find("FinInstrmGnlAttrbts.Id").text)
#     Fin = node.find("FinInstrmGnlAttrbts")
#     id = Fin.find("Id").text
#     fullnm = Fin.find("FullNm").text
#     clssfctntp = Fin.find("ClssfctnTp").text
#     cmmdtyderivind = Fin.find("CmmdtyDerivInd").text
#     ntnlccy = Fin.find("NtnlCcy").text
#     issr = node.find("Issr").text
#     csvfile_writer.writerow([id, fullnm, clssfctntp, cmmdtyderivind, ntnlccy, issr])
#
# # CLOSE THE CSV FILE
# csvfile.close()


import xmltodict, csv
# import threading

# PARSE XML FILE
with open("/Users/rohansharma/Documents/PycharmProjects/intern15/DLTINS_20210117_01of01.xml") as xmlfile:
    xml = xmltodict.parse(xmlfile.read())
    # print(xml)
# CREATE CSV FILE
csvfile = open("data2.csv", 'w', encoding='utf-8')
csvfile_writer = csv.writer(csvfile)

# ADD HEADER
csvfile_writer.writerow(["FinInstrmGnlAttrbts.Id", "FinInstrmGnlAttrbts.FullNm", "FinInstrmGnlAttrbts.ClssfctnTp",
                         "FinInstrmGnlAttrbts.CmmdtyDerivInd", "FinInstrmGnlAttrbts.NtnlCcy", "Issr"])

# FOR EACH EMPLOYEE
for employee in xml['BizData']["Pyld"]["Document"]["FinInstrmRptgRefDataDltaRpt"]["FinInstrm"]:
    # EXTRACT EMPLOYEE DETAILS
    csv_line = [employee['TermntdRcrd']['FinInstrmGnlAttrbts']["Id"],
                employee['TermntdRcrd']['FinInstrmGnlAttrbts']["FullNm"],
                employee['TermntdRcrd']['FinInstrmGnlAttrbts']["ClssfctnTp"],
                employee['TermntdRcrd']['FinInstrmGnlAttrbts']["CmmdtyDerivInd"],
                employee['TermntdRcrd']['FinInstrmGnlAttrbts']["NtnlCcy"], employee['TermntdRcrd']["Issr"]]
    print(csv_line)
    # ADD A NEW ROW TO CSV FILE
    csvfile_writer.writerow(csv_line)