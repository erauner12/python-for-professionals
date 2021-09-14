
import os
import shutil

def Diff(li1, li2):
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
    return li_dif

os.chdir('/Users/erauner/git/python-for-professionals')

alreadyExist = []

chapterMapping = {}

for d in os.listdir():
    file_name, file_ext = os.path.splitext(d)

    if "Chapter" in d:
        file = d.split(" ")
        chapterMapping.update({file[1]:d})
        


for f in os.listdir():    
    if "Chapter" not in f:
        file = f.split("_")
        
        for item in chapterMapping.items():
            if item[0] == file[0]:
                print(f)
                print(item[1])
                shutil.move(f,item[1])
            
    
    
    
