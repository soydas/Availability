# Author S.G. 22.01.2022 Availability Check (Mevcudiyet:)
# https://github.com/soydas/Availability

import os
import ssl
import sys
import urllib.request
from datetime import datetime
from socket import timeout
from urllib.error import URLError, HTTPError
from urllib.request import Request

from colorama import Fore, Style
from tabulate import tabulate

# Bu kod gereklidir, silinirse Status "Unreachable" olur.
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Varsayılan olarak HTTPS sertifikalarını doğrulamayan Eski Python için
    pass
else:
    # HTTPS doğrulamasını desteklemeyen hedef ortamı için
    ssl._create_default_https_context = _create_unverified_https_context

url_listem = "list.txt"
script_dizini = os.path.dirname(os.path.abspath(__file__))
dosya_yolu = os.path.join(script_dizini, url_listem)

while True:

    with open(dosya_yolu, "r") as f:

        table = []

        for line in f:
            if line[0] == '#':
                continue

            if line.strip() == "":
                continue

            req = Request(line)
            opener = urllib.request.build_opener()
            # 'User-agent', 'Python-urllib/3.11' --> 'User-Agent', 'Mozilla/5.0') dönüştürür.
            opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
            row = [line]

            try:
                response = opener.open(req, timeout=15)
                if response.status == 200:
                    row.append(Fore.GREEN + "Response : " + str(response.status) + " OK." + Style.RESET_ALL)

            except timeout as e:
                row.append(Fore.RED + "Socket timed out" + Style.RESET_ALL)
                tarih = datetime.now().strftime('%Y-%m-%d')
                zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                fh = open(script_dizini + "\\" + "log_" + tarih + ".txt", mode="a+")
                fh.write(zaman + " " + line.strip() + " -> Zaman aşımı.\n")
                fh.close()

            except HTTPError as e:
                row.append(Fore.RED + "Server request failed" + Style.RESET_ALL)
                # row.append("Error: " + str(e.code))
                tarih = datetime.now().strftime('%Y-%m-%d')
                zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                fh = open(script_dizini + "\\" + "log_" + tarih + ".txt", mode="a+")
                fh.write(zaman + " " + line.strip() + " -> Sunucu isteği yerine getiremedi.\n")
                fh.close()

            except URLError as e:
                row.append(Fore.RED + f"URL Hatası / Ulaşılamıyor" + Style.RESET_ALL)
                # row.append("Error: " + str(e.reason))
                tarih = datetime.now().strftime('%Y-%m-%d')
                zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                fh = open(script_dizini + "\\" + "log_" + tarih + ".txt", mode="a+")
                fh.write(zaman + " " + line.strip() + f" -> URL Hatası: {e}.\n")
                fh.close()

            except ValueError as e:
                print(Fore.RED + "list.txt içinde yanlış link var" + Style.RESET_ALL)

            except ConnectionResetError as e:
                row.append(Fore.RED + "Existing connection forcibly closed by a remote host" + Style.RESET_ALL)
                tarih = datetime.now().strftime('%Y-%m-%d')
                zaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                fh = open(script_dizini + "\\" + "log_" + tarih + ".txt", mode="a+")
                fh.write(zaman + " " + line.strip() + " -> Varolan bir bağlantı"
                                                      " uzaktaki bir ana bilgisayar tarafından zorla kapatıldı.\n")
                fh.close()
                break

            except KeyboardInterrupt:
                print(Fore.YELLOW + "bye! ;)" + Style.RESET_ALL)
                sys.exit()

            table.append(row)
            sys.stdout.flush()

    f.close()
    os.system('cls')
    print(tabulate(table, headers=[Fore.BLUE + "URL", f"Status  {datetime.now().strftime('T:%H:%M:%S')}" + Style.RESET_ALL], tablefmt="grid"))

    # print('10sn bekle')
    # time.sleep(10)
