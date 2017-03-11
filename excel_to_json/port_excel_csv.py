import xlrd
import csv
from os import sys


def csv_from_excel(excel_file):
    workbook = xlrd.open_workbook(excel_file)
    all_worksheets = workbook.sheet_names()
    for worksheet_name in all_worksheets:
        if worksheet_name == "Enclosure Port Mapping 6125 E1":
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(
                ''.join(['/var/nfvShell/conf/hpe_nfvsys_6125_e1_portmap', '.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8")
                             for entry in worksheet.row_values(rownum)])
            your_csv_file.close()

        if worksheet_name == "Enclosure Port Mapping 6125 E2":
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(
                ''.join(['/var/nfvShell/conf/hpe_nfvsys_6125_e2_portmap', '.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8")
                             for entry in worksheet.row_values(rownum)])
            your_csv_file.close()

        if worksheet_name == "Enclosure Port Mapping 5950":
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(
                ''.join(['/var/nfvShell/conf/hpe_nfvsys_5950_portmap', '.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8")
                             for entry in worksheet.row_values(rownum)])
            your_csv_file.close()

        if worksheet_name == "Port Mapping 5900":
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(
                ''.join(['/var/nfvShell/conf/hpe_nfvsys_5900_portmap', '.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8")
                             for entry in worksheet.row_values(rownum)])
            your_csv_file.close()

        if worksheet_name == "Rackmount Port Mapping 5950":
            worksheet = workbook.sheet_by_name(worksheet_name)
            your_csv_file = open(
                ''.join(['/var/nfvShell/conf/hpe_nfvsys_mstrr_5950_portmap', '.csv']), 'wb')
            wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

            for rownum in xrange(worksheet.nrows):
                wr.writerow([unicode(entry).encode("utf-8")
                             for entry in worksheet.row_values(rownum)])
            your_csv_file.close()

