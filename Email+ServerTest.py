import os
#import socket 
import platform    
import subprocess
import time

#hostname = socket.gethostname()    
#IPAddr = socket.gethostbyname(hostname)    
#print("Your Computer Name is:" + hostname)    
#print("Your Computer IP Address is:" + IPAddr) 

ip_list = ['IP1', 'IP2', 'IP3']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        i = 0
        x = 0
        while i < 3:
            response = os.popen(f"ping {ip}").read()
            if "Received = 4" in response:
                print(f"UP {ip} Ping Successful")
            else:
                print(f"DOWN {ip} Ping Unsuccessful")
                i = i + 1
                print("Count:", i)
                x = x + 1
                while x < 3:
                    response = os.popen(f"ping {ip}").read()
                    if "Received = 4" in response:
                        print(f"UP {ip} Ping Successful")
                        i = 3
                        break
                    else:
                        print(f"DOWN {ip} Ping Unsuccessful")
                        i = i + 1
                        print("Count:", i)
                        x = x + 1
                        if x == 3:
                            print("Server Unresponsive, please check server:",ip)
                            import smtplib

                            sender = 'Your Email'

                            password = 'Your Password'

                            receivers = ['Receivers Email']

                            message = """From: Your name <Your Email>
                            To: Receivers name <Receivers Email>
                            MIME-Version: 1.0
                            Content-Type: text/html
                            Subject: Test E-Mail

                            A server has returned as unresponsive, please check server: {ip}
                            """.format(ip=ip)

                            server = smtplib.SMTP('smtp.gmail.com:587')
                            server.ehlo()
                            server.starttls()
                            server.login(sender, password)
                            try:
                                server.sendmail(sender, receivers, message)
                                print("Message sent successfully")
                            except:
                                print("Failed to send message")
                            server.quit()
                            
def ping(host):

    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0
