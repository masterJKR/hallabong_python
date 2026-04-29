#json_test2.py

import json

# 화면에 자동차가  몇대가 있냐  
with open("file/18396710_frame_127.json" , "r", encoding="utf-8") as f:
    data = json.load(f)

anno = data["frames"]["annotations"]

print( "차량 몇대 : " , len(anno) )