import prettytable
import re


def print_transactions(logfile):
    table = prettytable.PrettyTable(["Date", "Account", "Fund", "Status"])
    with open(logfile, "r") as f:
        for line in f.readlines():
            if "Adding" in line:
                date, status, msg = line.split(" - ")
                account = re.findall(r"\'([^\"]*)\'", msg)[0]
                fund = re.findall(r"\d+\.?\d*", msg)[0]
                status = "Failed" if status == "ERROR" else "SUCCEED"
                table.add_row([date, account, fund, status])
    print(table)
