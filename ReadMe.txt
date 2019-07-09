References:  
    https://towardsdatascience.com/political-python-1e8eb46c1bc1
    https://github.com/chrismattmann/tika-python
    https://stackoverflow.com/questions/55298505/spacy-update-msvc-not-found --> Installed 64bit Python

pip install pywin32

scrapy shell
>> fetch('https://www.congress.gov/congressional-record/116th-congress/browse-by-date')
>> response.xpath('//td/a[@target="_blank"]/@href').extract()



Added ./data/
def save_pdf(self, response):
        path = './data/' + response.url.split('/')[-1]

scrapy runspider script.py # scrap and download pdfs
python parsing.py # parsing texts from pdfs then save txt files to ./data/txt/
python extract.py # Sentiment Analysis




