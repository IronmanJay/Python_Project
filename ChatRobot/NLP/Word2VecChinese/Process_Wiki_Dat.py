#!/usr/bin/envpython
#‐*‐coding:utf‐8‐*‐
#process_wiki_data.py用于解析XML，将XML的wiki数据转换为text格式

import logging
import os.path
import sys

from gensim.corpora import WikiCorpus

if name=='main':
    program=os.path.basename(sys.argv[0])
    logger=logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running%s"%''.join(sys.argv))

    #checkandprocessinputarguments
    if len(sys.argv)<3:
        print (globals()['__doc__']%locals())
        sys.exit(1)
    inp,outp=sys.argv[1:3]
    space = " "
    i=0

    output=open(outp,'w')
    wiki=WikiCorpus(inp,lemmatize=False,dictionary={})
    for text in wiki.get_texts():
        output.write(space.join(text)+"\n")
        i=i+1
        if(i%10000==0):
            logger.info("Saved"+str(i)+"articles")

    output.close()
    logger.info("FinishedSaved"+str(i)+"articles")