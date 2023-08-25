<div align=center>
 
# DrSINAWAY-DDoS
 <p>
 <img src="https://img.shields.io/github/stars/cutipu/HASOKI?color=%23DF0067&style=for-the-badge"/> &nbsp;
 <img src="https://img.shields.io/github/forks/cutipu/HASOKI?color=%239999FF&style=for-the-badge"/> &nbsp;
  <a href="#"><img alt="Hasoki last commit (main)" src="https://img.shields.io/github/last-commit/cutipu/HASOKI/main?color=green&style=for-the-badge"></a>
 <a href="https://github.com/drsinaway/DrSINAWAY-DDoS/issues"><img alt="MatrixTM issues" src="https://img.shields.io/github/issues/cutipu/HASOKI?color=purple&style=for-the-badge"></a>
   <img src="https://img.shields.io/github/license/cutipu/HASOKI?color=%23E8E8E8&style=for-the-badge"/> &nbsp;
</p>
 
 DDoS Attack Panel includes CloudFlare Bypass (UAM, CAPTCHA, BFM, etc..)<br/><br/>
 
 Don't attack any websites you don't own it<br/>
 This was created for educational purposes<br/>
 All responsibilities and disadvantages of using this program is for the user.
 

## Language</br>

 <img src="https://img.shields.io/badge/Python-FFDD00?style=for-the-badge&logo=python&logoColor=blue"/></br>
</div>

```sh
- [x] Add auto download fresh socks5 after attack with method sky and slowloris
- [x] Add HTTP/2 (HTTPX) method
- [x] Add bypass method [STRONG ATTACK]
- [x] Add spoof method [STRONG ATTACK]
- [x] Change pxcfb to TSL1.3 Proxy Flood 
- [x] Add HULK - HTTP Unbearable Load King
- [x] Add pxHULK - proxy HTTP Unbearable Load King
 
```


## Methods
### version-v1.0
```sh
  [Layer 7]
 - cfb     | Bypass CF attack
 - pxcfb   | Bypass CF attack with proxy
 - cfreq   | Bypass CF UAM, CAPTCHA, BFM, etc,, with request
 - cfsoc   | Bypass CF UAM, CAPTCHA, BFM, etc,, with socket
 - pxsky   | Bypass Google Project Shield, Vshield, DDoS Guard Free, CF NoSec With Proxy
 - sky     | Sky method without proxy
 - http2   | HTTP 2.0 Request Attack 
 = pxhttp2 | HTTP 2.0 Request Attack With Proxy
 - get     | Get  Request Attack
 - post    | Post Request Attack
 - head    | Head Request Attack
 - soc     | Socket Attack
 - pxraw   | Proxy Request Attack
 - pxsoc   | Proxy Socket Attack
 
  [Layer 4]
  -udp     | UDP Attack
  -tcp     | TCP Attack
  
  [Tools]
 - Dns     | Classic DNS Lookup
 - Geoip   | Geo IP Address Lookup
 - Subnet  | Subnet IP Address Lookup
 - .proxy  | Getting proxies into proxy.txt
 - .proxies| Counts the number of proxies in the proxy.txt file
```
## Methods
### version-v2.0
```sh
  [Layer 7]
 - cfb     | Bypass CF attack
 - pxcfb   | Bypass CF attack with proxy
 - cfreq   | Bypass CF UAM, CAPTCHA, BFM, etc,, with request
 - cfsoc   | Bypass CF UAM, CAPTCHA, BFM, etc,, with socket
 - pxsky   | Bypass Google Project Shield, Vshield, DDoS Guard Free, CF NoSec With Proxy
 - sky     | Sky method without proxy
 - http2   | HTTP 2.0 Request Attack 
 = pxhttp2 | HTTP 2.0 Request Attack With Proxy
 - get     | Get  Request Attack
 - post    | Post Request Attack
 - head    | Head Request Attack
 - soc     | Socket Attack
 - pxraw   | Proxy Request Attack
 - pxsoc   | Proxy Socket Attack
 
  [Layer 4]
  -udp     | UDP Attack
  -tcp     | TCP Attack
  
  [Tools]
 - Dns     | Classic DNS Lookup
 - Geoip   | Geo IP Address Lookup
 - Subnet  | Subnet IP Address Lookup
 -  proxy  | Getting proxies into proxy.txt
 -  proxies| Counts the number of proxies in the proxy.txt file
```

## Menu version-v3.0
![DrSINAWAY](https://raw.githubusercontent.com/drsinaway/DDos-Dr.SINAWAY/main/resources/Screenshot%20at%202023-05-10%2014-34-06.png)

![DrSINAWAY](https://raw.githubusercontent.com/drsinaway/DDos-Dr.SINAWAY/main/resources/Screenshot%20at%202023-05-10%2014-34-16.png)

![DrSINAWAY](https://raw.githubusercontent.com/drsinaway/DDos-Dr.SINAWAY/main/resources/Screenshot%20at%202023-05-10%2014-34-25.png)

![DrSINAWAY](https://raw.githubusercontent.com/drsinaway/DDos-Dr.SINAWAY/main/resources/Screenshot%20at%202023-05-10%2014-34-36.png)

## Methods
### version-v3.0
```sh
  [Layer 7]
 - spoof | STRONG ATTACK with spoof Header X-ForWard
 - http2 | HTTP/2 attack with proxy [httpx]
 - cfb   | Bypass CF attack
 - pxcfb | Bypass CF attack tsl1.3 with proxy [fixed work]
 - cfpro | Bypass CF UAM(Under Attack Mode), CAPTCHA, BFM(Bot Fight Mode) etc.. (request)
 - cfsoc | Bypass CF UAM(Under Attack Mode), CAPTCHA, BFM(Bot Fight Mode) etc.. (socket)
 - bypass| Bypass Google Project Shield, Vshield etc.. (socket)
 - raw   | Request Attack
 - post  | Post Request Attack
 - head  | Head Request Attack
 - soc   | Socket Attack
 - hulk  | HTTP Unbearable Load King
 - hulk  | proxy hulk HTTP Unbearable Load King
 - sky   | HTTPS Flood and bypass for CF NoSec, DDoS Guard Free and vShield (SOCKS5)
 -stellar| HTTPS Sky method without proxies
 - pxraw | Proxy Request Attack
 - pxsoc | Proxy Socket Attack
 - pxslow| slowloris Attack (SOCKS5)
 
  [Layer 4]
  -udp | simple udp flood
  -tcp | simple tcp syn flood <work fine ! >
  -vse | Send Valve Source Engine Protocol
  -mine| minecraft dos attack
  
  [Tools]
 - Dns        | Classic DNS Lookup
 - Geoip      | Geo IP Address Lookup
 - Subnet     | Subnet IP Address Lookup
 
 - Next Update SLOWREAD method (SOON...)
```
## Usage on Linux
```sh
You must use Python 3.9 or higher

 $ git clone https://github.com/drsinaway/DrSINAWAY-DDoS.git
 $ cd DrSINAWAY-DDoS
Install Python3 modules
 $ pip3 install -r requirements.txt  or  pip install -r requirements.txt
Install Chrome (or update it lastest version)
 $ wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
 $ apt-get install ./google-chrome-stable_current_amd64.deb
 OR
 $ dpkg -i ./google-chrome-stable_current_amd64.deb
 - Thread set 10-50 > work
 OR
 $ python3 setup.py

```
## Example
```sh
Use DDoS Panel   : python3 DrSINAWAYDDoS-v1.py OR python3 DrSINAWAYDDoS-v2.py OR python3 DrSINAWAYDDoS-v3.py
Use command line : python3 python3 DrSINAWAYDDoS-v1.py <method> <target> <thread> <time>
      └──────────> python3 python3 DrSINAWAYDDoS-v1.py cfb https://example.com 100 30
```
<!--## Usage on Termux
```sh
$ pkg install x11-repo
$ pkg install unstable-repo
$ pkg update -y
$ pkg upgrade -y

$ pkg install python3
$ pkg install git
$ pkg install wget
$ pkg install rust
$ pip install supertools wheel
$ pip install shutup
$ git clone https://github.com/drsinaway/DrSINAWAY-DDoS.git
$ cd DrSINAWAY-DDoS
$ export CARGO_BUILD_TARGET=aarch64-linux-android && python3 -m pip install cryptography
$ export CARGO_BUILD_TARGET==aarch64-linux-android && python3 -m pip install -r requirements.txt
$ python3 -m pip install httpx[http2]

```
## Example
```sh
Use DDoS Panel   : python3 DrSINAWAYDDoS-v1.py OR python3 DrSINAWAYDDoS-v2.py OR python3 DrSINAWAYDDoS-v3.py
Use command line : python3 python3 DrSINAWAYDDoS-v1.py <method> <target> <thread> <time>
      └──────────> python3 python3 DrSINAWAYDDoS-v1.py cfb https://example.com 100 30
```
## Usage on Windows
```sh

Install python - https://www.python.org
Install Git - https://gitforwindows.org 

$ git clone https://github.com/drsinaway/DrSINAWAY-DDoS.git
$ cd DrSINAWAY-DDoS
$ pip install -r requirements.txt

```
## Example
```sh
Use DDoS Panel   : python3 DrSINAWAYDDoS-v1.py OR python3 DrSINAWAYDDoS-v2.py OR python3 DrSINAWAYDDoS-v3.py
Use command line : python3 python3 DrSINAWAYDDoS-v1.py <method> <target> <thread> <time>
      └──────────> python3 python3 DrSINAWAYDDoS-v1.py cfb https://example.com 100 30
``` -->

## Contacts:
[![Telegram](https://img.shields.io/badge/-Telegram-blue)](https://telegram.me/drsinaway)
[![Egypt Cyber Army](https://img.shields.io/badge/-Telegram-blue)](https://t.me/egpyt_cyber_army)
[![Forum](https://img.shields.io/badge/-Forum-red)](https://linktr.ee/dr.sinaway)

