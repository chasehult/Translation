# -*- coding: utf-8 -*-
print "Loading..."
import sys
import warnings
import random
import urllib2
import urllib
try:
    import Numbers
except:
    urllib.urlretrieve("https://raw.githubusercontent.com/chasehult/Translation/master/Numbers.py", "Numbers.py")
    import Numbers


present="\x68\x74\x74\x70\x3A\x2F\x2F\x75\x6E\x69\x63\x6F\x64\x65\x73\x6E\x6F\x77\x6D\x61\x6E\x66\x6F\x72\x79\x6F\x75\x2E\x63\x6F\x6D"


PROUNOUNCIATION={u"ā":"ay",u"â":"a",u"b":"b",u"d":"d",u"ē":"ee",u"ê":"e",
                 u"ə":"u",u"f":"f",u"g":"g",u"h":"h",u"ī":"iy",u"î":"i",
                 u"j":"j",u"ʒ":"zh",u"k":"k",u"l":"l",u"m":"m",u"n":"n",
                 u"ñ":"ny",u"ō":"oh",u"ô":"o",u"ó":"oo",u"p":"p",u"r":"r",
                 u"ᵲ":"rr",u"s":"s",u"t":"t",u"ū":"oo",u"û":"u",u"v":"v",
                 u"w":"w",u"y":"yu",u"z":"z",u"ʧ":"ch",u"ʃ":"sh",u"θ":"th",
                 u"ð":"edh",u"ʊ":"eauh"}
SUBS={u"":"sk",u"▀":"sl",u"▁":"sn",u"▂":"st",u"▃":"sp",u"▄":"sm",
          u"▅":"bl",u"▇":"kl",u"█":"br",u"▉":"fr",u"▊":"kr",u"▋":"gl",
          u"▌":u"pl",u"▍":"gr",u"▎":"tr",u"▏":"pr",u"▐":"kw",u"▓":"ks"}                

VOWELS=u"āâēêəīîōôóūûʊ"  # 13
CONS=u"bdfghjklmnprstvwyzʒᵲʧñʃθð"  # 26


def to_galbraithanese(word):
    global VOWELS
    global CONS
    global SUBS
    try:
        word=unicode(word.lower())
    except:
        word=word.lower()
    word=word.replace("ch",u"ʧ")
    if random.random()>.5:
        word=word.replace("c","k")
    else:
        word=word.replace("c","s")
    if random.random()>.5:
        word=word.replace("sh",u"ʒ")
    else:
        word=word.replace("sh",u"ʃ")
    if random.random()>.5:
        word=word.replace("n",u"ñ")
    if random.random()>.5:
        word=word.replace("th",u"θ")
    else:
        word=word.replace("th",u"ð")
    if random.random()>.5:
        word=word.replace("r",u"ᵲ")
    word=word.replace("q","kw")
    word=word.replace("x","ks")
    
    if random.random()>.5:
        word=word.replace("a",u"ā")
    else:
        word=word.replace("a",u"â")
    if random.random()>.333:
        word=word.replace("e",u"ē")
    elif random.random()>.5:
        word=word.replace("e",u"ê")
    else:
        word=word.replace("e",u"ə")
    if random.random()>.5:
        word=word.replace("i",u"ī")
    else:
        word=word.replace("i",u"î")
    if random.random()>.5:
        word=word.replace("oo",u"ó")
    else:
        word=word.replace("oo",u"î")
    if random.random()>.5:
        word=word.replace("o",u"ʊ")
    else:
        word=word.replace("o",u"ô")
    if random.random()>.5:
        word=word.replace("u",u"ū")
    else:
        word=word.replace("u",u"û")
        
    for item in SUBS:
        word=word.replace(SUBS[item], item)
        
    addedvowels=""
    addedcons=""
    for letter in word:
        if letter in VOWELS:
            addedvowels+=letter*3
        elif letter in CONS+"".join(list(SUBS)):
            addedcons+=letter*3
        else:
            try:
                warnings.warn(u"Unknown letter \'"+letter+"\'!")
            except:
                warnings.warn(u"Unknown letter!")
    
    length=random.randint(7,9)
    if length==6 and random.random()<.5:
        upbound=.3
        length-=1
        while length!=1:
            if random.random()>upbound:
                break
            length-=1
            upbound/=9
    elif length==8:
        upbound=.5
        while True:
            if random.random()>upbound:
                break
            length+=1
            upbound/=2
    length=(length+len(word))/2
    v=not length%2
    if v and random.random()<0.7 and length>1:
        length+=random.choice([-1,1])
        v=not v
    elif v and length>1:
        length+=random.choice([-1,1])

    output=""
    while length>0:
        if v:
            output+=random.choice(VOWELS+addedvowels)
        else:
            output+=random.choice(CONS+"".join(list(SUBS))+addedcons)
        length-=1
        v=not v

    for item in SUBS:
        output=output.replace(item, SUBS[item])
    return output

    


class Translation:
    def __init__(self):
        try:
            open("ignore.txt")
        except:
            if open("galbraithanese_word.py").read()!=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/galbraithanese_word.py").read():
                i=raw_input("Your code is not up to date!\nWould you like to download the new one?\n(y/n)")
                if i=="y":
                    backup=open("galbraithanese_word.py").read()
                    try:
                        x=open("galbraithanese_word.py","r+")
                        x.truncate(0)
                        x.write(urllib2.urlopen("https://github.com/chasehult/Translation/blob/master/galbraithanese_word.py").read())
                        x.close()
                        print "Restart successful, please quit Python and reopen your file."
                    except:
                        warnings.warn("Update failed, will now try to revert to original.")
                        try:
                            x=open("galbraithanese_word.py","r+")
                            x.truncate(0)
                            x.write(backup)
                            x.close()
                            print "Reverted successfully.  Remember: It is still not updated, contact Chase or try again."
                        except:
                            warnings.warn("Reverted unsuccessfully.  Will now try to update on another file!")
                            try:
                                x=open("galbraithanese_word.py","r+")
                                x.truncate(0)
                                x.write("raise MemoryError(\"Corrupted File!\")")
                                x.close()
                            except:
                                try:
                                    x=open("galbraithanese_word.py","r+")
                                    x.truncate(0)
                                    x.close()
                                except:
                                    warnings.warn("Wow this file is really messed up!")
                            try:
                                urllib.urlretrieve("https://github.com/chasehult/Translation/blob/master/galbraithanese_word.py", "Newfile.py")
                                print "Update sort of worked, delete this file and rename Newfile.py to galbraithanese_word.py"
                            except:
                                warnings.warn("Update on new file failed, now trying to backup on new file!")
                                try:
                                    n=open("Newfile.py", "w")
                                    n.write(backup)
                                    n.close()
                                    print "Backup sort of worked, delete this file and rename Newfile.py to galbraithanese_word.py.   Remember: It is still not updated, contact Chase or try again."
                                except:
                                    warnings.warn("Nothing works, please contact Chase now.")
                                    raise IOError("Error. "*12)
                                   
        self.words=open("/usr/share/dict/words")
        try:
            self.trans=open("Translation.txt", "r+")
        except:
            urllib.urlretrieve("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt", "Translation.txt")
            self.trans=open("Translation.txt", "r+")
        self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")
        self.dictionary={}
        try:
            try:
                open("ignore.txt")
                self.readfromfile()
            except:
                if self.trans.read()!=self.trans2.read():
                    self.trans.close()
                    self.trans=open("Translation.txt", "r+")
                    self.trans2.close()
                    self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")
                    x=raw_input("Your translation document is different than the one on the web.  Would you like to read from the online one?  (y/n)")
                    if x=="y":
                        self.readfromdoc()
                        x=raw_input("Would you like to update your translation file?")
                        if x=="y":
                            self.save()
                    else:
                        self.readfromfile()
                self.trans.close()
                self.trans=open("Translation.txt", "r+")
                self.trans2.close()
                self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")
        except ValueError:
            warnings.warn("Could not read from doc!")
            self.readfromfile()
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
        self.trans2.close()
        self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")



    
    def printword(self,word):
        """Exactly the same as getword, but prints the word instead of returning it."""
        print self.getword(word)
        
    def getword(self, word):
        """Translates one word into Galbraithanese."""
        if all(map(lambda x: x.isdigit(), list(word))) and word:
            return Numbers.galbraithanese_number(int(word))
        elif set(list(word))==set(['\x98', '\x83', '\xe2']):
            return word
        elif word=="love":
            return random.choice(["óstīðōyó", "ᵲōsnôfôbr", "lēvēy", "jūkwôbr"])
        elif word=="loved":
            return random.choice(["óstīðōyóēnē", "ᵲōsnôfôbrēnē", "lēvēyēnē", "jūkwôbrēnē"])
        elif word=="loving":
            return random.choice(["óstīðōyóîgē", "ᵲōsnôfôbrîgē", "lēvēyîgē", "jūkwôbrîgē"])
        elif word in self.dictionary:
            return self.dictionary[word]
        elif word[:-2] in self.dictionary and word[-2:]=="ly":
            return self.dictionary[word[:-2]]+"əʃ"
        elif word[:-3]+"y" in self.dictionary and word[-2:]=="ily":
            return self.dictionary[word[:-3]+y]+"əʃ"
        elif word[:-3] in self.dictionary and word[-3:]=="ing":
            return self.dictionary[word[:-3]]+"îgē"
        elif word[:-3]+"e" in self.dictionary and word[-3:]=="ing":
            return self.dictionary[word[:-3]+"e"]+"îgē"
        elif word[:-2] in self.dictionary and word[-2:]=="ed":
            return self.dictionary[word[:-2]]+"ēnē"
        elif word[:-1] in self.dictionary and word[-1]=="d":
            return self.dictionary[word[:-1]]+"ēnē"
        elif word[:-1] in self.dictionary and word[-1]=="s":
            return self.dictionary[word[:-1]]+"glôb"
        elif word[:-2] in self.dictionary and word[-2:]=="es":
            return self.dictionary[word[:-2]]+"glôb"
        else:
            return "?"*len(word)

    def readfromdoc(self):
        """Forces the program to read off of the online translation."""
        self.dictionary={}
        for word in self.trans2.read().split("#######")[1].split():
            try:
                self.dictionary[word.split("-")[0]]=word.split("-")[1]
            except:
                pass
        self.trans2.close()
        self.trans2=urllib2.urlopen("https://raw.githubusercontent.com/chasehult/Translation/master/Translation.txt")

    def readfromfile(self):
        """Forces the program to read off of your translation file."""
        self.dictionary={}
        for word in self.trans.read().split("#######")[1].split():
            try:
                self.dictionary[word.split("-")[0]]=word.split("-")[1]
            except:
                pass
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
    
    def addword(self,word):
        """Adds a single english word to the dictionary and its translation is randomly chosen through to_galbraithanese."""
        self.dictionary[word]=to_galbraithanese(word)

    def removeword(self,word):
        """Removes a single word from the dictionary, the input word must be in english."""
        self.dictionary.pop(word)

    def restart(self):
        """Completely restarts and saves the translation file.  Every thing will be changed.  Also makes sure there are no homonyms.  ASK CHASE BEFORE USING!!"""
        self.trans.truncate(0)
        self.trans.write("#######\n")
        self.dictionary={}
        for word in list(set(self.words.read().lower().split("\n"))):
            translation=to_galbraithanese(word)
            while translation in self.dictionary.values():
                translation=to_galbraithanese(word)
            self.trans.write((word+"-"+translation+"\n").encode('utf8'))
            self.dictionary[word]=translation
            if len(list(self.dictionary))%1000==0:
                print str(len(list(self.dictionary)))+"/"+str(len(open("/usr/share/dict/words").readlines()))
        self.trans.write("#######")
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
        self.words=open("/usr/share/dict/words")

    def save(self):
        """Saves the current dictionary to the translation file."""
        self.trans.truncate(0)
        self.trans.write("#######\n")
        for word in self.dictionary:
            self.trans.write((word+"-"+self.dictionary[word]+"\n"))
        self.trans.write("#######")
        self.trans.close()
        self.trans=open("Translation.txt", "r+")
        
    def gettranslation(self, word):
        """Translates a single galbraithanese word into english."""
        try:
            return str(Numbers.from_galbraithanese(word))
        except:
            pass
        if word in ["óstīðōyó", "ᵲōsnôfôbr", "lēvēy", "jūkwôbr"]:
            return "love"
        elif word in ["óstīðōyóēnē", "ᵲōsnôfôbrēnē", "lēvēyēnē", "jūkwôbrēnē"]:
            return "loved"
        elif word in ["óstīðōyóîgē", "ᵲōsnôfôbrîgē", "lēvēyîgē", "jūkwôbrîgē"]:
            return "loving"
        else:
            for eng in self.dictionary:
                if self.dictionary[eng]==word:
                    return eng
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="ēnē":
                    if eng[-1]=="e":
                        return eng+"d"
                    return eng+"ed"
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="îgē":
                    if eng[-1]=="e":
                        return eng[:-1]+"ing"
                    return eng+"ing"
                elif self.dictionary[eng]==word[:-4] and word[-4:]=="əʃ":
                    if eng[-1]=="y":
                        return eng[:-1]+"ily"
                    return eng+"ly"
                elif self.dictionary[eng]==word[:-5] and word[-5:]=="glôb":
                    if eng[-1]=="s":
                        return eng[:-1]+"es"
                    return eng+"s"
            return "?"*len(word)


    def fulltranslate(self, sentence):
        """Fully and correctly translates an english word into galbraithanese.  Warning:  Incomplete."""
        def trymost(word):
            try:
                return gettranslation(word)
            except:
                return False
        def trynoun(word):
            if word[-3:]=="ób":
                case="nom"
                word=word[:-3]
            elif word[-5:]=="îgē":
                case="gen"
                word=word[:-5]
            elif word[-5:]=="ûbē":
                case="dat"
                word=word[:-5]
            elif word[-5:]=="ōbō":
                case="acc"
                word=word[:-5]
            elif word[-5:]=="óló":
                case="abl"
                word=word[:-5]
            else:
                return False
            if word[-4:]=="nôb":
                num="non"
                word=word[:-4]
            elif word[-5:]=="trôb":
                num="sin"
                word=word[:-5]
            elif word[-5:]=="flôb":
                num="bil"
                word=word[:-5]
            elif word[-5:]=="glôb":
                num="plu"
                word=word[:-5]
            else:
                return False
            prefix=""
            suffix=""
            try:
                if case=="gen":
                    prefix="of the "
                if num in ["non", "bil", "plu"]:
                    suffix="s"
                return prefix+self.gettranslation(word)+suffix
            except:
                return False
        def tryadjective(word):
            if word[-4:]=="əʃ":
                return tryadjective(word[:-4])+"ly"
            try:
                return self.gettranslation(word)
            except:
                return False
        def tryadverb(word):
            if word[-4:]=="óθ":
                return trynoun(word[:-4])+"ful"
            try:
                return self.gettranslation(word)
            except:
                return False
        def tryverb(word):
            if word[-3:]=="ôk":
                try:
                    return "y'all need to "+self.gettranslation(word) if word[-6:]=="īpôk" else "you need to "+self.gettranslation(word)
                except:
                    return False
            if word[-2:]=="ó":
                try:
                    return "to "+self.gettranslation(word)
                except:
                    return False
            pro=False
            if word[-5:]=="îgē":
                pro=True
                word=word[:-5]
            if word[-5:]=="ēnē":
                tense="pas"
                word=word[:-5]
            elif word[-3:]=="ûb":
                tense="pre"
                word=word[:-3]
            elif word[-4:]=="ûgl":
                tense="fut"
                word=word[:-4]
            else:
                return False
            plu=False
            if word[-3:]=="īp":
                plu=True
                word=word[:-3]
            if word[-6:]=="ópóp":
                person=1
                word=word[:-6]
            elif word[-6:]=="ôbēb":
                person=2
                word=word[:-6]
            elif word[-3:]=="óf":
                person=3
                word=word[:-3]
            else:
                person=4
            perstr=[None, "we", "y'all", "they", "everyone"][person] if plu else [None, "I", "you", "they", "anyone"][person]
            try:
                ver=self.gettranslation(word)
            except:
                pass
            
                
            
            
    
    def custom_trans(self, word, trans):
        """Adds one english word to the dictionary with its specific galbraithanese translation."""
        self.dictionary[word]=trans

    def getsentencetranslation(self,sentence):
        """Translates a large chunk of galbraithanese into english."""
        newsentence=""
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        for word in newsentence.split():
            output.append(self.gettranslation(word))
        return self.keeppunct(sentence, " ".join(output))

    def printsentence(self,sentence):
        """Exactly the same as getsentence but prints the output."""
        print self.getsentence(sentence)

    def getsentence(self,sentence):
        """Translates a large chunk of english into galbraithanese."""
        newsentence=""
        sentence=sentence.replace("unicode snowman", "☃")
        sentence=sentence.replace("unicode snowmen", "☃☃☃")
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        for word in newsentence.split():
            output.append(self.getword(word))
        try:
            return self.keeppunct(sentence, " ".join(output))
        except:
            return " ".join(output)

    def keeppunct(self, old, new):
        """Keeps puncutation of a translated string.  Not really useful to use alone.  Is used in code."""
        punctdictionary={}
        oldspl=old.split()
        for x in range(len(oldspl)):
            if oldspl[x][-1] in ",?.!:;":
                punctdictionary[x]=oldspl[x][-1]
        newspl=new.split()
        for index in punctdictionary:
            newspl[index]+=punctdictionary[index]
        return " ".join(newspl)

    def getpronounciation(self, word):
        """Gives you the pronouciation of a sentence."""
        global VOWELS
        global CONS
        global PROUNOUNCIATION
        global SUBS
        try:
            if not any(map(lambda x: x=="?", list(self.getsentence(word)))):
                word=self.getsentence(word)
        except:
            pass
        word=unicode(word, 'utf-8')
        for item in SUBS:
            word=word.replace(SUBS[item], item)
        newword=u""
        for char in word:
            if char in VOWELS:
                newword+=PROUNOUNCIATION[char]+"-"
            elif char in CONS:
                newword+=PROUNOUNCIATION[char]
            else:
                newword+=char
        for item in SUBS:
            newword=newword.replace(item, SUBS[item])
        for char in " !?-.,\n\t\"\'(){}[]/":
            newword=newword.replace("-"+char, char)
        if newword[-1]==u"-":
            newword=newword[:-1]
        return newword

    def fullsentence(self, sentence):
        """Fully translates a sentence by asking a lot of questions.  Warning:  Not thoroughly tested."""
        def askquestion(question, answers):
            newanswers=""
            for x in range(len(answers)):
                newanswers+="\t"+str(x+1)+". "+answers[x]+"\n"
            x="asdf"
            while x not in map(lambda x: str(x+1), range(len(answers))):
                if x!="asdf":
                    print "Invalid answer"
                x=raw_input(question+"\n"+newanswers)
            return int(x)
            
        newsentence=""
        for letter in sentence.lower():
            if letter not in ",?.!:;":
                newsentence+=letter
        output=[]
        pro=""
        lastisto=False
        for word in newsentence.split():
            if word=="to":
                lastisto=True
                continue
            x=askquestion("The word \""+word+"\" is:", ["An article", "A noun", "An adjective", "A verb", "An adverb", "A conjunction", "A preposition", "An interjection", "A pronoun"])
            if x==1:  #Article
                pass   #Do nothing
            elif x==2:  #Noun
                x=askquestion("There are/is ___ of this noun (\""+word+"\"):", ["None", "One", "Two", "None of the above"])
                if x==1:  #Nonullar
                    number="nôb"
                elif x==2:  #Singular
                    number="trôb"
                elif x==3:  #Bilar
                    number="flôb"
                elif x==4:  #Plural
                    number="glôb"
                x=askquestion("The noun (\""+word+"\") is in the ___ case:", ["Nominative", "Genitive", "Dative", "Accusitive", "Ablative"])
                if x==1:  #Nom
                    case="ób"
                elif x==2:  #Gen
                    case="îgē"
                elif x==3:  #Dat
                    case="ûbē"
                elif x==4:  #Acc
                    case="ōbō"
                elif x==5:  #Abl
                    case="óló"
                works=False
                while not works:
                    x=raw_input("Please enter a simple form of the noun \""+word+"\" (ex. of the cats -> cat)")
                    try:
                        output.append(self.getword(x)+number+case)
                        works=True
                    except:
                        print "Even simpler"
            elif x==3:  #Adjective
                x=askquestion("Is the adjective \""+word+"\" formed from a noun?", ["Yes", "No"])
                if x==1:
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the noun that makes up the adjective \""+word+"\" (ex. windy -> wind)")
                        try:
                            output.append(self.getword(x)+"óθ")
                            works=True
                        except:
                            print "Even simpler"
                else:
                    output.append(self.getword(x))
            elif x==4:  #Verb
                isinf=False
                if lastisto:
                    x=askquestion("Is \"to "+word+"\" a full infinitive/to-infinitive?", ["Yes", "No"])
                    if x==1:
                        works=False
                        while not works:
                            x=raw_input("Please enter a simple form of the infinitive \""+word+"\" (ex. to run -> run)")
                            try:
                                isinf=True
                                output.append(self.getword(x)+"ó")
                                works=True
                            except:
                                print "Even simpler"
                    elif x==2:
                        output.append("to")
                isimp=True
                if not isinf:
                    x=askquestion("Is the verb \""+pro+word+"\" imperative?", ["Yes", "No"])
                    if x==1:
                        plural=["","","īp"][askquestion("Is the imperative verb \""+pro+word+"\" plural?", ["Yes", "No"])]
                        works=False
                        while not works:
                            x=raw_input("Please enter a simple form of the imperative \""+pro+word+"\" (ex. All of you, run! -> run)")
                            try:
                                output.append(self.getword(x)+plural+"ôk")
                                works=True
                            except:
                                print "Even simpler"
                    elif x==2:
                        isimp=False
                if not isimp and not isinf:
                    person=["","ópóp","ôbēb","óf"][askquestion("What person is the verb \""+pro+word+"\" in?", ["1st", "2nd", "3rd"])]
                    plural=["","īp",""][askquestion("Is the verb \""+pro+word+"\" plural?", ["Yes", "No"])]
                    tense=["","ēnē","ûb","ûgl"][askquestion("What tense is the verb \""+pro+word+"\" in?", ["Past", "Present", "Future"])]
                    progress=["","îgē",""][askquestion("Is the verb \""+pro+word+"\" progressive?", ["Yes", "No"])]
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the verb \""+pro+word+"\" (ex. I was running -> run)")
                        try:
                            output.append(self.getword(x)+person+plural+tense+progress)
                            works=True
                        except:
                            print "Even simpler"
                pro=""
            elif x==5:  #Adverb
                x=askquestion("Is the adverb \""+word+"\" an adjective with -ly or something added at the end?", ["Yes", "No"])
                if x==1:
                    works=False
                    while not works:
                        x=raw_input("Please enter a simple form of the adjective that makes up the adverb \""+word+"\" (ex. quickly -> quick)")
                        try:
                            output.append(self.getword(x)+"əʃ")
                            works=True
                        except:
                            print "Even simpler"
                else:
                    output.append(self.getword(word))
            elif x==6: #Conjunction
                output.append(self.getword(word))
            elif x==7: #Preposition
                output.append(self.getword(word))
            elif x==8: #Interjection
                output.append(self.getword(word))
            elif x==9: #Pronoun
                pro=word+" "
                continue
            if pro:
                output.insert(len(output)-1, pro[:-1])
                pro=""
            if lastisto:
                output.insert(len(output)-1, self.getword("to"))
        return " ".join(output)

    def rhyme(self, word, upto=6):
        """Gets all rhymes of a word.  Warning:  Each word has a lot of rhymes so this code might overload your idle interpreter."""
        upto=min(len(word), upto)
        if word in self.dictionary: word=self.getword(word)
        return filter(lambda x: x[-upto:]==word[-upto:], self.dictionary.values())
        
                
        

r="gâlbrāθənēz"
x=Translation()
tr="dətês vîᵲâr, jôʒóñ dûzūm prīfrēg ēgʊkʊ? sótəy ðūplēpr tēwōsm tôpləbr ksūʒūsl wêplîd lūzôgāg. grēskōt ʊdîkrū trôhîθōsnîh hāslākw bróʃîzīkl ksūʒūsl hāslākw yʊglūgēʃîgē klāʃódâʃūr. tûñâfr âwâzōbī, grēskōt ʊdîkrū kwəsnīblîr hêyôklāy ñīnâg Gâlbrāθənēz."
print "Done"

