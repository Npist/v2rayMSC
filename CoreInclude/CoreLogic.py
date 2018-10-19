from CoreInclude import Config
from CoreInclude import RsaModel
import requests
import json

public_key = '''
'''

private_key = '''
'''

headers = {'User-Agent': Config.UA}
login_url = Config.DOMAIN + '/V2rayMS_ClientAPI.php'

rsa = RsaModel.Rsa(pub_skey=public_key, pri_skey=private_key)


def user_login(user_data):
    send_post = requests.post(
        login_url,
        rsa.enc_bytes(json.dumps(user_data).encode()),
        headers=headers)
    try:
        getlist = eval(send_post.content.decode())
        if getlist[0].strip() == 'error_code':
            Call_Error(getlist)
        else:
            Config.set_client(
                json.loads(rsa.dec_bytes(send_post.content).decode()))
    except Exception:
        Config.set_client(
            json.loads(rsa.dec_bytes(send_post.content).decode()))


def login_check():
    client = Config.get_client()
    if len(client) != 0:
        if client[0]['name']:
            return True
    return False


def connect_message(order_data):
    send_post = requests.post(
        login_url,
        rsa.enc_bytes(json.dumps(order_data).encode()),
        headers=headers)
    try:
        getlist = eval(send_post.content.decode())
        if getlist[0].strip() == 'error_code':
            Call_Error(getlist[1])
        else:
            Config.set_order(
                json.loads(rsa.dec_bytes(send_post.content).decode()))
    except Exception:
        Config.set_order(json.loads(rsa.dec_bytes(send_post.content).decode()))


def get_server():
    order = Config.get_order()
    resolve_data = order['server_conn'].split('|')
    show_servers = []
    program_use_servers = []
    if len(resolve_data) % 6 != 0:
        Call_Error('0x110')
        return []
    else:
        server_count = int(len(resolve_data) / 6)
        for i in range(server_count):
            server_name = resolve_data[0 + i * 6].strip().strip('\r\n')
            server_ip = resolve_data[1 + i * 6].strip().strip('\r\n')
            server_port = resolve_data[2 + i * 6].strip().strip('\r\n')
            server_alterid = resolve_data[3 + i * 6].strip().strip('\r\n')
            server_protocol = resolve_data[4 + i * 6].strip().strip('\r\n')
            server_path = resolve_data[5 + i * 6].strip().strip('\r\n')
            show_msg = [
                server_name,
                server_protocol.upper() + ' ' + server_ip + ':' + server_port
            ]
            app_msg = [
                server_name, server_ip, server_port, server_alterid,
                server_protocol, server_path
            ]
            show_servers.append(show_msg)
            program_use_servers.append(app_msg)
        Config.set_servers(enumerate(program_use_servers))
        return enumerate(show_servers)


def Call_Error(error_code):
    print(error_code)
