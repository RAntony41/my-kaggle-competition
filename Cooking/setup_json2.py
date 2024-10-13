import json


#train set
with open('capgen_v1.0_train.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

path = []
label = []
for i in data.keys():
    temp = i
    
    for j in data[i]:
        
        if i[:12] == 'coco/val2017':
            temp = '/project/lt900502-ck24tn/captioning/coco/val2017' + i[-17:]
        elif i[:14] == 'coco/train2017':
            temp = '/project/lt900502-ck24tn/captioning/coco/train2017' + i[-17:]
            
        elif i[:16] == 'ipu24/val/travel':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/val/travel' + i[-17:]
        elif i[:14] == 'ipu24/val/food':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/val/food' + i[-17:]
        
        elif i[:18] == 'ipu24/train/travel':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/train/travel' + i[-17:]
        elif i[:16] == 'ipu24/train/food':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/train/food' + i[-17:]
        
        
        path.append(temp)
        label.append(j)
        
final_dic = []
for i, _ in enumerate(label):
  dic = {
    "id": str(i),
    "image": [path[i]],
    "conversations": 
      "<Image><Image><|user|>\nช่วยอธิบายรูปนี้ใหน่อย<|end_of_text|>\n<|assistant|>\n" + label[i]
    }
  final_dic.append(dic)

st = "/format_capgen_v1.0_train.json" + " " + str(len(final_dic)) + "\n"

with open('format_capgen_v1.0_train.json', 'w', encoding='utf-8') as file:
  json.dump(final_dic, file, ensure_ascii=False, indent=4)
    
    
#val set
with open('capgen_v1.0_val.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

path = []
label = []
for i in data.keys():
    temp = i
    
    for j in data[i]:
        
        if i[:12] == 'coco/val2017':
            temp = '/project/lt900502-ck24tn/captioning/coco/val2017' + i[-17:]
        elif i[:14] == 'coco/train2017':
            temp = '/project/lt900502-ck24tn/captioning/coco/train2017' + i[-17:]
            
        elif i[:16] == 'ipu24/val/travel':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/val/travel' + i[-17:]
        elif i[:14] == 'ipu24/val/food':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/val/food' + i[-17:]
        
        elif i[:18] == 'ipu24/train/travel':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/train/travel' + i[-17:]
        elif i[:16] == 'ipu24/train/food':
            temp = '/project/lt900502-ck24tn/captioning/ipu24/train/food' + i[-17:]
        
        
        path.append(temp)
        label.append(j)
        
final_dic = []
for i, _ in enumerate(label):
  dic = {
    "id": str(i),
    "image": [path[i]],
    "conversations": 
      "<Image><Image><|user|>\nช่วยอธิบายรูปนี้ใหน่อย<|end_of_text|>\n<|assistant|>\n" + label[i]
    }
  final_dic.append(dic)
  
st = st + "/format_capgen_v1.0_val.json" + " " + str(len(final_dic)) + "\n"

with open('format_capgen_v1.0_val.json', 'w', encoding='utf-8') as file:
  json.dump(final_dic, file, ensure_ascii=False, indent=4)
  

#.txt
with open('data.txt', 'w', encoding='utf-8') as file:
    file.write(st)