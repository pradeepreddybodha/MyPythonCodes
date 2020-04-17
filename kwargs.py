def func_school(**kwargs):
    for i,j in kwargs.items():
        print(i,":",j," ", end = "")
    print()


func_school(name = "Pradeep", roll_no = "03671A0531", college = "JBIET", section = "CSE")
func_school(name = "Bheema", roll_no = "03671A0566", college = "KMC", section = "MBBS")


def func_list(li):
    for i in li:
        print(i, end = "")


li = [1, 4, 9, 16, 25]
func_list(li)