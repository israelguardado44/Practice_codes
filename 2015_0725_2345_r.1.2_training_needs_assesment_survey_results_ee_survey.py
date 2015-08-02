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
    frequency = 0
    proficiency = 0
    skill_dict = {}
    skill_dict['A Department'] = None
    skill_lst = create_skill_lst(filename)
    for i in skill_lst:
        skill_dict[i] = [frequency, proficiency]
    return sorted(skill_dict)

def response_lst(filename):
    response_lst = []
    text = set_up_file(filename)
    for i in text[2:]:
        x = i[9:]
        response_lst.append(x)
    return response_lst
       

def tally_results_by_dept(filename, department):
    skills = skills_dict(filename)
    skills['A Department'] = department
    responses = response_lst(filename)
    for i in responses:
        if department in i:
            for key in skills:
                if skills[key] == 'A Department':
                    pass
                else:
                    skills[key] = 

            















print tally_results_by_dept('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print response_lst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print skills_dict('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print create_skill_lst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print create_deptlst('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
#print set_up_file('2015_0725_2111_i.2_test_results_for_ee_tna_survey.csv')
