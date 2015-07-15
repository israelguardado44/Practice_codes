##this is a program code to create and organize the date of the respondents

def set_up_file(filename):
    new_lst =[]
    File = open(filename, 'rU')
    text_lst = File.readlines()
    for i in text_lst:
        i = i.split(',')
        new_lst.append(i)
    return new_lst

def create_dict(filename):
    dict_lst = []
    text = set_up_file(filename)
    for i in text:
        person = {}
        person['id'] = i[0]
        person['dept'] = i[1]
        person['responses'] = i[2:]
        dict_lst.append(person)
    return dict_lst
        
def give_dept_totals(filename, dept):       ##returns list of named depts
    dept_lst = []
    dict_lst = create_dict(filename)
    for dic in dict_lst:
        if dic['dept'] == dept:
           dept_lst.append(dic)
    return dept_lst

def last(dic):
    return dic[-1]

def gives_totals_by_department(filename, dept):
    counts = {}
    dept_lst = give_dept_totals(filename, dept)
    for dic in dept_lst:
        for i in dic['responses']:
            if i == '' or i == '\n':
                pass
            elif i in counts.keys():
                counts[i] += 1
            elif i not in counts.keys():
                counts.fromkeys(i)
                counts[i] = 1
    print dept
    for x in sorted(counts.items(), key=last):
        print x


print gives_totals_by_department('Sheet_1.csv', 'Social Sevices')
#print give_dept_totals('Sheet_1.csv', 'Sheriff')
#print create_dict('Sheet_1.csv')
#print set_up_file('Sheet_1.csv')
