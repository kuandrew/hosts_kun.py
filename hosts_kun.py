#coding:gbk
import math
import os
def init():
    hosts = open('C:\Windows\System32\drivers\etc\hosts','r',0)
    str = hosts.read()
    hosts.close
    s = str.split('\n')
    data = dict()
    i = 0
    for item in s :
        if item.find('#')!=-1 or len(item) < 10:
            continue
        if item.count(' ') == 1:
            ip = item[:item.find(' ')]
            domain = item[item.find(' ') + 1:]
            data[i] = {'ip':ip,'domain':domain}
            i+=1
    return data

def show():
    data = init()
    for i in data:
        print data[i]
    main()

def select():
    data = init()
    domain = raw_input('������Ҫ���ҵ�����,����q���� \n')
    if(domain == 'q'):
        main()
    result = []
    for i in data:
        if (data[i]['domain'] == domain):
            result.append(i)
    if(len(result) == 0):
        print 'û���ҵ��������\n'
    else:
        for i in result:
            print 'id = ',i,'\n',data[i]
    select()

def add():
    domain = raw_input('���������� \n')
    ip = raw_input('������IP \n')
    str = '\n'+ip+' '+domain
    hosts = open('C:\Windows\System32\drivers\etc\hosts','a',0)
    hosts.write(str)
    hosts.close
    print '��ӳɹ�'
    main()

def delete():
    data = init()
    id = raw_input('�������ӦID,����q���� \n')
    if(id == 'q'):
        main()
        return
    id = int(id)
    try:
        str = '\n'+data[id]['ip']+' '+data[id]['domain']
        hostsR = open('C:\Windows\System32\drivers\etc\hosts','r')
        temp = hostsR.read()
        temp = temp.replace(str,'')
        print str
        hostsR.flush
        hostsR.close
        print 'ɾ���ɹ�\n'
        hostsN = open('C:\Windows\System32\drivers\etc\hosts','w',0)
        hostsN.write(temp)
        hostsN.close
    except:
        print 'û���ҵ���ӦID \n'
        delete()
    main()
    return

def main():
    choice = input('1���鿴 2����ѯ 3������ 4��ɾ�� \n')
    if choice == 1:
        show()
    elif choice == 2:
        select()
    elif choice == 3:
        add()
    elif choice == 4:
        delete()
    else:
        main()
main()

    

