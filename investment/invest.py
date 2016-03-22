import random

class Investment():

    def __init__(self, number_of_enterprises, req_dict, numb_of_rows):
        #self.number_of_projects = number_of_projects
        self.number_of_enterprises = number_of_enterprises
        self.data = req_dict
        self.numb_of_rows = numb_of_rows
        self.number_of_answers = 0

    def create_dictionary(self):
        l = []
        enterprises = []
        '''cr = {   'C11': 0, 'R11': 0,
                                        'C12': 1, 'R12': 3,
                                        'C13': None, 'R13': None,
                        
                                        'C21': 0, 'R21': 0,
                                        'C22': 3, 'R22': 5,
                                        'C23': 5, 'R23': 9,
                        
                                        'C31': 0, 'R31': 0,
                                        'C32': 1, 'R32': 4,
                                        'C33': 2, 'R33': 6,
                        
                                        'C41': 0, 'R41': 0,
                                        'C42': 2, 'R42': 3,
                                        'C43': None, 'R43': None,
                                }'''
        copy = {}
        numb_of_proj = 0

        list_rs = []
        dd = {}
        for pred in range(1, self.number_of_enterprises+1):
            for proj in range(1, self.numb_of_rows+1):
                index = 'R'+str(pred)+str(proj)
                if not self.data[index] in list_rs:
                    list_rs.append(self.data[index])
                    index_x = 'X'+str(proj)
                    dd[index_x] = [index, self.data[index]]
            #print(list_rs, dd)
            index_pred = 'company'+str(pred)
            copy[index_pred] = dd.copy()
            numb_of_proj = max(numb_of_proj, len(list_rs))
            list_rs.clear()
            dd = {}
        #print("copy", copy)
        #print(numb_of_proj)

        for i in range(1,self.number_of_enterprises+1): #1,2,3,4
            enterprise = 'company'+str(i)
            enterprises.append(enterprise)

            # задаем список для  построения структуры  -- {'enterprise4': [], 'enterprise1': [], 'enterprise3': [], 'enterprise2': []}
            l.append((enterprise,[]))

            ll = []
            projects = []
            for j in range(1,numb_of_proj+1):   #1,2,3
                project = 'project'+str(j)
                projects.append(project)

                # задаем список для добавления проектов для каждого enterprise-- [{'project1': [], 'project2': [], 'project3': []}]
                ll.append((project, []))

        #добавляем предприятия для основного dict -- {'enterprise4': [], 'enterprise1': [], 'enterprise3': [], 'enterprise2': []}
        d = dict([a for a in l])

        for pred in enterprises:
            # добавляем проекты для каждого предприятия -- [{'project1': [], 'project2': [], 'project3': []}]
            d[pred] = [dict([a for a in ll])]

        for n, k in enumerate(sorted(copy.keys()), start=1):
            for p in range(0, numb_of_proj):
                proj = 'project'+str(p+1)
                try:
                    c = sorted(copy[k])[p]
                    r = sorted(copy[k].values())[p][1]
                    c = self.data[c]
                except IndexError:
                    c = None
                    r = None
                cc = 'C' + str(n)   # значения C11, C21, ....
                rr = 'R' + str(n)   # значения R11, R21, ....
                d[k][0][proj] = dict([(cc, c),(rr, r)])

        return numb_of_proj, d

    @staticmethod
    def etap(d=None, numb_of_rows=None, numb_of_projects=None, numb_of_companies=None, et=None, f=None):
        data_etap = {}
        dict_f = {}
        print("ETAP\t", et)
        if f == None:
            for i in range(1, numb_of_projects+1):
                perem = 'pr' + str(i) + '_c' + str(et)  #вместо numb_of_comp наверное должно быть et
                data_etap[perem] = {}
            #print("data etap\t", data_etap)
            for i in range(1, numb_of_projects+1):
                perem = 'pr' + str(i) + '_c' + str(et)
                if d['company'+str(et)][0]['project'+str(i)]['C'+str(et)] == None:
                    #pass
                    data_etap[perem] = None
                else:
                    r = int(d['company'+str(et)][0]['project'+str(i)]['C'+str(et)])
                    #print("r\t", r)
                    for ii in range(numb_of_rows-1, r-1, -1):
                        y = 'y'+str(ii)                                                         # ИЗМЕНЕНО
                        data_etap[perem][y] = d['company'+str(et)][0]['project'+str(i)]['R'+str(et)]
                        if ii == r and ii != 0:
                            for p in range(ii-1, -1, -1):
                                y = 'y'+str(p)                                                    #ИЗМЕНЕНО
                                data_etap[perem][y] = None
        else:
            for i in range(1, numb_of_projects+1):
                perem = 'pr' + str(i) + '_c' + str(et)  #вместо numb_of_comp наверное должно быть et
                data_etap[perem] = {}
            #print(data_etap)
            for i in range(1, numb_of_projects+1):
                perem = 'pr' + str(i) + '_c' + str(et)
                if d['company'+str(et)][0]['project'+str(i)]['C'+str(et)] == None:
                    #pass
                    data_etap[perem] = None
                else:
                    r = int(d['company'+str(et)][0]['project'+str(i)]['C'+str(et)])
                    #print(r)
                    for ii in range(numb_of_rows-1, r-1, -1):
                        y = 'y'+str(ii)                                                         # ИЗМЕНЕНО
                        #print(y, perem)
                        data_etap[perem][y] = d['company'+str(et)][0]['project'+str(i)]['R'+str(et)]
                        if ii == r and ii != 0:
                            for p in range(ii-1, -1, -1):
                                y = 'y'+str(p)                                                    #ИЗМЕНЕНО
                                data_etap[perem][y] = None

            #print(data_etap)
            for k in sorted(data_etap.keys()):
                #print(k)
                if_none = 0
                if data_etap[k] != None:
                    for enum, key_y in enumerate(sorted(data_etap[k].keys())):
                        #print(enum, key_y)
                        if data_etap[k][key_y] != None:
                            f_keys = sorted(f.keys())[enum-if_none]
                            #print(f[f_keys])
                            #print("f", f[key_f])
                            #print(data_etap[k][key_y] + "+" + str(f[f_keys]))
                            data_etap[k][key_y] = str(int(data_etap[k][key_y]) + int(f[f_keys]))
                        else:
                            if_none += 1
        print("data etap", data_etap)

        data_y = {}
        max_values = []
        max_values_key = []
        max_vals = {}
        for ii in range(0, numb_of_rows):
            for k in data_etap.keys():
                if data_etap[k] == None:
                    #print('none')
                    pass
                else:
                    #print('yeah')
                    y = 'y'+str(ii)
                    if data_etap[k][y] == None:
                        max_values.append(-1)
                        max_values_key.append(k+y)
                        max_vals[k+y] = -1
                    else:
                        max_values.append(int(data_etap[k][y]))
                        max_values_key.append(k+y)
                        max_vals[k+y] = int(data_etap[k][y])
            #print("max_values_key\t", max_values_key)
            #print("max_values\t", max_values)
            #print("max_vals\t", max_vals)
            max_value = max(max_vals.values())
            if max_values.count(max_value) > 1:
                pass

            key_for_data_y = max_values_key[max_values.index(max_value)]
            #print(key_for_data_y.split('_'))
            key_for_data_y = key_for_data_y.split('_')[1][-2:] + '_' + key_for_data_y.split('_')[0]
            data_y[key_for_data_y] = max_value
            #print("key_for_data_y\t", key_for_data_y)
            #print(max_value, '\n')

            max_values = []
            max_values_key = []
            max_vals = {}
        return data_y

    def find_maximums(self, aa, n_of_projects):
        """aa - invest dict"""
        et = self.number_of_enterprises
        result_fs = {}
        f = None
        n_of_rows = self.numb_of_rows
        numb_of_proj = n_of_projects
        numb_of_companies = self.number_of_enterprises
        for e in range(et, 0, -1):
            #print('ETAP ' + str(e))
            ep = 'ETAP ' + str(e)
            f= self.etap(aa, n_of_rows, numb_of_proj, numb_of_companies, e, f)
            result_fs[ep] = f
            #print("f", f)
            #print('\n')
        return result_fs

    def return_result(self, aa, result_fs):
        """aa - invest dict"""
        et = self.number_of_enterprises
        summ_of_money = self.numb_of_rows - 1
        max_val_etap = -1
        result_proj = []
        for i in range(1, et+1):
            ep = 'ETAP ' + str(i)
            #print(result_fs[ep])
            for v in sorted(result_fs[ep].keys(), reverse=True):
                company = 'company' + str(i)
                proj = 'project' + str(v[-1])
                c = 'C' + str(i)
                yy = 'y' + str(v[1:2])
                #print("yy", yy[-1], "money", summ_of_money)
                #print("money - ", summ_of_money, "from d- ", aa[company][0][proj][c], "y-", yy[-1])
                if summ_of_money >= int(aa[company][0][proj][c]) and int(yy[-1]) == summ_of_money:
                    #print("max- ", max_val_etap, "res- ", result_fs[ep][v])
                    if max_val_etap < result_fs[ep][v]:
                        max_val_etap = result_fs[ep][v]
                        summ_of_money -= int(aa[company][0][proj][c])
                        result_proj.append(proj)
                        #print("money", summ_of_money)

            #print("\tmax", max_val_etap)
            max_val_etap = 0

        #print("project list- \t", result_proj)
        return result_proj

if __name__ == '__main__':
    request_dict = {'R11': '0', 'R21': '0', 'R31': '0', 'R41': '0', 'X1': '0',
                                'R12': '3', 'R22': '0', 'R32': '4', 'R42': '0', 'X2': '1',
                                'R13': '3', 'R23': '0', 'R33': '6', 'R43': '3', 'X3': '2',
                                'R14': '3', 'R24': '5', 'R34': '6', 'R44': '3', 'X4': '3',
                                'R15': '3', 'R25': '5', 'R35': '6', 'R45': '3', 'X5': '4',
                                'R16': '3', 'R26': '9', 'R36': '6', 'R46': '3', 'X6': '5'
                }

    rows = 6
    companies = 4
    #print(data)
    invest_obj = Investment(number_of_enterprises=companies, req_dict=request_dict, numb_of_rows=rows)
    n_of_proj, invest_dict = invest_obj.create_dictionary()
    print("invest_dict", invest_dict, "\nn_of_proj", n_of_proj)
    res_fs = invest_obj.find_maximums(invest_dict, n_of_proj)
    print("res_fs", res_fs)
    invest_result =invest_obj.return_result(invest_dict, res_fs)
    print("invest_result", invest_result)
    #e = invest_obj.etap(invest_dict, rows, n_of_proj, companies, companies)
    #print(e)
    if invest_obj.number_of_answers > 1:
        print("Задача має {0} рішення".format(invest_obj.number_of_answers))
    """numb_of_rows = 6
                a = Investment(4, request_dict, numb_of_rows)
                nn, aa= a.create_dictionary()
                print("aa", aa)
            
                #print(aa)
            
                numb_of_companies = 4
                numb_of_rows = 6
                numb_of_projects = 3
                summ_of_money = 5
                et = numb_of_companies
            
            
                result_fs = {}
                f = None
                for e in range(et, 0, -1):
                    print('ETAP ' + str(e))
                    ep = 'ETAP ' + str(e)
                    f = a.etap(aa, numb_of_rows, numb_of_projects, numb_of_companies, e, f)
                    result_fs[ep] = f
                    print("f", f)
                    print('\n')
            
                max_val_etap = -1
                result_proj = []
                for i in range(1, et+1):
                    ep = 'ETAP ' + str(i)
                    #print(result_fs[ep])
                    for v in sorted(result_fs[ep].keys(), reverse=True):
                        company = 'company' + str(i)
                        proj = 'project' + str(v[-1])
                        c = 'C' + str(i)
                        yy = 'y' + str(v[1:2])
                        #print("yy", yy[-1], "money", summ_of_money)
                        print("money - ", summ_of_money, "from d- ", aa[company][0][proj][c], "y-", yy[-1])
                        if summ_of_money >= int(aa[company][0][proj][c]) and int(yy[-1]) == summ_of_money:
                            print("max- ", max_val_etap, "res- ", result_fs[ep][v])
                            if max_val_etap < result_fs[ep][v]:
                                max_val_etap = result_fs[ep][v]
                                summ_of_money -= int(aa[company][0][proj][c])
                                result_proj.append(proj)
                                print("money", summ_of_money)
            
                    print("\tmax", max_val_etap)
                    max_val_etap = 0
            
                print("project list- \t", result_proj)"""


