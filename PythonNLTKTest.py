import nltk
#from nltk.book import *
from nltk.corpus import genesis, brown, names, stopwords, PlaintextCorpusReader
from nltk.corpus import inaugural
from nltk.corpus import gutenberg
from urllib import request
from bs4 import BeautifulSoup
from nltk import PorterStemmer
from nltk import LancasterStemmer


#nltk.download("gutenberg")

def accessTextCorpora(fileid, word):
    # Write your code here
    wordcoverage = int(len(inaugural.words(fileid)) / len(set(inaugural.words(fileid))))
    edwords = [word1 for word1 in set(inaugural.words(fileid)) if word1.endswith('ed')]
    textfreq = [word2.lower() for word2 in inaugural.words(fileid) if word2.isalpha()]
    wordfreq = len([word3 for word3 in textfreq if word3 == word])
    return wordcoverage, edwords, wordfreq

def createUserTextCorpora(filecontent1, filecontent2):
    # Write your code here
    corpusdir = 'nltk_data/'
    with open(corpusdir + 'content1.txt', 'w') as text_file1:
        text_file1.write(filecontent1)
    with open(corpusdir + 'content2.txt', 'w') as text_file2:
        text_file2.write(filecontent2)
    text_corpus = PlaintextCorpusReader(corpusdir, ['content1.txt', 'content2.txt'])
    no_of_words_corpus1 = len(text_corpus.words('content1.txt'))
    no_of_unique_words_corpus1 = len(set(text_corpus.words('content1.txt')))
    no_of_words_corpus2 = len(text_corpus.words('content2.txt'))
    no_of_unique_words_corpus2 = len(set(text_corpus.words('content2.txt')))
    return text_corpus, no_of_words_corpus1, no_of_unique_words_corpus1, no_of_words_corpus2, no_of_unique_words_corpus2

#nltk.download('punkt')
#nltk.download('book')
#text = 'Python is an interpreted high-level programming language for general purpose programming. created by john...'
#sentences = nltk.sent_tokenize(text)
#print(len(sentences))
#words = nltk.word_tokenize(text)
#print(len(words))
#print(words[:5])

#text_l = [word.lower() for word in set(text1)]
#print(len(set(text_l)))
#print([word for word in set(text1) if len(word) > 17])
#print([word for word in set(text1) if word.startswith('Sun')])
#print(nltk.FreqDist(text1).most_common(5))
#uncommon_words = [word for word in text1 if word.isalpha() and len(word) > 7]
#print(nltk.FreqDist(uncommon_words).most_common(3))
#print(nltk.FreqDist(uncommon_words).total())
#print(len(set(text6)))
#print(len([word for word in text6 if word == 'ARTHUR']))

#print(genesis.fileids())


#cfd = nltk.ConditionalFreqDist([(genre, word)
#                                for genre in brown.categories()
#                                for word in brown.words(categories=genre)])
#print(cfd.conditions())
#cfd.tabulate(conditions=['government', 'humor', 'reviews'], samples=['leadership', 'worship', 'hardship'], cumulative = True)
#news_fd = cfd['news']
#print(news_fd.most_common(3))
#nt = [(fid.split('.')[0], name[-1])
#      for fid in names.fileids()
#      for name in names.words(fid)]
#cfd2 = nltk.ConditionalFreqDist(nt)
#print(sum([cfd2['female'][x] for x in cfd2['female']]) > sum([cfd2['male'][x] for x in cfd2['male']]))
#print(cfd2.tabulate(samples=['a', 'e']))


def calculateCFD(cfdconditions, cfdevents):
    # Write your code here
    stop_words = set(stopwords.words('english'))
    nt = [(genre, word.lower())
            for genre in cfdconditions
            for word in brown.words(categories=genre) if word not in stop_words and word.isalpha()]
    cdev_cfd = nltk.ConditionalFreqDist(nt)
    inged_cfd = [(genre, word)
            for genre in brown.categories()
            for word in brown.words(categories=genre) if (word.endswith('ing')) or (word.endswith('ed'))]
    inged_cfd = [list(x) for x in inged_cfd]
    for wd in inged_cfd:
        if wd[1].endswith('ing') and wd[1] not in stop_words:
            wd[1] = 'ing'
        elif wd[1].endswith('ing') and wd[1] not in stop_words:
            wd[1] = 'ed'
    inged_cfd = nltk.ConditionalFreqDist(inged_cfd)
    cdev_cfd.tabulate(conditions=cfdconditions,samples=cfdevents)
    inged_cfd.tabulate(conditions=cfdconditions,samples=['ed', 'ing'])


#url = "https://hrcdn.net/s3_pub/istreet-assets/2KDELtu3svGwJgNXUXFE7Q/001.txt"
#tok = nltk.regexp_tokenize('Python is cool!!!', r'\w+')
#print(len(tok))
#print(tok)
#content1 = request.urlopen(url).read()
#text_content1 = content1.decode('unicode_escape')
#tokens1 = nltk.word_tokenize(text_content1)
#print(tokens1[:])


def processRawText(textURL):
    # Write your code here
    textcontent = request.urlopen(textURL).read()
    tokenizedlcwords = nltk.word_tokenize(textcontent.decode('utf8'))
    tokenizedlcwords = [word1.lower() for word1 in tokenizedlcwords]
    noofwords = len(tokenizedlcwords)
    noofunqwords = len(set(nltk.word_tokenize(textcontent.decode('utf8').lower())))
    wordcov = int(noofwords / noofunqwords)
    wordfreq = nltk.FreqDist(tokenizedlcwords)
    maxfreq = wordfreq.max()
    print(noofwords, noofunqwords, wordcov, maxfreq)


#s = 'Python is an awesome language.'
#tokens = nltk.word_tokenize(s)
#print(list(nltk.ngrams(tokens, 4)))
#eng_tokens = genesis.words('english-kjv.txt')
#eng_bigrams = nltk.bigrams(eng_tokens)
#filtered_bigrams = nltk.FreqDist([(w1, w2) for w1, w2 in eng_bigrams if len(w1) >=5 and len(w2) >= 5])
#print(filtered_bigrams.most_common(3))
#eng_cfd = nltk.ConditionalFreqDist(eng_bigrams)
#print(eng_cfd['living'].most_common(2))
#gen_text = nltk.Text(tokens)
#print(gen_text.collocations())


def performBigramsAndCollocations():
    # Write your code here
    textcontent = 'Thirty-five sports disciplines and four cultural activities will be offered during seven days of competitions. He skated with charisma, changing from one gear to another, from one direction to another, faster than a sports car. Armchair sports fans settling down to watch the Olympic Games could be for the high jump if they do not pay their TV licence fee. Such invitationals will attract more viewership for sports fans by sparking interest among sports fans. She barely noticed a flashy sports car almost run them over, until Eddie lunged forward and grabbed her body away. And he flatters the mother and she kind of gets prissy and he talks her into going for a ride in the sports car.'
    word = 'sports'
    stop_words = set(stopwords.words('english'))
    tokenizedwords = nltk.tokenize.regexp_tokenize(textcontent, pattern='\w*')
    tokenizedwords = [word1.lower() for word1 in tokenizedwords if word1!= '']
    tokenizedwordsbigrams = nltk.bigrams(tokenizedwords)
    tokenizednonstopwordsbigrams = [(w1, w2) for w1, w2 in tokenizedwordsbigrams if (w1,w2) not in stop_words]
    cfd_bigrams = nltk.ConditionalFreqDist(tokenizednonstopwordsbigrams)
    mostfrequentwordafter = cfd_bigrams[word].most_common(3)
    collocationwords = nltk.Text(tokenizedwords).collocation_list()
    collocationwords = [i[0]+" "+i[1] for i in collocationwords]
    print(mostfrequentwordafter, collocationwords)


def performStemAndLemma(textcontent):
    # Write your code here
    pattern = r'\w*'
    stop_words = set(stopwords.words('english'))
    tokenizedwords = nltk.tokenize.regexp_tokenize(textcontent, pattern, gaps=False)
    filteredwords = [word1 for word1 in tokenizedwords if word1 != '']
    filteredwords = [word1.lower() for word1 in set(filteredwords) if word1 != '']
    filteredwords = [word1 for word1 in filteredwords if word1 not in stop_words]
    # print(filteredwords)
    porterstemmedwords = [nltk.PorterStemmer().stem(word1) for word1 in filteredwords]
    lancasterstemmedwords = [nltk.LancasterStemmer().stem(word1) for word1 in filteredwords]
    lemmatizedwords = [nltk.WordNetLemmatizer().lemmatize(word1) for word1 in filteredwords]
    return porterstemmedwords, lancasterstemmedwords, lemmatizedwords

def tagPOS():
    # Write your code here
    textcontent = 'Python is awesome.'
    taggedtextcontent = 'Python/NNP is/VBZ awesome/DT ./.'
    defined_tags = dict(brown.tagged_words(tagset='universal'))
    tagwords = nltk.word_tokenize(textcontent)
    nltk_pos_tags = nltk.pos_tag(tagwords)
    tagged_pos_tag = [nltk.tag.str2tuple(word1) for word1 in taggedtextcontent.split()]
    bt = nltk.UnigramTagger(model=defined_tags)
    unigram_pos_tag = bt.tag(tagwords)
    print(nltk_pos_tags, tagged_pos_tag, unigram_pos_tag)


