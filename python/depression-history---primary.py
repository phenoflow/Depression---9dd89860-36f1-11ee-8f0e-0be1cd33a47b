# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"101054.0","system":"med"},{"code":"101153.0","system":"med"},{"code":"12122.0","system":"med"},{"code":"12399.0","system":"med"},{"code":"19439.0","system":"med"},{"code":"22116.0","system":"med"},{"code":"2716.0","system":"med"},{"code":"30405.0","system":"med"},{"code":"30483.0","system":"med"},{"code":"30583.0","system":"med"},{"code":"32841.0","system":"med"},{"code":"42931.0","system":"med"},{"code":"44848.0","system":"med"},{"code":"51258.0","system":"med"},{"code":"55384.0","system":"med"},{"code":"57409.0","system":"med"},{"code":"65435.0","system":"med"},{"code":"71009.0","system":"med"},{"code":"72966.0","system":"med"},{"code":"85852.0","system":"med"},{"code":"88644.0","system":"med"},{"code":"91105.0","system":"med"},{"code":"96995.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('depression-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["depression-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["depression-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["depression-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
