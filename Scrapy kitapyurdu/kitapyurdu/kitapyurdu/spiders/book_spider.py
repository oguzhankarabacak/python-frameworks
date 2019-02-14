import scrapy

class BooksSpider(scrapy.Spider):
    name = "kitapyurdu"
    count=1
    page=0
    file=open("book.txt","a",encoding="utf-8")
    start_urls=[
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&list_id=6&filter_in_stock=1"
        ]
    def parse(self, response):
        
        author=response.css("div.product-grid div.author.compact.ellipsis a.alt::text").extract()
        publisher=response.css("div.product-grid div.publisher span a.alt span::text").extract()
        book_name=response.css("div.product-grid div.name.ellipsis a span::text").extract()
        
        i = 0
        while (i < len(book_name)):
            """yield {
                "name" : book_names[i],
                "author" : book_authors[i],
                "publisher" : book_publishers[i]
            }"""
            self.file.write("-----------------------------------------------\n")
            self.file.write(str(self.count) + ".\n")
            self.file.write("Kitap İsmi : " + book_name[i] + "\n")
            self.file.write("Yazar : " + author[i] + "\n")
            self.file.write("Kitap İsmi : " + publisher[i] + "\n")
            self.file.write("-----------------------------------------------\n")
            i +=1
            self.count +=1

        url=response.css("a.next::attr(href)").extract_first()
        self.page += 1

        if url is not None and self.page != 10:
            yield scrapy.Request(url = url,callback = self.parse)
        else:
            self.file.close()

        

        
        
