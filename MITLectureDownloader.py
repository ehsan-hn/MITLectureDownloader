

import requests  as rq
import bs4
from homura import download
import os
import os.path


baseUrl="https://ocw.mit.edu"
courseUrl=raw_input("Enter the course link: ")#"https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-034-artificial-intelligence-fall-2010"
lecturesPage="/lecture-videos/"
lecturesPage2="/videos-lecture/"
lecturesPageUrl=courseUrl+lecturesPage
dpage
print ("reading course name...")
try:
    
    dpage = rq.get(courseUrl)
    dsoup = bs4.BeautifulSoup(dpage.content)
except:
    lecturesPageUr= courseUrl+lecturesPage
    dpage = rq.get(courseUrl)
    dsoup = bs4.BeautifulSoup(dpage.content)
    
directory =dsoup.find("h1",class_="title").string
print directory
print("reading content ...")
page = rq.get(lecturesPageUrl)
soup = bs4.BeautifulSoup(page.content)  
lectures = soup.findAll("a",class_="medialink")
videolinks = []
su = []
subsceneLinks = []
print("getting video link...")
for n in lectures:
    VideoPage = rq.get(baseUrl+n.get('href'))
    s2 = bs4.BeautifulSoup(VideoPage.content)
    try:
        div = s2.find("div",id="vid_related")
        links = div.findAll("a")
        videolinks.append(links[1].get("href"))
    except:
        try:
            div = s2.find("div",id="vid_transcript")
            links = div.findAll("a")
            videolinks.append(links[1].get("href"))
        except:
            pass
    
    script = s2.find("div",id="course_wrapper_media")
    sub = script.findAll("script")
    su.append(sub[1].string)
print("done.")
for s in su:
    sa = s[39:-2]
    subsceneLinks.append(baseUrl+sa)
    
print videolinks
print subsceneLinks

if not os.path.exists(directory):
    os.makedirs(directory)
if not os.path.exists(directory+"/download.txt"):
    saveFile = open(directory+"/download.txt",'w')
    saveFile.write("")
    saveFile.close()
for i in range(len(videolinks)):
    print i
    if subsceneLinks[i] not in open(directory+"/download.txt").read():
        print("downloading : "+subsceneLinks[i])
        download(url = subsceneLinks[i] , path = directory)
        appendFile = open(directory+"/download.txt",'a')
        appendFile.write(subsceneLinks[i])
        appendFile.close()
    if videolinks[i] not in open(directory+"/download.txt").read():
        print("downloading : "+videolinks[i])
        download(url = videolinks[i] , path = directory)
        appendFile = open(directory+"/download.txt",'a')
        appendFile.write(videolinks[i])
        appendFile.close()
