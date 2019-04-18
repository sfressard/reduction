#!/usr/bin/env python
import os,glob,shutil

#Create an 'old' directory to put all the deprecated script versions
os.system("mkdir old")

#Filter only the script files and create a unique list of script names
scriptNameList=[] 
for f in glob.glob("*.sh*"): 
	scriptName=f.split(".")[0]
        if scriptName not in scriptNameList:
		scriptNameList.append(scriptName) 
#print scriptNameList

#Get file list sorted by modification date
sortedFileList=sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

#For each script name, get all the versions 
for scriptName in scriptNameList:
	filteredFileList=[k for k in sortedFileList if scriptName+'.sh-v' in k]

	#In case of need, sort by name
        #filteredFileList.sort()
        print filteredFileList

        #If symlink exists, rename it
        targetScriptName=scriptName+".sh"
        if os.path.exists(targetScriptName) and os.path.islink(targetScriptName):
		print "Symlink exists, archiving it .."
		os.system("mv "+targetScriptName+" old/")

        #TO DO: Identify the latest version (the one the symlink is pointing to) and issue warnings if it's not the same 
        # as the last version in the file list

        #For each version, copy to target file and commit
        i=0
        for file in filteredFileList:
                print "Copy "+file+" into "+targetScriptName
		shutil.copy(file,targetScriptName)
                if i==0:
			os.system("git add "+targetScriptName)
		os.system("git commit -m '"+file+"' "+targetScriptName)
                os.system("mv "+file+" old/ ")
                i+=1
		#Test if the file exists in git, if file exists in git	
                 
#for scriptName in scriptNameList:
#  print scriptName

#files = sorted(os.listdir(path),key=os.path.getctime);
#print files  
#Commit the history of every file
