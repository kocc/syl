import scrapy

class CourseItem(scrapy.Item):
	"""
	定义 Item 非常简单，只需要继承 scrapy.Item 类，将每个要爬取
    的数据声明为 scrapy.Field()。下面的代码是我们每个课程要爬取的 4个数据
	"""
	name = scrapy.Field()
	description = scrapy.Field()
	type = scrapy.Field()
	student = scrapy.Field()
