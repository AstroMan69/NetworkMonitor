import os
#import socket 
import platform    
import subprocess
#import time
from typing import Text

#hostname = socket.gethostname()    
#IPAddr = socket.gethostbyname(hostname)    
#print("Your Computer Name is:" + hostname)    
#print("Your Computer IP Address is:" + IPAddr) 

ip_list = ['192.168.1.10', '192.168.1.144']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    #if "Received = 4" in response:
    if "Destination host unreachable" not in response:
        print(f"UP {ip} Ping Successful")
    else:
        i = 0
        x = 0
        while i < 3:
            response = os.popen(f"ping {ip}").read()
            #if "Received = 4" in response:
            if "Destination host unreachable" not in response:
                print(f"UP {ip} Ping Successful")
            else:
                print(f"DOWN {ip} Ping Unsuccessful")
                i = i + 1
                print("Count:", i)
                x = x + 1
                while x < 3:
                    response = os.popen(f"ping {ip}").read()
                    #if "Received = 4" in response:
                    if "Destination host unreachable" not in response:
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
                            import smtplib, ssl
                            from email.mime.text import MIMEText
                            from email.mime.multipart import MIMEMultipart

                            sender_email = "sabretest7@gmail.com"
                            receiver_email = "darren.pratt@sabrerail.com"
                            password = 'Maz1keen!'

                            message = MIMEMultipart("alternative")
                            message["Subject"] = "Server Down"
                            message["From"] = sender_email
                            message["To"] = receiver_email
                            
                            text = """\
                                A server has returned as unresponsive, please check server: {ip}
                                """
                            html = """\
                            <html>
                                <body>
                                  <p>Hi,<br>
                                     A server has returned as unresponsive, please check server: {ip}<br>
                                  </p>
                                </body>
                            </html>
                            """.format(ip=ip)
                            
                            part1 = MIMEText(text, "plain")
                            part2 = MIMEText(html, "html")

                            message.attach(part1)
                            message.attach(part2)
                            
                            context = ssl.create_default_context()
                            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                                server.login(sender_email, password)
                                server.sendmail(sender_email, receiver_email, message.as_string())
                                print("Message Sent")
                            print("Proccess Complete")

def ping(host):

    param = '-n' if platform.system().lower()=='windows' else '-c'

    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0