#!/usr/bin/env python

# Main steps:
# 1) Create a main loop for the program - done
# 2) Utilize the time function to update feed - done
# 3) Test with more sources - done
# 4) Create check methods to allow for more arguments-done
#    A) Allow the ability to add sources through argument - to be tested-done
# Project marked completed 6/10/2019
# Next steps:
#pressing 's' to search for titles for keywords
import threading,sys,select,os,time,feedparser,colorama
import feeds
filename = "source.txt"
keyword = None
flag=''
def inputtimer(prompt,timeout):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    ready,_,_=select.select([sys.stdin],[],[],timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n').split()
    else:
        return None
if len(sys.argv) >1:
  flag = sys.argv[1]
  if(flag=='-s'):
     keyword=sys.argv[2:]
  if(flag=='-a'):
    feeds.enterSource(sys.argv[2],filename)    

feed =feeds.gatherSources(filename)
 
def mainLoop(flag,keyword):
  choice=[None]
  while choice[0] !='q':
    if choice == '-s':
        flag = choice[0]
        keyword = choice[1:]
    if(keyword == None):
        feeds.feedloop(flag,feed)
    else:
       feeds.feedloop,(flag,feed,keyword)
    choice=inputtimer('>',5)
    if(choice==None):
      choice = [None]
    if(len(choice)==0):
      choice = [None]
mainLoop(flag,keyword)
