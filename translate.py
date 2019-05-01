import boto3

from docx import Document
from docx.shared import Inches

import re

filename = "C:/\\Users/\\admin/\\Desktop/\\apn.docx"

document = Document(filename)
orgintext = ''
newtext = []
for data in document.paragraphs:
    orgintext += data.text

newtext = re.findall(r'.{500}',orgintext)

print(len(newtext))


for i in range(len(newtext)):
    print(len(newtext[i]))
    translate = boto3.client(service_name='translate', region_name='us-east-1', use_ssl=True)
    result = translate.translate_text(Text=newtext[i],
                SourceLanguageCode="en", TargetLanguageCode="zh")
    print(result.get('TranslatedText'))
    print("\n")


#with open(filename,'rb') as f:
#    data = f.read(100)

















# print('SourceLanguageCode: ' + result.get('SourceLanguageCode'))
# print('TargetLanguageCode: ' + result.get('TargetLanguageCode'))


# !/usr/bin/env python
# -*- coding: utf-8 -*-


#translate = boto3.client(service_name='translate')

# The terminology file 'my-first-terminology.csv' has the following contents:
'''
en,fr
Amazon Family,Amazon Famille

# Read the terminology from a local file
with open('translate.csv', 'rb') as f:
    data = f.read()

file_data = bytearray(data)


print("Importing the terminology into Amazon Translate...")
response = translate.import_terminology(Name='my-first-terminology', MergeStrategy='OVERWRITE',
                                        TerminologyData={"File": file_data, "Format": 'CSV'})
print("Terminology imported: "),
print(response.get('TerminologyProperties'))
print("\n")

print("Getting the imported terminology...")
response = translate.get_terminology(Name='my-first-terminology', TerminologyDataFormat='CSV')
print("Received terminology: "),
print(response.get('TerminologyProperties'))
print("The terminology data file can be downloaded here: " + response.get('TerminologyDataLocation').get('Location'))
print("\n")

print("Listing the first 10 terminologies for the account...")
response = translate.list_terminologies(MaxResults=10)
print("Received terminologies: "),
print(response.get('TerminologyPropertiesList'))
print("\n")

print("Translating 'Amazon Family' from English to Chinese with no terminology...")
response = translate.translate_text(Text="Amazon Family", SourceLanguageCode="en", TargetLanguageCode="zh")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

print("Translating 'Amazon Family' from English to Chinese with the 'my-first-terminology' terminology...")
response = translate.translate_text(Text="Amazon Family", TerminologyNames=["my-first-terminology"],
                                    SourceLanguageCode="en", TargetLanguageCode="zh")
print("Translated text: " + response.get('TranslatedText'))
print("\n")

'''