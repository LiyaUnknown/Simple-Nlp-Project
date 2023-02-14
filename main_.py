from nltk import ne_chunk , word_tokenize , pos_tag
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import nltk

def test() : 
    # set grammer

    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    grammar = "NP: {<DT>?<JJ>*<NN>}"

    # work on sentences
    
    text = "what's the another word for python".lower()

    text_tok = nltk.word_tokenize(text)

    pos_tag = pos_tag(text_tok)

    chunk = ne_chunk(pos_tag)

    # extract the important words
    
    cp = nltk.RegexpParser(grammar)
    result = cp.parse(chunk)

    for word in result : 
        try : 
            if word[1] == "DT" or word[1] == "IN" or  word[1] == "NNS" or word[1] == "JJ" or word[1] == "JJS" or word[1] == "NNS" or word[1] == "NN" or word[1] == "JJR" or word[1] == "NNP" or word[1] == "NNPS" :
                if word[0].split("/")[0].strip() != "i" or word[0].split("/")[0].strip() != "im" : 
                    print(word[0].split("/")[0])
            for i in word[0::] :
                if i[1] == "DT" or i[1] == "IN" or i[1] == "NNS" or i[1] == "JJ" or i[1] == "JJS" or i[1] == "NNS" or i[1] == "NN" or i[1] == "JJR" or i[1] == "NNP" or i[1] == "NNPS" :
                    if i[0].strip() != "i" or i[0].strip() != "im" : 
                        print(i[0])
        except : 
            try : 
                for i in word[0::] :
                    if i[1] == "DT" or i[1] == "IN" or i[1] == "NNS" or i[1] == "JJ" or i[1] == "JJS" or i[1] == "NNS" or i[1] == "NN" or i[1] == "JJR" or i[1] == "NNP" or i[1] == "NNPS" :
                        if i[0].strip() != "i" or i[0].strip() != "im" :
                            print(i[0])
            except : 
                None
        print(" " )
test()
