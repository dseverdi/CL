"""
Python wrapper for SS-F API calls:
    https://ss-framework.com
    
# ToDO:
REST API
"""

import requests
import nltk
import json
import spacy
from spacy import displacy

# MACROS
# universal POS tags:
POS_TAG = {
    "pridjev" : "ADJ", # adjective
    "prijedlog": "ADP", # prijedlog
    "prilog": "ADV",
    "pomocni": "AUX",
    "veznik": "CCONJ",
    "yyy": "DET", # determinant
    "xxx": "INTJ", # interjunction
    "imenica": "NOUN",
    "broj": "NUM",
    "čestica": "PART",
    "zamjenica": "PRON",
    "vlastita": "PROPN",
    "interpunkcija": "PUNCT",
    "zzz": "SCONJ", # subordinating conjuction
    "simbol": "SYM",
    "glagol": "VERB",
    "nlo": "x"    
}

CODE_OK = 200

# SSF code 
api_url = "http://ss-framework.com/api/fpj"
key = "429ae4bfe8088f071abef86ac021653b"

# supported languages (only: hr)
languages = ['hr','eng','de']


# Data container
class Doc:
    def __init__(self):
        self._text = ''
        self._tokens = []
        self._tags   = []
        self._size   = 0
        
    def __iter__(self):
        """ Iterate over (token,tag) objects """
        for i in range(self._size):
            yield (self._tokens[i],self._tags[i])
        
    def render(self,backend='spaCy'):
        data = {}
        data['words'],data['arcs'] = [],[]
        
        for token in self:
            data['words'].append({'text':token[0], 'tag': token[1] })
            
        displacy.render(data, style='dep',jupyter=True,manual=True)
        
  
    
# text-processing client program for SSF
class ssf:
    """
    REST interface to ss-framework.
    """
    # constructors
    def __init__(self,lang='hr',interface='Python'):
        self.lang = lang
        self.interface = interface        
     
    
    # API specific
    def _query(self,code):
        """
            API access
        """             
        r = requests.post(api_url, data = {'apiKey':key, 'program':self.interface, 'code':code})
        r.encoding = 'utf-8'
        return r.json() if r.status_code == requests.codes.ok else None   
    
    def _response(self,api_call):
        resp = self._query(api_call)
        return resp['result'] if resp['status']==CODE_OK else None
    
    
class POSTagger(ssf):
    def __init__(self,lang='hr',interface='Python'):
        ssf.__init__(self,lang,interface)  
        
        
    @classmethod
    def load(cls,lang):
        return POSTagger(lang) if lang in languages else POSTagger()
            
    # callable    
    def __call__(self,text):
        """
           callable interface.           
        """
        
        doc = Doc()
        doc._text    = text
        doc._tokens  = self.Tokenizer(text)
        doc._tags    = self.Tagger(text)        
        doc._size    = len(doc._tokens)
        
        return doc


    
    def Tokenizer(self,text):
        """
            split sentences into words.
        """        
        tokens = nltk.word_tokenize(text)
        return tokens 
    
    
    def Tagger(self,sentence,tags='uPOS'):
        """
        POS Tagger based on SSF Gets function
        """
        # normalize sentence
        sentence = sentence.lower() # toDo ...
        if tags == 'uPOS': 
            code = u"=Gets({!r},{!r})".format(sentence,'Vrsta riječi')
        else: 
            pass
        
               
        # tags = response['result'] if response['status']==CODE_OK else None
        tags = self._response(code)
        tags = tags.lower().split(' ')
        
        return list(map(POS_TAG.get,tags))
    
    
        

    
    
    
if __name__ == '__main__':
    print('Testing SSF interface...')
    # SSF interface
    nlp = POSTagger.load('hr') # HR only supported
    # data   
   
    doc = nlp('Novinari su prenijeli lošu vijest.') 
    for item in doc:
        print(item)
        
        
  
    
    

    