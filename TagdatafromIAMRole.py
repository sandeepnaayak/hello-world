import json
import boto3
import logging
import time
import datetime

iam = boto3.resource('iam')
role = iam.role('CE_TagData_Readonly')
mio = role.tags('key','value')
print (mio.value)




tg = []
    iam = boto3.resource('iam')
    role = iam.Role('App_Temp_Tag_Automation')
    tg = role.tags
    for mytag in tg:
        if mytag['Key'] == 'CE_MIO_Code':
            mio = (mytag['Value'])
        elif mytag['Key'] == 'CE_Application_ID':
            appid =  (mytag['Value'])
        elif mytag['Key'] == 'CE_Business_Entity':
            bizent = (mytag['Value'])
    print ( mio , appid , bizent )
