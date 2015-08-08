import csv

def open_file(filename):
    f = open(filename, 'r')
    t = csv.reader(f)
    text = []
    for i in t:
        text.append(i)
    f.close()
    return text

def switch_to_numbers(filename):
    text = open_file(filename)
    for i in text:
        for t in range(len(i)):
                if i[t] == 'Daily':
                    i[t] = 1
                elif i[t] == 'Often':
                    i[t] = 2
                elif i[t] == 'Occasionally':
                    i[t] = 3
                elif i[t] == 'Rarely/Never':
                    i[t] = 4
                elif i[t] == 'Extremely Proficient':
                    i[t] = 11
                elif i[t] == 'Very Proficient':
                    i[t] = 12
                elif i[t] == 'Proficient':
                    i[t] = 13
                elif i[t] == 'Somewhat Proficient':
                    i[t] = 14
                elif i[t] == 'Not Proficient':
                    i[t] = 15
                elif i[t] == '':
                    i[t] = 0
    return text

def make_skill_dict(filename):
    skill_lst = []
    text = open_file(filename)
    for i in text[1]:
        if '-' not in i:
            pass
        else:
            dash = i.find('-')
            skill = i[:dash]
            if skill in skill_lst:
                pass
            else:
                skill_lst.append(skill)
    skill_dict = dict.fromkeys(skill_lst, [0,0])
    return skill_dict

def tally_results_by_dept(filename, dept):
    responses = switch_to_numbers(filename)
    dept_response = []
    for i in responses:
        if dept in i:
            dept_response.append(i[10:])
    skill_dict = make_skill_dict(filename)
    for i in dept_response:
        t = 0
        for key in sorted(skill_dict):
            vlst = [i[t],i[t + 1]]
            skill_dict[key] = [x + y for x,y in zip(vlst, skill_dict[key])]
            t += 2
    return skill_dict






print tally_results_by_dept('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv', 'County Counsel')
#print make_skill_dict('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print switch_to_numbers('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print open_file('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
