#spider 负责从网页上爬取数据
#Item 相当于一个包装盒，对爬取的数据进行标准化包装
#Pipeline则对Item进行这几项处理
'''
Pipeline 对 Item 进行这几项处理：
	验证爬取到的数据 (检查 item 是否有特定的 field)
	检查数据是否重复
	存储到数据库
'''

#编写的ShiyanlouPipeline默认是关闭状态，要开启的话需要在setting.py对下面一行进行取消注释的修改
#67 ITEM_PIPELINES = {'shiyanlou.pipeline.ShiyanlouPipeline':300} 这个字典中key表示pipeline的位置，value是开启多个pipeline时它的执行顺序。数值越小越先执行。

from sqlalchemy.orm import sessionmaker
from shiyanlou.models import Course, engine

class ShiyanlouPipeline(object):
	def process_item(self, item, spider):
		"""
		parse 出来的 item 会被传入这里，这里编写的处理代码会作用到每一个 item 上面。
		这个方法必须要返回一个 item 对象
		"""
		#提取的学习人数是字符串，把它转换成 int
		item['students'] = int(item['students'])
		#根据 item 创建 Course Model 对象并添加到 session
		#item 可以当成字典来用，所以也可以使用字典解构, 相当于Course(name=item['name'],type=item['type'],...)
		self.session.add(Course(**item))
		return item

	def open_spider(self, spider):
		"""
		当爬虫被开启的时候调用
		此处创建数据库session
		"""
		Session = sessionmaker(bind=engine)
		self.session = Session()

	def close_spider(self, spider):
		"""
		当爬虫关闭的时候调用
		此处提交session再关闭session
		"""
		self.session.commit()
		self.session.close()