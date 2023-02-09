from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import List
import pandas as pd
import shutil as st
import str_time
import os
import filetype
app = FastAPI()

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# #load data into a DataFrame object:
# df = pd.DataFrame(data)
# df = df.to_json()

time = str_time.now_utc()
dir_name = str_time.str_yyyy_mm_dd(time)
file_name = str_time.get_time()



# @app.post("/")
# async def root(file: UploadFile = File(...)):
#   with open(f'{file_name}', 'wb') as alex:
#     st.copyfileobj(file.file, alex)
#   return {'file_name': alex}


@app.post("/uploadfile/")
async def upload_file(files: List[UploadFile] = File(...)):
  for file_in_list in files:
    dir_path = "upload/" + str_time.str_yyyy_mm_dd(time)
    str_time.create_path("upload")
    str_time.create_path(dir_path)
    type = file.filename.split(".")[1]
    file_path = dir_path + "/" + f'{file_name}.{type}'
    # file_path = dir_path + "/" + f'{file_name}.wav'
    file_bytes = file_in_list.file.read()
    print(file_bytes)
    str_time.upload_file_bytes(file_bytes, file_path)
    # with open(f'{file_path}', 'wb') as alex:
    #     st.copyfileobj(file_in_list.file, alex)
    return {'file_name': 'Good'}
    
@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfile/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)


# with open('requirements.txt', mode='r', encoding='UTF-8') as f:
#     print()
