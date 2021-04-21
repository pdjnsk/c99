import time
import os
import shutil

path = input("enter the folder path ")

days = time.time()


os.path.exists(path)

list_of_files = os.listdir(path)
print(list_of_files)
os.walk(path)

join = os.path.join(path)


ctime = os.stat(path).st_ctime


compair = days - ctime


if (compair < 2592000):
	print ("files deleted")
	os.remove(path)

	