import codecs
import re

#opening the sample text file, change the path accordingly.
filename='/home/shreemoyee/Desktop/Assign01_IR/hindi.txt'
f=codecs.open(filename,encoding='utf-8')
text=f.read()

print(text)

#Clean text

text=re.sub(r'(\d+)',r'',text)
text=text.replace(u',','')
text=text.replace(u'"','')
text=text.replace(u'(','')
text=text.replace(u')','')
text=text.replace(u'"','')
text=text.replace(u':','')
text=text.replace(u"'",'')
text=text.replace(u"‘‘",'')
text=text.replace(u"’’",'')
text=text.replace(u"''",'')
text=text.replace(u".",'')
text=text.replace(u"*",'')
text=text.replace(u"#",'')



#Split the sentences
sentences=text.split(u"।")
print(sentences)


#Tokenizing
sentences_list=sentences
tokens=[]
for each in sentences_list:
        word_list=each.split(' ')
        tokens=tokens+word_list

#Remove token with only space
for tok in tokens:
    tok=tok.strip()
#Remove hyphens in tokes
for each in tokens:
     if '-' in each:
            tok=each.split('-')
            tokens.remove(each)
            tokens.append(tok[0])
            tokens.append(tok[1])

print(len(tokens))

##Removing stop words, the txt file of stop words in the attachment, change path accordingly.
f=codecs.open("/home/shreemoyee/Desktop/Assign01_IR/stop_words.txt",encoding='utf-8')
'''if not self.stemmed_word:
     self.generate_stem_dict()'''
stopwords=[x.strip() for x in f.readlines()]
#tokens=[i for i in tokens if i not in stopwords]
final_tokens=tokens

print(len(tokens))

#Removing suffixes
'''We have included five steps, and within each step, rules are applied until one of them passes the conditions. If a rule is 
accepted, the suffix is removed accordingly, and the next step is performed. The resultant stem at the end of the 
fifth step is returned.''' 
suffixes = {
    1: [u"ो",u"े",u"ू",u"ु",u"ी",u"ि",u"ा"],
    2: [u"कर",u"ाओ",u"िए",u"ाई",u"ाए",u"ने",u"नी",u"ना",u"ते",u"ीं",u"ती",u"ता",u"ाँ",u"ां",u"ों",u"ें"],
    3: [u"ाकर",u"ाइए",u"ाईं",u"ाया",u"ेगी",u"ेगा",u"ोगी",u"ोगे",u"ाने",u"ाना",u"ाते",u"ाती",u"ाता",u"तीं",u"ाओं",u"ाएं",u"ुओं",u"ुएं",u"ुआं"],
    4: [u"ाएगी",u"ाएगा",u"ाओगी",u"ाओगे",u"एंगी",u"ेंगी",u"एंगे",u"ेंगे",u"ूंगी",u"ूंगा",u"ातीं",u"नाओं",u"नाएं",u"ताओं",u"ताएं",u"ियाँ",u"ियों",u"ियां"],
    5: [u"ाएंगी",u"ाएंगे",u"ाऊंगी",u"ाऊंगा",u"ाइयाँ",u"ाइयों",u"ाइयां"],
}

stems=[]
for word in tokens:
    for L in 5, 4, 3, 2, 1:
        if len(word) > L + 1:
             for suf in suffixes[L]:
                        #print(type(suf),type(word),word,suf)
                        if word.endswith(suf):
                            word=word[:-L]
    if word:
         stems.append(word)




#Write the stems in a file, change path accordingly.
filename=filename='/home/shreemoyee/Desktop/Assign01_IR/stems_generated.txt'
f=codecs.open(filename,"w",encoding='utf-8')
for stem in stems: 
        #print(stem)
        f.write(str(stem))
        f.write(u"\u0020")
f.close()












