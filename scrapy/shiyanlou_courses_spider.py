#scrapy runspider shiyanlou_courses_spider.py -o data.json
#-o输出成一个data.json文件
#vim data.join即可查看

#scrapy.Spider类有默认的 start_requests，只提供需要爬取的 start_urls，默认的 start_requests 方法会根据 start_urls 生成 Request 对象

import scrapy

class ShiyanlouCoursesSpider(scrapy.Spider):
	name = 'Shiyanlou-courses'

	@property
	def start_urls(self):		#获取可迭代对象的网页
		url_tmpl = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
		return (url_tmpl.format(i) for i in range(1, 23))

	def parse(self, response):
		for course in response.css('div.course-body'):
			yield {
				'name': course.css('div.course-name::text').extract_first(),
				'description': course.css('div.course-desc::text').extract_first(),
				'type': course.css('div.course-footer span.pull-right::text').extract_first(),
				'student':course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d][^\d][^\d]*')
					}