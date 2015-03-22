__author__ = 'defremov85'

#import mysql.connector

import MySQLdb
import pprint

def dbrib_data():
    gcm_results_list = []
    gcm_list = []

    db_connection = MySQLdb.connect(host='localhost', user='reports', passwd='password')
    cursor = db_connection.cursor()
    cursor.execute('USE deutsche_schema')
    cursor.execute("SELECT * FROM deutsche_schema.GCM")
    result = cursor.fetchall()
    for i in result:
    #    print '[%s]' % ', '.join(map(str, i))
        for item in i:
            gcm_list.append(item)
    gcm_results_list = map(list, zip(*[iter(gcm_list)]*len(i)))

    for gcm,urg,impl,appr,server,crt,start in gcm_results_list:
        value = gcm,urg,impl,appr,server,crt,start
        #print value
        f.write(str(value) + '\n')
    #return '\n'.join(str(gcm_results_list))

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

    #print '<table>'
    #for sublist in a:
        #print sublist
        #print '  <tr><td>'
        #print '    </td><td>'.join(sublist)
        #print '  </td></tr>'
    #print '</table>'



f = open('output.html','r+')
dbrib_data()
f.close()

f = open('output.html','r')
fw = open('good_output.html','w')
html_table()
f.close()
fw.close()



#data()

#htmlFilename = 'test.html'
#htmlFile = open(htmlFilename, 'w')
#htmlFile.write = data
#def formatDataAsHtml(data):
#    return '\n'.join(data)

#htmlFile.write(formatDataAsHtml(data()))
#htmlFile.write(data())
#htmlFile.close()




"""
cnx = mysql.connector.connect(user='reports', password='password',
                              host='127.0.0.1',
                              database='deutsche_schema')

cursor = cnx.cursor()

query = ("SELECT * FROM deutsche_schema.GCM where CI_List = ANY (SELECT Server_Name FROM deutsche_schema.CI where NARid = '72075-1')")
#query_ci = ("SELECT * FROM deutsche_schema.CI where NARid = '72075-1'")

#hire_start = datetime.date(1999, 1, 1)
#hire_end = datetime.date(1999, 12, 31)

a = cursor.execute(query)
#cursor.execute(query_ci)

print a

for i in cursor:
  print i

cursor.close()
cnx.close()
"""
