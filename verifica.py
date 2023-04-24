import requests
import hashlib
import time
from datetime import datetime

while True:
    x = requests.get('https://www.cesgranrio.org.br/concursos/evento.aspx?id=bb0122')
    corpo = x.content
    messageDigest = hashlib.sha1()
    stringM = str(corpo)
    byteM = bytes(stringM, encoding='utf')
    messageDigest.update(byteM)
    now = datetime.now()
    print(str(now.hour) + ":" + str(now.minute) + ":" + str(now.second) + " " + messageDigest.hexdigest())
    time.sleep(1)