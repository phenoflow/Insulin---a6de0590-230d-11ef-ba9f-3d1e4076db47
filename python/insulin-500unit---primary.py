# Caroline E Dale, Rohan Takhar, et al., 2024.

import sys, csv, re

codes = [{"code":"0601012D0BCAZAZ","system":"bnf"},{"code":"0601012S0BGAEAI","system":"bnf"},{"code":"0601011R0BEAAAE","system":"bnf"},{"code":"0601012Z0BBACAC","system":"bnf"},{"code":"0601012F0AAABAB","system":"bnf"},{"code":"0601012D0BGAIBX","system":"bnf"},{"code":"0601011A0AAACAC","system":"bnf"},{"code":"0601011L0BBACAC","system":"bnf"},{"code":"0601012D0BBAVBZ","system":"bnf"},{"code":"0601011L0BDABAB","system":"bnf"},{"code":"0601012D0BCAVBX","system":"bnf"},{"code":"0601011L0BDAAAG","system":"bnf"},{"code":"0601012D0BCARBZ","system":"bnf"},{"code":"0601012D0BBASBA","system":"bnf"},{"code":"0601012D0BBAUBZ","system":"bnf"},{"code":"0601012X0BBABAB","system":"bnf"},{"code":"0601012S0BGADAL","system":"bnf"},{"code":"0601012S0BIADAI","system":"bnf"},{"code":"0601012S0BCAHAT","system":"bnf"},{"code":"0601012Z0AAABAB","system":"bnf"},{"code":"0601011N0AAAPAP","system":"bnf"},{"code":"0601011N0BHADAP","system":"bnf"},{"code":"0601012Z0AAAAAA","system":"bnf"},{"code":"0601012V0BBACAD","system":"bnf"},{"code":"0601012F0AAADAD","system":"bnf"},{"code":"0601011N0BCAGAY","system":"bnf"},{"code":"0601012F0BBABAB","system":"bnf"},{"code":"0601011N0BCAHAZ","system":"bnf"},{"code":"0601011L0BBAFAF","system":"bnf"},{"code":"0601012V0AAAAAA","system":"bnf"},{"code":"0601012Z0AAACAC","system":"bnf"},{"code":"0601011L0BDACAC","system":"bnf"},{"code":"0601012D0BGAGBV","system":"bnf"},{"code":"0601012S0BIABAL","system":"bnf"},{"code":"0601012X0BBACAB","system":"bnf"},{"code":"0601012S0BDANAI","system":"bnf"},{"code":"0601011L0AAAFAF","system":"bnf"},{"code":"0601012V0BEAAAD","system":"bnf"},{"code":"0601012D0BCBCBU","system":"bnf"},{"code":"0601012S0BDAMAI","system":"bnf"},{"code":"0601011N0AAAYAY","system":"bnf"},{"code":"0601011N0AAAMAM","system":"bnf"},{"code":"0601012S0AAASAS","system":"bnf"},{"code":"0601012D0BGAJBW","system":"bnf"},{"code":"0601012S0AAATAT","system":"bnf"},{"code":"0601012D0BBARAZ","system":"bnf"},{"code":"0601012S0BDALAL","system":"bnf"},{"code":"0601012F0BBAFAC","system":"bnf"},{"code":"0601012D0BGADBS","system":"bnf"},{"code":"0601012D0BCBDBZ","system":"bnf"},{"code":"0601011L0BBAHAG","system":"bnf"},{"code":"0601012Z0BBAAAA","system":"bnf"},{"code":"0601012D0BGAFBU","system":"bnf"},{"code":"0601011L0AAAGAG","system":"bnf"},{"code":"0601011A0AAADAD","system":"bnf"},{"code":"0601012Z0BBABAB","system":"bnf"},{"code":"0601012W0AAAAAA","system":"bnf"},{"code":"0601012D0BCBABA","system":"bnf"},{"code":"0601012D0BCAYBI","system":"bnf"},{"code":"0601011N0AAAZAZ","system":"bnf"},{"code":"0601012S0BCAGAS","system":"bnf"},{"code":"0601012D0BCATA3","system":"bnf"},{"code":"0601011L0AAACAC","system":"bnf"},{"code":"0601012D0BCBBBK","system":"bnf"},{"code":"0601011A0AAABAB","system":"bnf"},{"code":"0601012V0BBAEAD","system":"bnf"},{"code":"0601012V0BBAAAA","system":"bnf"},{"code":"0601012S0AAALAL","system":"bnf"},{"code":"0601012F0BBACAC","system":"bnf"},{"code":"0601012S0BGAFAI","system":"bnf"},{"code":"0601012F0BBAAAA","system":"bnf"},{"code":"0601011R0AAAEAE","system":"bnf"},{"code":"0601012V0AAAFAF","system":"bnf"},{"code":"0601012D0BCAUBH","system":"bnf"},{"code":"0601012S0BIACAI","system":"bnf"},{"code":"0601012D0BGAHBW","system":"bnf"},{"code":"0601012D0BCASBQ","system":"bnf"},{"code":"0601011L0BBAGAF","system":"bnf"},{"code":"0601012F0BBAEAA","system":"bnf"},{"code":"0601012F0BBADAD","system":"bnf"},{"code":"0601012D0BGABBN","system":"bnf"},{"code":"0601012X0BBAAAA","system":"bnf"},{"code":"0601011L0BDADAF","system":"bnf"},{"code":"0601012V0AAADAD","system":"bnf"},{"code":"0601012D0AAAIAI","system":"bnf"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-500unit---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-500unit---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-500unit---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
