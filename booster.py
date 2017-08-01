#!/usr/bin/python

from time import sleep
import websocket
import json,sys,signal

stop=False;
f=open("proxies", "r"); # One IP per line, must use port 3128. no spaces infront of proxies

ip=None;
if len( sys.argv ) > 1:
    ip=sys.argv[1];

if not ip:

    while True:
        
        ip=f.readline();
        ip=ip.strip();
        print("trying ", ip);
        
        try:
            master = websocket.create_connection("ws://lines.editfight.com/app",   http_proxy_host=ip, http_proxy_port=3128 )    
            break;
        except :
            continue;

else:
    master = websocket.create_connection("ws://lines.editfight.com/app",   http_proxy_host=ip, http_proxy_port=3128 )    

uuid="461f2199-c299-472f-b065-244f8f9ad586";
data=json.loads( master.recv() );
#print (data); sys.eixt // uncomment to get your uid, or just get it throgh the console, i don't relaly care


print("boosting: ", uuid)
conns=[]
conns.append(master)
#i=0;
#for i in range(0,1):
#    conns.append( create_connection("ws://lines.editfight.com/app") );


print("Boosting ",uuid," from ", ip);

while True:
    #for c in conns:

    try:
        master.send('{"upvote":"'+uuid+'"}');
        sleep(3);
    except:
        master = websocket.create_connection("ws://lines.editfight.com/app",   http_proxy_host=ip, http_proxy_port=3128 )    







def signal_handler(signal, frame):
        print('Closing sockets.')
        master.close();
        for c in conns:
            c.close();
        print("Dieing");
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)