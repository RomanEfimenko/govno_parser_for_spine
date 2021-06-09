import json

text = 0
time_actions = []
names_actions = []
with open('g1_grader_garage.json', 'r', encoding='utf-8') as f: #открыли файл
    text = json.load(f) #загнали все из файла в переменную
    # print(text) #вывели результат на экран

anims = text.get("animations")
names_actions = anims.keys() # название ключей(экшенов)
for anim in names_actions :
    print("ACTION - "+anim)
    anm = anims.get(anim)
    max_time = 0.0
    for slotorbon in anm :
        huina = anm.get(slotorbon)
        for el_anim in huina :
            huina2 = huina.get(el_anim)
            for diya in huina2 :
                huina3 = huina2.get(diya)
                for step in huina3 :
                    #print(step)
                    if max_time < step.get("time") :
                        max_time = float(step.get("time"))

    print("TIME - "+str(max_time))





















konec = input()
