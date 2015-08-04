import csv

def open_file(filename):
    f = open(filename, 'r')
    t = csv.reader(f)
    text = []
    for i in t:
        text.append(i)
    f.close()
    return text










print open_file('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
