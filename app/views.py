from django.shortcuts import render

# Create your views here.
from app.models import *
import csv
from django.http import HttpResponse

def insert_bank(self):
    with open('C:\\Users\\SAINATH REDDY\\OneDrive\\Desktop\\Django_1\\vishnu\\Scripts\\csvfiles\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)
        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank Data Is Inserted SuccessFully..!')


def insert_branch(self):
    with open('C:\\Users\\SAINATH REDDY\\OneDrive\Desktop\\Django_1\\vishnu\\Scripts\\csvfiles\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifsc=i[1]
                branch=i[2]
                address=i[3]
                contact=i[4]
                city=i[5]
                district=i[6]
                state=i[7]

                BRO=Branch(bank_name=BO[0],ifsc=ifsc,branch=branch,address=address,contact=contact,city=city,district=district,state=state)
                BRO.save()

    return HttpResponse('Branch is InsertedSuccessFully...!!!!!!')