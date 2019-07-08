Tutorial from:  
    https://towardsdatascience.com/political-python-1e8eb46c1bc1

pip install pywin32

scrapy shell
>> fetch('https://www.congress.gov/congressional-record/116th-congress/browse-by-date')
>> response.xpath('//td/a[@target="_blank"]/@href').extract()

scrapy runspider script.py

Added ./data/
def save_pdf(self, response):
        path = './data/' + response.url.split('/')[-1]