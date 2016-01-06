import os,time, datetime



##############################
## Functions
##############################

def get_filepaths(directory):
    file_paths = [] # list to store the directories

    for root,directories,files in os.walk(directory):
            for directory in directories:
                filepath = os.path.join(root,directory)
                file_paths.append(filepath)
    return file_paths


def printReadings(full_file_paths):
    allList = []
    i = 0
    for dir in full_file_paths:

        file = dir + "/w1_slave"
        f = open(file, 'r')
	    id = getId(dir)
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')


        reading =  f.read()

        temp = getTemp(reading)

        f.close()
        values = [st,dir,temp]
	allList.append(values)
        #writeTemp(values)
	#print values
    return allList

def getId(dir):
    result = dir.split('devices/')
    return result[1]


def getTemp(text):
    temp = "t="
    index = text.find(temp)+2
    tempc = float(text[index:])/1000.0
    return tempc

def writeTemp(values):

    file = open("2016.txt",'a')

    s = str(values)
    file.write(s)
    file.write("\n")

    file.close()

def addSpacing():
	file = open("test.txt",'a')
	file.write("\n\n\n\n\n\n")
	print ("\n\n\n\n\n\n")
	file.close()


def getReadings():
	full_file_paths = get_filepaths("/sys/bus/w1/devices")
	full_file_paths.pop(0) #this gets rid of the non sensor directory
	return printReadings(full_file_paths)


#
# while(True):
#
#     	time.sleep(600)
