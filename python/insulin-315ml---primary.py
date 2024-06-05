# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0601012D0BCAQA2","system":"bnf"},{"code":"0601012D0AABDBD","system":"bnf"},{"code":"0601012D0BCALAJ","system":"bnf"},{"code":"0601012V0BCAAAE","system":"bnf"},{"code":"0601012S0AAANAN","system":"bnf"},{"code":"0601012S0AAAMAM","system":"bnf"},{"code":"0601012D0BCANBE","system":"bnf"},{"code":"0601012D0BCAMBJ","system":"bnf"},{"code":"0601012S0BDAKAM","system":"bnf"},{"code":"0601011L0BBAAAA","system":"bnf"},{"code":"0601012D0AAA2A2","system":"bnf"},{"code":"0601011N0AAAUAU","system":"bnf"},{"code":"0601011R0AAACAC","system":"bnf"},{"code":"0601011R0BDAAAC","system":"bnf"},{"code":"0601011N0BCADAT","system":"bnf"},{"code":"0601012S0BCADAN","system":"bnf"},{"code":"0601012D0AABLBL","system":"bnf"},{"code":"0601012V0AAAEAE","system":"bnf"},{"code":"0601011N0AAATAT","system":"bnf"},{"code":"0601012D0AABJBJ","system":"bnf"},{"code":"0601011N0AAADAD","system":"bnf"},{"code":"0601012D0BCAPBL","system":"bnf"},{"code":"0601012S0BCAFAP","system":"bnf"},{"code":"0601012D0AABEBE","system":"bnf"},{"code":"0601011N0BCAFAU","system":"bnf"},{"code":"0601012S0AAAPAP","system":"bnf"},{"code":"0601011L0AAAAAA","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-315ml---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-315ml---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-315ml---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
