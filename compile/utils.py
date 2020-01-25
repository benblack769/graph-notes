import csv
import collections

def read_csv(fname):
    with open(fname) as csvfile:
        spamreader = csv.DictReader(csvfile)
        return list(spamreader)
        #return [{key:value for key,value in item.items()} for item in spamreader]

def join(strlist):
    return "".join(strlist)

def linejoin(strlist):
    return "\n"+"\n".join(strlist)+"\n"

def key_dictlist_by(dicts,key):
    return {d[key]:d for d in dicts}

def read_file(fname):
    with open(fname) as file:
        return file.read()

def write_file(fname,text):
    with open(fname,'w') as file:
        file.write(text)
