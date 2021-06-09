import os
import os.path
import json

def search_spine_jsons(_dir) :
    file_list = os.listdir(_dir)
    for chell in file_list :
        if chell.find(".json") != -1 :
            #print(_dir+"\\"+chell)
            list_jsons.append(_dir+"\\"+chell)
        if chell.find(".") == -1 :
            search_spine_jsons(_dir+"\\"+chell)

text = 0
list_jsons = []
time_actions = []
names_actions = []

parent_dir = os.getcwd()
search_spine_jsons(parent_dir)
print("-----")

for adresa in list_jsons :
    print("PATH - "+adresa)
    print("-----")
    with open(adresa, 'r', encoding='utf-8') as f: #открыли файл
        text = json.load(f) #загнали все из файла в переменную
    anims = text.get("animations")
    names_actions = anims.keys() # название ключей(экшенов)
    for anim in names_actions :
        print("ACTION - "+anim)
        anm = anims.get(anim)
        max_time = 0.0
        for slotorbon in anm :
            huina = anm.get(slotorbon)
            for el_anim in huina :
                if str(type(huina)).find("<class 'dict'>") != -1 :
                    huina2 = huina.get(el_anim)
                    for diya in huina2 :
                        if str(type(huina2)).find("<class 'dict'>") != -1 :
                            huina3 = huina2.get(diya)
                            for step in huina3 :
                                #print(step)
                                if str(type(step)).find("<class 'dict'>") != -1 :
                                    if step.get("time") != "none" :
                                        if max_time < step.get("time") :
                                            max_time = float(step.get("time"))
        pos_doc = str((round(30*max_time))/30).find(".")
        #print((len(str((round(30*max_time))/30)) - pos_doc))
        if 3 < (len(str((round(30*max_time))/30)) - pos_doc) :
            print("TIME - "+str(max_time))
            print("FRAMES - "+str((round(30*max_time))))
            print(str((round(30*max_time))/30))
            print("--------------")



konec = input()
