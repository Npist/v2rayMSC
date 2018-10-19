TitleName = 'Npist'
DOMAIN = 'https://proxy.npist.com'
UA = 'V2rayMS_Client'


class global_var:
    client = '{}'
    order = ''
    username = ''
    servers = None


def change_loginflag():
    if global_var.loginflag is False:
        global_var.loginflag = True
    else:
        global_var.loginflag = False


def loginflag():
    return global_var.loginflag


def QSS():
    with open('style/Default.qss', 'r', encoding='utf-8') as qss_file:
        return qss_file.read()


def set_username(username):
    global_var.username = username


def get_username():
    return global_var.username


def set_client(client):
    global_var.client = client


def get_client():
    return global_var.client


def set_order(order):
    global_var.order = order


def get_order():
    return global_var.order


def set_servers(servers):
    global_var.servers = servers


def get_servers():
    return global_var.servers
