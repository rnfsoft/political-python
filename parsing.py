from multiprocessing import Pool
import tika
from tika import parser
import glob
import os
import time

def tika_parser(file):
    content = parser.from_file(file)
    if 'content' in content:
        text = content['content']
    else:
        return

    text = str(text).replace('\n', '')
    text = text.encode('utf-8', errors='ignore')

    new_file = './data/txt/' + os.path.basename(file).split('.')[0] + '.txt' # ./data/txt/CREC-2019-01-03.txt

    with open(new_file, 'wb+') as f:
        f.write(text)

if __name__ == '__main__':
    start = time.time()
    files = glob.glob('./data/*.pdf') 
    pool = Pool()
    pool.map(tika_parser, files)
    print('Execution time: {}'.format(time.time()-start))