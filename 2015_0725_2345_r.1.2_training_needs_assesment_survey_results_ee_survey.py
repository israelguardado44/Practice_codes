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

def create_skill_lst(filename):
    skill_lst = []
    new_text = []
    text = set_up_file(filename)
    for i in text[1][10:]:
        new_text.append(i)
    for x in new_text:
        dash = x.find('-')
        skill = x[:dash]
        skill = skill.strip('"')
        if skill in skill_lst:
            pass
        else:
            skill_lst.append(skill)
    return skill_lst

def skills_dict(filename):
    skill_dict = {}
    skill_lst = create_skill_lst(filename)
    skill_dict['A Department'] = None
    for i in skill_lst:
        skill_dict[i] = None
    return skill_dict

def response_lst(filename):
    response_lst = []
    text = set_up_file(filename)
    for i in text[2:]:
        x = i[9:]
        response_lst.append(x)
    return response_lst
       

def switch_to_numbers(filename):
    i = 0
    x = 0
    resp_lst = response_lst(filename)
    for y in resp_lst:
        x = 0
        for item in y:
            if resp_lst[i][x] == 'Daily':
                resp_lst[i][x] = 1
            elif resp_lst[i][x] == 'Often':
                resp_lst[i][x] = 2
            elif resp_lst[i][x] == 'Occasionally':
                resp_lst[i][x] = 3
            elif resp_lst[i][x] == 'Rarely/Never':
                resp_lst[i][x] = 4
            elif resp_lst[i][x] == 'Extremely Proficient' or resp_lst[i][x] == 'Extremely Proficient\n':
                resp_lst[i][x] = 11
            elif resp_lst[i][x] == 'Very Proficient' or resp_lst[i][x] == 'Very Proficient\n':
                resp_lst[i][x] = 12
            elif resp_lst[i][x] == 'Proficient' or resp_lst[i][x] == 'Proficient\n':
                resp_lst[i][x] = 13
            elif resp_lst[i][x] == 'Somewhat Proficient' or resp_lst[i][x] == 'Somewhat Proficient\n':
                resp_lst[i][x] = 14
            elif resp_lst[i][x] == 'Not Proficient' or resp_lst[i][x] == 'Not Proficient\n':
                resp_lst[i][x] = 15
            x += 1
        i += 1
    return resp_lst

def tally_dept_results(filename, department):
    skills = skills_dict(filename)
    response = switch_to_numbers(filename)
    skills['A Department'] = department
    for i in sorted(skills):
        x = 1
        y = 2
        for item in response:
            if department in item:
                if skills[i] == department:
                    pass
                elif skills[i] == [int, int]:
                    skills[i] = skills[i][0] + 1, skills[i][1] + 1
                else:
                    skills[i] = [item[x], item[y]]
                x = y + 1
                y = y + 2
            else:
                pass
    return skills













print tally_dept_results('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv', 'County Counsel')
#print switch_to_numbers('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print response_lst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print skills_dict('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print create_skill_lst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print create_deptlst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
