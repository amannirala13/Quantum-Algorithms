# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:18:33 2020

@author: amann
"""


import sys
import os

def write_successful(article):
    try:
        toc = open('toc.qan', 'a')
    except:
        sys.exit("ERROR: toc.qan file missing")
    toc.write(article+"\n")
    toc.close()
  
    
    
def get_article_data(article):
    #try:
    data = open(article+"/data.txt",'r')
    #except:
        #sys.exit("ERROR: data.txt file missing")
    info = data.readlines()
    data.close()
    article_data_raw=[]
    for i in range (0, len(info)):
        article_data_raw.append(info[i].split(':~'))
    
    article_data = ['Title', 'Brief', 'Link', 'Name', 'Github', 'Repos_link']
    for i in range (0,len(article_data_raw)):
        if article_data_raw[i][0] in ["Title","TITLE", "title"]:
            article_data[0] = article_data_raw[i][1].strip()
        elif(article_data_raw[i][0] in ["Brief","BRIEF", "brief"]):
            article_data[1] = article_data_raw[i][1].strip()
        elif(article_data_raw[i][0] in ["Link","LINK", "link"]):
            article_data[2] = article_data_raw[i][1].strip()
        elif(article_data_raw[i][0] in ["Name","NAME", "name"]):
            article_data[3] = article_data_raw[i][1].strip()
        elif(article_data_raw[i][0] in ["Github","GITHUB", "github"]):
            article_data[4] = article_data_raw[i][1].strip()
        
    article_data[5] = "https://github.com/amannirala13/Quantum-Algorithms/tree/master/"+article[2:].replace(' ', '%20')
        
    return article_data



def write_to_html(article, index):
    article_data = get_article_data(article)
    updated = '<tbody align="center"><tr><th scope="row">'+str(index)+'</th><td>'+article_data[0]+'</td><td><button class = "btn btn-primary" data-toggle="collapse" data-target="#'+'detail_'+str(index)+'">Show details</button></td><td><a href="'+article_data[4]+'">'+article_data[3]+'</a></td><td><a href="'+article_data[2]+'"><button class = "btn btn-primary">Read Article</button></a></td><td><a href="'+article_data[5]+'"><button class = "btn btn-dark">Visit Github</button></a></td></tr></tbody><tbody><tr id ='+'detail_'+str(index)+' class="collapse in"><td colspan="6"><div class = "alert alert-warning">'+article_data[1]+'</div></td></tr></tbody>\n<!--71050AC3E762F5B380B440D1661B0201735BA539EDD0E7D39B9DFA37622E7CF3-->'
    
    try:
        webpage = open('index.html', 'r')
    except:
        sys.exit("ERROR: index.html file missing")
    content = webpage.read()
    content = content.replace('<!--71050AC3E762F5B380B440D1661B0201735BA539EDD0E7D39B9DFA37622E7CF3-->', updated)
    webpage.close()
    
    try:
        webpage = open('index.html', 'w')
    except:
        sys.exit("ERROR: index.html file missing")
    webpage.write(content)
    webpage.close()
    
    write_successful(article)



article_list = [f.path for f in os.scandir("./") if f.is_dir()]
reject_list = ["./res", "./.git", "./.github", "./node_modules"]
try:
    toc = open('toc.qan', 'r')
    indexed_list = toc.readlines()
    toc.close()
except:
    indexed_list = []
index = len(indexed_list)

for i in range (0, len(article_list)):
    if article_list[i]+"\n" not in indexed_list:
        if article_list[i] not in reject_list:
            index = index+1
            write_to_html(article_list[i],index)
