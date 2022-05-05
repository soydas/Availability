# Author S.G. 22.01.2022 Availability Check
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.request
from datetime import datetime
from socket import timeout
import time
import sys
import ssl
import os

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


while True:

    f = open("list.txt", "r")

    for line in f:
        if line[0] == '#':
            continue
        print(len(line) * '_')

        if line.strip() == "":
            continue

        req = Request(line)

        try:
            response = urllib.request.urlopen(req, timeout=15)
            if response.status == 200:
                print(line + "\nResponse : " + str(response.status) + " OK.")

        except timeout as e:
            print(line + '-->socket timed out')
            tarih = datetime.now().strftime('%Y-%m-%d')
            print(tarih)
            zaman = datetime.now().strftime('%Y-%m-%d %H %M %S')
            print(zaman)
            print(os.getcwd())
            fh = open("log_" + tarih + ".txt", mode="a+")
            fh.write(zaman + " " + line + "-->socket timed out\n")
            fh.close()

        except HTTPError as e:
            print(line + '-->Sunucu isteği yerine getiremedi.')
            print('Hata : ', e.code)
            tarih = datetime.now().strftime('%Y-%m-%d')
            zaman = datetime.now().strftime('%Y-%m-%d %H %M %S')
            print(os.getcwd())
            fh = open("log_" + tarih + ".txt", mode="a+")
            fh.write(zaman + " " + line + "-->Sunucu isteği yerine getiremedi.\n")
            fh.close()

        except URLError as e:
            print(line + '\n-->Ulaşılamıyor.')
            print('Hata : ', e.reason)
            tarih = datetime.now().strftime('%Y-%m-%d')
            zaman = datetime.now().strftime('%Y-%m-%d %H %M %S')
            print(os.getcwd())
            fh = open("log_" + tarih + ".txt", mode="a+")
            fh.write(zaman + " " + line + "-->Ulaşılamıyor.\n")
            fh.close()

        except ValueError as e:
            print(line + '-->list.txt\'de uygun olmayan link mevcut!')
            print('Hata : ', e.reason)
        else:
            sys.stdout.flush()
    f.close()
    print('15sn bekle')
    time.sleep(15)
