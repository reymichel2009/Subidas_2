import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5477880325:AAG4D9yuEljDKFmUb12aF2y6i2k-_rCDS3Q')
API_ID =  os.environ.get('api_id','17158127')
API_HASH = os.environ.get('api_hash','d1a5974070430293b64fde5339591447')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','reymichel2009').split(';')
static_proxy = '' #agrega si kieres tener un proxy statico Con @raydel0307 si kieres comprar un proxy
PROXY = ProxyCloud.parse(static_proxy)

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')

space = {}
space['reymichel2009', 'george0x0'] = 0
