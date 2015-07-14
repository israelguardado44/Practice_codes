##this is a program code to create and organize the date of the respondents

def set_up_file(filename):
    new_lst =[]
    File = open(filename, 'rU')
    text_lst = File.readlines()
    for i in text_lst:
        i = i.split(',')
        new_lst.append(i)
    for i in new_lst:
        person = {}
        person['id'] = i[0]
        person['department'] = i[1]
        person['responses'] = i[2:]
        print person   

        








    ##match = re.findall(r'\w+\W*\w*,', text)
   ## for i in match:









print set_up_file('Sheet_1.csv')
