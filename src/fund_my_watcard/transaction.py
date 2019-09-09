import prettytable
import re

def print_transaction(logfile):
    table = prettytable.PrettyTable(['Date', 'Account', 'Fund', 'Status'])
    f = open(logfile, 'r')
    for line in f:
        if line.__contains__('Adding'):
            l = line.split(" - ")
            date = l[0]
            account = re.findall(r"\'([^\"]*)\'",l[2])[0]
            fund = re.findall(r"\d+\.?\d*",l[2])[0]
            status = "Failed" if l[1]=="ERROR" else "SUCCEED"
            table.add_row([date, account, fund, status])
    f.close()
    print(table)
