#!/usr/bin/python
# -*- coding: utf-8 -*-

import ftplib

def anonLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@your.com')
        print ('\n[*] ' + str(hostname) +\
          ' FTP Anonymous Logon Succeeded.')
        ftp.quit()
        return True
    except:
        print ('\n[-] ' + str(hostname) +\
	  ' FTP Anonymous Logon Failed.')
	return False
    
host = '210.42.121.132'
anonLogin(host)
