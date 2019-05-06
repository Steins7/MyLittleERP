
import os

path = os.path.abspath(".")
dirs,filename = os.path.split(path)

if os.path.dirname(path)
    # creation of directories
    if not os.path.exists(dirs +"/json_files"):	os.makedirs(dirs + "/json_files")
    if not os.path.exists(dirs +"/src"):		os.makedirs(dirs + "/src")
    if not os.path.exists(dirs +"/csv_files"):	os.makedirs(dirs + "/csv_files")

    # move code files in the src directory
    for i in os.listdir(dirs):
	    if os.path.isdir(dirs+"/"+i): continue
	    if i == "README.txt":          continue 
	    os.rename(dirs+"/"+i, dirs+"/src/"+i)	



