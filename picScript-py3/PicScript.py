#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from PIL import Image
import os
from PIL import ImageFile

# 报错后 google 了一下需要加这一句
ImageFile.LOAD_TRUNCATED_IMAGES = True

# 需要处理的文件夹,改你的文件夹的路径
folder = '/Users/sea/Desktop/0/'
# folder = '/Users/sea/Desktop/0/'

# 处理图片后输出的文件夹
outPath = '/Users/sea/Desktop/excellent/'
if not os.path.exists(outPath):  #如果不存在则创建一个
	os.makedirs(outPath)

# 处理后需要在次筛选的文件
outPath2 = '/Users/sea/Desktop/medium/'
if not os.path.exists(outPath2): 
	os.makedirs(outPath2)

# 处理图片的主程序
def picProcess(imagePath,n):

	#新增加一个数据，知道目前处理了多少张图片
	num = '第%d张' % n

	# 获取单张图片的宽和高
	img = Image.open(imagePath)
	width,height = img.size
	# print('Width = %s , Height = %s' % (width,height))

	# 输出的路径和名称
	path = outPath + imagePath
	path2 = outPath2 + imagePath

	# 按照比例缩放的计算
	newHeight = int((1125 * height) / width)
	newWidth = int((2436 * width) / height)

	#当处理图片库的时候出现 bug，关于 RGBA与RGB转换的
	if img.mode in ('RGBA', 'LA'):
	    img = img.convert('RGB')

	#设置一些规则过滤筛选图片,输出到不同的文件夹。
	if width >= 1125 and height >= 2436 and width < height:
		img = img.resize((1125,newHeight),Image.LANCZOS)
		print(num,imagePath, img.size[1] , '以宽1125进行缩小','%.4f ' % (height/width))
		img.save(path)	#图片非常优秀，进入excellent文件夹
	elif width >= 1125 and height >= 2436 and width > height:
		img = img.resize((newWidth,2436),Image.LANCZOS)
		print(num,imagePath, img.size[0] , '以高为2436进行缩小','%.4f ' % (height/width))
		img.save(path,quality=85)	#图片非常优秀，进入excellent文件夹
	elif 1000 < width < 1125 or 1900 < height < 2436 :
		print(num,imagePath , '保存到2号文件夹，待操作')
		img.save(path2,quality=80)	#图片中等，进入人工筛选状态
	elif width <= 1000 or height <= 1900:
		print(num,imagePath , "不操作，删除")
		pass	#图片质量低，直接删除
	# print( imagePath + ' save is done')

# 遍历文件夹里的图片然后循环
def runScript():

	#改变当前工作目录到指定的路径:图片的列表文件夹
	os.chdir(folder)

	n = 0

	#for in遍历文件夹,os.listdir()方法用于返回指定的文件夹包含的文件或文件夹的名字的列表
	for image in os.listdir(os.getcwd()):	#os.getcwd()方法用于返回当前工作目录
		# print(image)
		n = n + 1
		#只识别图片格式，忽略其它文件,把 image 分割成文件名和后缀名
		imageType = os.path.splitext(image)[1]
		# print(imageType,image)

		#如果文件夹内的文件是以下格式则运行
		if imageType == '.jpg' or imageType == '.JPG' or imageType == '.jpeg' or imageType == '.PNG':
			
			# print(image)
			picProcess(image,n) #执行封装好的压缩程序		

if __name__ == '__main__':
	runScript()

#-*- MAX Young 2019-4-17  -*-