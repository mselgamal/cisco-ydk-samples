from argparse import ArgumentParser as argp
from urlparse import urlparse

from ydk.services import CRUDService as service
from ydk.providers import NetconfServiceProvider as NetConfService
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_native
import logging
import sys
import getpass

'''
    run:
        pythong read-hostname-ios-xe.py <device ip address> <port>
'''

'''
    access object's hostname attribute and print
'''
def read_hostname(native):
    print(native.hostname)

'''
   - format ip address, username and password to unicode format (required by netconf service provider)
   - format port to int
   - create a netconf provider object (handles connection to IOS device using netconf protocol over ssh)
   - create a crud service object ('create, read, update and delete' service)
   - create a ios_xe native object ('native' object represents 
   the yang model for cisco IOS xe, converted to a python object)
'''
def main():
    ip = unicode(sys.argv[1],'utf-8')
    port = int(sys.argv[2])
    username = unicode(raw_input("Username: "),'utf-8') 
    password = unicode(getpass.getpass(),'utf-8')
    print("hello, we are connecting to the IOS device")
    
    provider = NetConfService(address=ip,
            port=port,
            username=username,
            password=password,
            protocol=u'ssh')
    
    crud = service()

    native = xe_native.Native()
    native = crud.read(provider,native)
    read_hostname(native)
main()
