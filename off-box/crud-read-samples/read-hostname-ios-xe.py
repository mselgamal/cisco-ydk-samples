from argparse import ArgumentParser as argp
from urlparse import urlparse

from ydk.services import CRUDService as service
from ydk.providers import NetconfServiceProvider as NetConfService
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_native
import logging
import sys
import getpass


def read_hostname(native):
    print(native.hostname)

def main():
    ip = unicode(sys.argv[1],'utf-8')
    port = 830
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
    process_native(native)
main()
