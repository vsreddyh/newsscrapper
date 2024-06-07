import scrapy
from news.items import NewsItem

class NewsspiderSpider(scrapy.Spider):
    name = "newsspider"
    allowed_domains = ["www.bbc.com"]
    start_urls = ["https://www.bbc.com/news"]
    custom_settings = {
        'FEEDS': { 'data.csv': { 'format': 'csv',}}
        }
    def start_requests(self):
        url = "https://www.bbc.com/news"
        yield scrapy.Request(url, callback=self.first_select)
    def first_select(self, response):
        x=response.xpath("//*[@id='__next']/div/nav[2]/nav/ul/li[1]/div/a/@href").get()
        section=response.xpath("//*[@id='__next']/div/nav[2]/nav/ul/li[1]/div/a/text()").get()
        yield response.follow(x, callback=self.parse, meta={'section':section})
    def parse(self, response):
        txt=response.meta['section']
        if txt!="BBC Verify":
            for i in range(1,11):
                if i==5:
                    continue
                article = NewsItem()
                article["Section"]=txt
                a=response.xpath("//h2[text()='Latest updates']/parent::div/parent::div/following-sibling::div/div[1]")
                # print(a,"lollllll")
                article["Headline"]=a.xpath("div["+str(i)+"]/div/a/div/div[2]/div[2]/div[1]/div/h2/text()").get()
                article["Date"]=a.xpath("div["+str(i)+"]/div/a/div/div[1]/div/span/text()").get()
                article["Description"]=a.xpath("div["+str(i)+"]/div/a/div/div[2]/div[2]/p/text()").get()
                article["Link"]=a.xpath("div["+str(i)+"]/div/a/@href").get()
                yield article
                section_link = response.xpath("//a[contains(@class, 'yKcKi') and contains(@class, 'eZqXkk')]/ancestor::li/following-sibling::li/div/a/@href").get()
                section_text = response.xpath("//a[contains(@class, 'yKcKi') and contains(@class, 'eZqXkk')]/ancestor::li/following-sibling::li/div/a/text()").get()
                yield response.follow(section_link, callback=self.parse, meta={'section': section_text})
        pass