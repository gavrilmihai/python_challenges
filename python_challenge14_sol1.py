'''
Day 14 Challenge
'''
import time
import paramiko

def connect_para(ip_user_pass_tuple):
    '''Calls up the parimiko ssh session'''
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_user_pass_tuple[0],
                       username=ip_user_pass_tuple[1],
                       password=ip_user_pass_tuple[2],
                       look_for_keys=False)
    connection = ssh_client.invoke_shell()
    return connection

def manal_command_entry(session):
    '''not used, but point to this function for testing'''
    usercommand = ""
    while usercommand == input('What command to run? '):
        session.sendall(usercommand+'\n')
        time.sleep(1)
        data_out = session.recv(4094)
        print(data_out.decode().strip())
        print(type(data_out))
        print(data_out)
    session.close()


def command_set(session):
    '''pushes the lines one by one, no error checking is done'''
    usercommands = ['conf t', 'alias exec sabibby show ip int bri | ex own',
                    'do sabibby', 'ip access-list extended sabibby',
                    'deny tcp any any eq 23', 'permit ip any any',
                    'int loopback 666', 'ip access-group sabibby in',
                    'do show ip int loop 666 | inc access']
    for command in usercommands:
        session.sendall(command+'\n')
        time.sleep(1)
        data_out = session.recv(4094)
        print(data_out.decode().strip())
    session.close()

#Define the variables that we will use & create a tuple
IP = '10.53.254.222'
USERNAME = 'python'
PASSWORD = 'secretsnake'
MY_DEVICE = (IP, USERNAME, PASSWORD)

#Pass the tuple to the function
DEVICE_SESSION = (connect_para(MY_DEVICE))
command_set(DEVICE_SESSION)
