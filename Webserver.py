import os
# -*- coding: cp1252 -*-
import codecs
import time
import requests
import urllib2
import urllib
import json as m_json
import os
import sys
from urllib import FancyURLopener
import time
from flask import Flask, request, Response
from BeautifulSoup import BeautifulSoup, Comment
import json as simplejson
Soup = BeautifulSoup
from nltk import sent_tokenize, word_tokenize
from collections import Counter
from collections import defaultdict
from math import log10
# -*- coding: utf-8 *-*
import nltk.data
from nltk.corpus import wordnet as wn
from nltk import pos_tag
import nltk
from nltk import word_tokenize
from collections import Counter
from math import log10
import re
syno =[]
hg = 0
sentence = '''Mugabe rose to prominence in the 1960s as the Secretary General of the Zimbabwe African National Union (ZANU) during the conflict against the white-minority government of Ian Smith. Mugabe was a political prisoner in Rhodesia for more than 10 years between 1964 and 1974.[2] Upon release Mugabe, along with Edgar Tekere, left Rhodesia in 1975 to re-join the fight during the Rhodesian Bush War from bases in Mozambique.
At the end of the war in 1979, Mugabe emerged as a hero in the minds of many Africans.[3][4] He won the general elections of 1980, the second in which the majority of black Africans participated. (The electoral system in Rhodesia had allowed black participation based on qualified franchise). Mugabe became the first Prime Minister after calling for reconciliation between formerly warring parties, including white Rhodesians and rival political groups.
The years following Zimbabwe's independence saw a split between the two key parties who had fought alongside each other during the 1970s against the white minority rulers of Rhodesia. An armed conflict between Mugabe's government and followers of Joshua Nkomo's ZAPU erupted. Following the deaths of thousands, with neither faction able to defeat the other, the parties reached a landmark agreement leading to the creation of a new party, ZANU PF, a coalition between the two former rivals.[5]
In 1998, Mugabe's government supported the Southern African Development Community's intervention in the Second Congo War by sending Zimbabwean troops to assist the government of Laurent-Désiré Kabila. Some commentators called Zimbabwe's intervention a tactic to bolster its economy by controlling the Congo's natural resources.[6]'''
app = Flask(__name__)


URLA = "https://mykey:mykey@api.datamarket.azure.com/Bing/Search/Web?$format=json&Query=%(q)s"
API_KEY = 'WdxgHLzMYWAsYipg/tv/RpK1mFk5YhuFeLQZxH2I1Uw'
URLI = "https://mykey:mykey@api.datamarket.azure.com/Bing/Search/Image?$format=json&Query=%(q)s"

program = ['programmer','programming','coding','coder','Java','C++','Python']
actor = ['film','actor','movie', 'TV show','acting']
science = ['physic','chemist','science','discovered','invent']
business = ['entrpreneu','company','investor','startup']
politician = ['politic']

def sent(ghjui):
    case =[]
    tey = ''.join(ghjui)
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', tey)
    #print sentences
    for i in sentences:
        case.append(i)
    #print case
    return case

def requester(que, **params):
    que = ('%27'+que+ '%27')
    r = requests.get(URLA % {'q': que}, auth=('', API_KEY))
    return [res['Url'] for res in r.json()['d']['results']]

def birth(sente):
    birth_day = ''
    birth_month = ''
    birth_year = ''
    count1 = 0
    count2 = 0
    count3 = 0
    months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    birth_month =''
    if ('born') in sente:
       sents = word_tokenize(sente)
       print "yoyoa"
       for sets in sents:
            for mon in months:
                if (mon ==sets) and (count1==0):
                    birth_month = mon
                    count1 = 1
                    for  se in sents:
                        if se.isdigit() is True:                        
                            if (len(se) is 2) and (count2==0):
                               birth_day = se
                               count2 = 1

            if sets.isdigit() is True:
                if (len(sets) is 4) and (count3==0):
                    birth_year= sets
                    count3 = 1
            
    borf = birth_day + " " + birth_month + ' ' + birth_year
    return borf


def asky(te):
    sentences = sent_tokenize(te)
    collections_tokens = word_tokenize(te)
    collection_counter = Counter(collections_tokens)
    sent_saliences = []
    scored_sents = []
    num_to_extract = 1
    print "fdg"
    for index, sentence in enumerate(sentences):
        sent_salience = 0
        sent_tokens = word_tokenize(sentence)
        sent_counter = Counter(sent_tokens)
        for token in sent_tokens:
            tf = sent_counter[token]
            idf = log10(len(sentences) / sent_counter[token])
            tfidf = tf * idf
            sent_salience += tfidf
        normalized_salience = sent_salience / len(sent_tokens)
        sent_saliences.append(normalized_salience)
        scored_sents.append((normalized_salience, sentence, index))

    scored_sents.sort(key=lambda tup: tup[0], reverse=True)
    selected_sents = sorted(scored_sents[:num_to_extract], key=lambda tup: tup[2])
    return '%s' % (' '.join([i[1] for i in selected_sents]))

def check_for_div_parent(mark):
    mark = mark.parent
    if 'div' == mark.name:
        return True
    if 'html' == mark.name:
        return False
    return check_for_div_parent(mark)


def imagery(imaa, **params):
    print "Yolo"
    print imaa
    r = requests.get(URLI % {'q': imaa}, auth=('', API_KEY))
    g = r.json()['d']['results']
    print g[0]['Thumbnail']
    return g[0]['Thumbnail']['MediaUrl']

def splitParagraphIntoSentences(paragraph):
    import re
    sentenceEnders = re.compile('[.!?][\s]{1,2}(?=[A-Z])')
    sentenceList = sentenceEnders.split(paragraph)
    return sentenceList
    if __name__ == '__main__':
        mylist = []
        sentences = splitParagraphIntoSentences(text)
        for s in sentences:
            mylist.append(s.strip())
            for i in mylist:
                print i

def Ti(enter):
    sentence = nltk.word_tokenize(enter)
    sent = pos_tag(sentence)
    alpha = [s for s in sent if s[1] == 'NN'  ]
    for i in range(0,len(alpha)-1):
       for ss in wn.synsets(alpha[i][0]): # Each synset represents a diff concept.
          syno.extend(ss.lemma_names)
          word_counter = {}
    newm =[]
    for i in range(0,len(alpha)-1):
        newm.append (alpha[i][0])

    counts = defaultdict(int)
    for x in newm:
        counts[x]+=1
    #print counts
    popular_words = sorted(counts, key = counts.get, reverse = True)   
    top = popular_words[:8]
    #print top
    results = []
    for i in range(0, len(top)-1):
        indx = sentence.index(top[i])
        results.append(" ".join(sentence[indx-1:indx+2]))
    return results

@app.route('/')
def hello():
    return ''' <a href= /about>About</a>
                <center><br><br><img src="https://lh5.googleusercontent.com/-MISGJsdATlo/Ufo2xq2lGfI/AAAAAAAAAbk/3lG9hKOSN5A/w500-h229-no/PaceByte.png" width = 500px><br><br>
                <font size =4 style = Trajan>The Research Engine</font>
                <br><br><br>

                
                <head>
		<meta name="msvalidate.01" content="C0A6DA20A34D64388F0FA37AD2028052" />
                </head>
                
                <form method="POST" action="/people">
                    <font size = "4">I am looking for?</font><br>
                    <font size = 2>Please enter atleast two words. </font><br><br>
                    <input name="search" type="text" width=1000px>
                    <br>
                    <input type="submit" value="People Search"/>
                    <br>
                </form>
                        <br>
                        <br><br>
                     <br>
                     <br>
                     <br>
                     <br>
                     <br>
                     Please send your feedback to: <a href="mailto:'admin@pacebyte.com'">admin@pacebyte.com</a>
                     <script>
                      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                          ga('create', 'UA-42935531-1', 'pacebyte.com');
                          ga('send', 'pageview');

                </script>
                </center>
              </form>'''

@app.route('/about')
def About():
    return '''<html>
                <center>
            
            <img src="https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png" width = 500px>
                <br><br><h1> About</h1>
                <body> 
                <font size = 4> PaceByte is an online data mining and aggregation tool that generates write-ups using information available on the internet.
                <script>
                  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
                     (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
                      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                      })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

                      ga('create', 'UA-42935531-1', 'pacebyte.com');
                      ga('send', 'pageview');

                </script>
                    <br>

                 </body>

                </center> '''


@app.route('/people', methods=['POST'])
def PeopleSearch():
    try:
        name = request.form.get('search')
        print (name)
        name = name.title()
        name_s = name.split()
        al = len(name_s)
        if (al < 2):
            return "You need to enter atleast two words"
        for x in range (0,7):
            if profanity[x] in (name):
                return ("We will not process that")
        
        
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    
        print "tioj"
          
        adjEdu = ['school','educa,','university','colleg','scholar','merit','young','teenag','years']
        ael = (len(adjEdu)-1)
        adjCareer = ['worked','discovered','wrote','develop','business','money' ,'sell','won','invent','practiced','study','research','preside','govern','act']
        acl = (len(adjCareer)-1)
        query = name
        raw = query
        searchTerm = (raw)
        
        searchTerm = ('%27'+raw+'%27')
        print "Hi"
        picture = imagery(searchTerm)
        
        print "yu"
    except:
        pass

    #Imports Text
    bornc =0
    Education =""
    End = ("<font size = 1><center>The information provided on this webpage does not belong to Pace Byte and has been re-quoted from other website whose urls have been embedded in the headline of the articles</center></font>")
    Career =""
    print picture
    QuerySplit = query.split()
    print QuerySplit
    QSL = len(QuerySplit)
    print str(query)
    string = ("")
    summary = ""
    cli =0
    born =""
    summary = ""

    print QuerySplit[0]
    j = 0
    l = 0
    k = 0
    v = 0
    Abst = "Nothing Here"
    jet = " "
    
    #First Search
    cc = 0
    pc = 0
    sc = 0
    pp =0
    ss =0
    prof = "Profession: "
    borc = 0
    quer =('"' +name+ ' biography"')
    print (quer)
    o = requester(quer)
    #print o
    i = 0
    flag = 0
    Title = raw
    Heading = ("<img src='https://lh5.googleusercontent.com/-cjODD9V7AXI/UerIKznIVNI/AAAAAAAAAaU/dSi288GNIr4/w500-h229-no/PaceByte.png' width = 200px> + <center><font size = 14> " + raw + "</font><br><br><img src='" + picture + "' width =400px><br><a href = "+picture+ ">" + picture + "</a></center><br><br>")
    body = ""
    Main = ""
    for f in range(0,len(o)-1):
        if (f>10):
            break
        print "Going"
        url = o[f]
        print url
        if ('wikipedia') not in (url):              #Removes Wikipedia Entries
            if ('youtube') not in (url):
                try:
                    ourUrl = opener.open(url).read()
                except Exception,err:
                    continue
                soup = BeautifulSoup(ourUrl)
                for link in soup.findAll('a', href=True):
                        link.replaceWith(Comment(unicode(link)))
                try:
                    dem = soup.findAll('p')
                    tex = soup.title.string
                except:
                    continue
                Main = (Main + "<a href='" + url + "'>"+ "<font size = 4>" + tex +"</font>" +"</a><br><br>")
                
                backurl = " "
                URL = url
                
                try:
                    for i in dem:

                       #print i.text
                       if (i.text) not in Main:
                         for k in range (l ,QSL-1):
                             
                              if QuerySplit[k] in i.text:
                                if("@") not in i.text:
                                    if ("http") not in i.text:
                                                                          
                                        for a in range (0,ael):
                                            if adjEdu[a] in (i.text):
                                                if (i.text) not in (Education):
                                                    Education = (Education + i.text )
                                                    continue
                                        print "sdfg"
                                                
                                        for a in range (0,acl):
                                            if adjCareer[a] in (i.text):
                                                if (i.text) not in (Career):
                                                    Career = (Career + i.text)
                                                    continue
                                       
                                        print "zsf"      
                                        if ("born") in (i.text):
                                            try:
                                                a = sent(i.text)
                                                print a
                                                for i in range(0,len(a)-1):
                                                    if (("born") in a[i]) and (bornc == 0):
                                                        bory = birth(a[i])
                                                        summary = a[i] +". " +a[i+1]+"<br>" + summary
                                                        print "xvgzc"
                                                        bornc = 1
                                            except:
                                                continue
                                            
                                            
                                       
                                        
                                        Main = (Main  +"</center>"  + i.text+"</font><br>"+"</font>" +"<br><br></font>")
                                        deg = ""
                                        
                                        print "we done here"

                                        for c in program:
                                            if (c in i.text) and (cc==0):
                                                print "dfg"
                                                prof = prof +'Programmer, '
                                                cc=1
                                                
                                        for y in science:
                                            if (y in i.text) and (sc ==0):
                                                print "asdf"
                                                prof = prof + 'Scientist, '
                                                sc =1
                                                
                                        for t in actor:
                                            print "asfd"
                                            if (t in i.text) and (pc==0):
                                                prof = prof +'Actor, '
                                                pc =1
                                        for r in business:
                                            if (r in i.text) and (ss ==0):
                                              
                                                prof = prof + 'Business Man, '
                                                ss =1
                                                
                                        for w in politician:
                                            print "asfd"
                                            if (w in i.text) and (pp==0):
                                                prof = prof +'Politician, '
                                                pp =1

    
                    continue
                
                except Exception,err:
                    continue
    
    print "yayu"
    #summary = fgh
    Ed = ""
    a = splitParagraphIntoSentences(Education)
    
    for i in range (0,len(a)-1):
        for f in range (0,ael):
            if adjEdu[f] in (a[i]):
                Ed = (Ed + a[i] +"<br>")
                break
    print "kaku"
    ca = ""
    a = splitParagraphIntoSentences(Career)
    for i in range (0,len(a)-1):
        for f in range (0,acl):
            if adjCareer[f] in (a[i]):
                ca = (ca + a[i] +"<br>")  
                break

    summary = summary +'<br>' + prof
    
    
    string = (Heading +"<center><font size =4>" + bory +"</center></font><font size = 6 color = #0080FF><u>"+"Summary:<br>"+"</u></font>" +"<font size=4>"+summary + "</font><br><br>"
              + "<font size = 6 color = #0080FF><u>Early Life and Work:</u></font><br><font size=4>" +Ed + "</font><br><br>" + "<font size = 6 color = #0080FF><u>Career:</u></font><br><font size=4>"
              + ca + "</font><br><br>" + "<font size = 6 color = #0080FF><u>Main Content:</u></font><br><br>"+ Main + "<br><br>" + End)
    return (string)



@app.errorhandler(500)
def pageNotFound(error):
    nopage = ("<br><br><br><br><br><br>"+"<center><font size =6>Oops...your search timed out. Please refresh your page and try again.</font></center>")
    return (nopage)


app.run(host='localhost', port =8080)
