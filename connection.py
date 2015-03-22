__author__ = 'defremov85'

import MySQLdb

def dbrib_data():
    gcm_results_list = []
    gcm_list = []

    db_connection = MySQLdb.connect(host='localhost', user='reports', passwd='password')
    cursor = db_connection.cursor()
    cursor.execute('USE deutsche_schema')
    cursor.execute("SELECT * FROM deutsche_schema.GCM")
    result = cursor.fetchall()

    for i in result:
        for item in i:
            gcm_list.append(item)
    gcm_results_list = map(list, zip(*[iter(gcm_list)]*len(i)))

    for gcm,urg,impl,appr,server,crt,start in gcm_results_list:
        value = gcm,urg,impl,appr,server,crt,start
        f.write(str(value) + '\n')

def html_table():
    fw.write('<table border="1" style="width:100%">\n')
    fw.write(' <tr>\n')
    fw.write('  <th>GCMid</th>\n')
    fw.write('  <th>Urgency</th>\n')
    fw.write('  <th>Implementer Group</th>\n')
    fw.write('  <th>Approver Group</th>\n')
    fw.write('  <th>CI List</th>\n')
    fw.write('  <th>Created Date</th>\n')
    fw.write('  <th>Planned Date</th>\n')
    fw.write(' </tr>\n')
    for line in f:
        fw.write(' <tr>\n')
        for i in line.split(', '):
            i = i.replace("'","")
            i = i.replace("(","")
            i = i.replace(")","")
            i = i.replace("\n","")
            fw.write('  <td>' + i + '</td>\n')
        fw.write(' </tr>\n')
    fw.write('</table>\n')

f = open('output.html','r+')
dbrib_data()
f.close()

f = open('output.html','r')
fw = open('good_output.html','w')
html_table()
f.close()
fw.close()

