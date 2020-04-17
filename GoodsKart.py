import os
import re

try:
    class Customer:
        def __init__(self, title, fst_name, Lst_name, black_list):
            self.title = title
            self.fst_name = fst_name
            self.last_name = lst_name
            self.black_list = black_list
            print("Title:", self.title, "First Name:", self.fst_name, "Last_name:", self.last_name, self.black_list)

        def createorder(self, blacklist):
            if blacklist == 1:
                raise "CustomerNotAllowedException"

    ab_path = os.path.dirname("D:/JetBrains/PycharmProjects/PythonforBeginners/CaseStudy3")
    rel_path = "CaseStudy3/FairDealCustomerData.csv"
    file ="".join([ab_path, '/', rel_path])
    file = open(file, 'r')
    i = 0
    name_list = []

    for customer_data in file:
        i += 1
        if i == 1:
            continue
        pattern = re.compile(r"([A-Za-z]+),\s([A-Za-z]+\.)\s([A-Za-z]+\s?[A-Za-z]*)\s,([0-9])")
        # print(customer_data)
        matches = pattern.finditer(customer_data)
        for match in matches:
            title = match.group(2)
            fst_name = match.group(1)
            lst_name = match.group(3)
            black_list = match.group(4)

        obj = Customer(title, fst_name, lst_name, black_list)
        obj.createorder(black_list)




finally:
    file.close()