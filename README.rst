SMS messages using the CYTA Web sms API
======================================= 


Introduction
============

A command line util, easily scriptable that will provide the *simple* functionality to send very easily sms messages through CYTA.


Requirements
============		

Requires python 2.7.x and the package httplib2. Also make sure you have your CYTA''s  username and  passkey available. They are 
easily available from the `cyta web site <https://www.cyta.com.cy/web-sms>`_.


How it works
============
Make sure you have an internet connection. Open a command line or terminal. Execute the following command:

``cyta_send_sms.py -d 99211189 -m "this is the message i wish to send" -u username -p passkey``

Also by executing :

``cyta_send_sms.py -h``

it will display the help/usage options.

``usage: cyta_send_sms.py [-h] -d MOBILENUMBER -m MESSAGE -u USERNAME -p PASSKEY  [--version]``

``arguments:``

``-h, --help       show this help message and exit``

``-d MOBILENUMBER  destination mobile number``

``-m MESSAGE       message``

``-u USERNAME      username for the cyta's web sms api``

``-p PASSKEY       secretkey for the cyta's web sms api``

``--version        show program's version number and exit``



License
=======
CYTA Web sms API is licensed under the GNU ver. 3 License.

