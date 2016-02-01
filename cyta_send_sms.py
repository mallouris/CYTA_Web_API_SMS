#!/usr/bin/env python
# Created by Stephanos Mallouris 7-Sept-2015
# will use CYTA's SMS gateway to sent sms messages
# it will only need the httplib2 dependency package 

import argparse
import httplib2


def CYTA_Web_SMS(mobilenumber,XmlValidSmsMessage,username,passkey ):    
    PostData = '<?xml version="1.0" encoding="UTF-8" ?> ' \
               "<websmsapi>" \
               " <version>1.0</version>" \
               " <username>" + username + "</username>" \
               " <secretkey>" + passkey + "</secretkey>" \
               " <recipients>" \
               " <count>1</count>" \
               " <mobiles>" \
               " <m>" + str(mobilenumber) + "</m>" \
               " </mobiles>"  \
               " </recipients>" \
               " <message>" + XmlValidSmsMessage + "</message>" \
               " <language>en</language>" \
               "</websmsapi>"
    print PostData

    url='https://www.cyta.com.cy/cytamobilevodafone/dev/websmsapi/sendsms.aspx'
    #print 'Full message length' +str(len(PostData))
    
    myheader = { "Content-Type" : "application/xml; charset=utf-8", 'content-length':str(len(PostData)) }
    httpconnect = httplib2.Http()
    responce, content = httpconnect.request(url,'POST', headers=myheader, body=PostData)
    print '\n'
    print PostData
    print '\n'
    
    print 'Server Responce:' + str(responce)
    print '\nContent:' + str(content)    


if __name__ == '__main__':
    utilpurpose = '\nThis util is for accessing CYTA''s bulk sms service for sending bulk messages or even integrading it into your application, alerting or administratior ' + \
                  'tasks. Util is provided as is under GNU v3 licensing scheme.Use -h switch for help\n'

    parser = argparse.ArgumentParser(description=utilpurpose)
    parser = argparse.ArgumentParser(add_help=True)
    
    parser.add_argument('-d',action='store', dest='mobilenumber', help='destination mobile number', required=True)
    parser.add_argument('-m',action='store', dest='message', help='message', required=True)
    parser.add_argument('-u',action='store', dest='username', help="username for the cyta's web sms api", required=True)
    parser.add_argument('-p',action='store', dest='passkey', help="secretkey for the cyta's web sms api", required=True)

    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    results = parser.parse_args()

    
    CYTA_Web_SMS(results.mobilenumber,results.message,results.username,results.passkey)    
    
