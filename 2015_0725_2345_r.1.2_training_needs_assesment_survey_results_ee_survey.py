##This is to organize the data collected from the tna survey from the tna survey from employees

def set_up_file(filename):
    new_lst = []
    text = open(filename, 'rU')
    text_lst = text.readlines()
    for i in text_lst:
        i = i.split(',')
        new_lst.append(i)
    return new_lst

def create_deptlst(filename):
    new_deptlst = []
    deptlst = []
    text = set_up_file(filename)
    for i in text[2:]:
        if i[9] in deptlst:
            pass
        else:
            deptlst.append(i[9])
    for i in deptlst:
        i = i.strip('"')
        new_deptlst.append(i)
    return new_deptlst








print create_deptlst('2015_0725_2111_i.2_test_results_for_ee_tna_surevey.cvs')
#print set_up_file('2015_0725_2111_i.2_test_results_for_ee_tna_surevey.cvs')
