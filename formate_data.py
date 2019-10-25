#import pandas as pd
#pd.DataFrame([
#    ["hello",1],
#    ["world",2]
#    ])

import numpy as np
import pandas as pd


event_list = ["20028823","20023771","20027251","20023799","20028335","20025783","20038067","20027421","20027425","20035569","20023779","20023777","20023773","20023781","20029429","20023805","20025571","20024017","20023775","20025223","20023769","20023807","20024991","20035113","20030225","20025731","20032603","20027465","20027427","20028699","20023783","20028437","20024419","20032439","20024413","20023793","20028013","20023803","20032501","20025229","20033771","20024337","20033881","20032449","20026523","20035545","20028473","20031129","20025801","request_token","20032737","game_load","engine_load","20023801","20026441","20023789","20023785","20023768","20025727","20033111","20026513","20023791","20035553","20032441","20025735","20036879","20032653","20035845","20026535","20024421","20028855","20024335","20025097","20035587","20037895","engineBegin","20029113","20030237","cleanupBegin","caton","averageFps","cleanupEnd","minFps","lowFpsDuration","20028009","20033893","gameEnd","gameBegin","20030221","20034391","20032509","engineEnd","20025737","20026515","20031603","20033151","20190429","20027991","20033117","20035809","51201","20027939","20025715","20028011","PushOpenSucceed"] 

event_num = len(event_list)
one_hot_dict = np.identity(event_num,dtype = int)
event_map = {}
for i in range(len(event_list)):
    event_map[event_list[i]]=i

#print(event_map)
#太大了要分批读取
df_event = pd.read_csv("/workspace/share_dir/event_sequence.csv")
last_hdid = ""
last_is_black = 0
last_event = np.zeros(event_num,dtype = int)

def m_print():
    if last_hdid != "":
        print("%s %d %s" % (last_hdid,last_is_black ," ".join([str(i) for i in last_event.tolist()])))

#print(event_map["20025229"])
for index,row in df_event.iterrows():
    print(index)
    hdid = row['hdid']
    is_black = row['is_black']
    eventid = str(row['eventid'])
    if hdid != last_hdid:
        m_print()
        last_hdid = hdid 
        last_is_black = is_black
        last_event = np.zeros(event_num,dtype = int)
#    print(event_map[eventid])
    tmp = event_map[eventid]
    last_event += one_hot_dict[tmp]
m_print()
