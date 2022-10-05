def xml_to_csv(filepath):
    import xmltodict, csv
    import threading

    # PARSE XML FILE
    with open(filepath) as xmlfile:
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