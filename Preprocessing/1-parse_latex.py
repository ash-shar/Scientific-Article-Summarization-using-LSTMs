from __future__ import print_function
import latexwalker
import latex2text
import codecs
from pprint import pprint
import os

import sys
from plasTeX.TeX import TeX
from plasTeX.Renderers.XHTML import Renderer

# basepath = "/home/du3/13CS30043/Papers_folder/"
basepath = sys.argv[1]
destpath = sys.argv[2]



def main():

	folders = os.listdir(basepath)

	if not os.path.exists(destpath):
		os.makedirs(destpath)

	err_cnt = 0

	i = 0

	# file = codecs.open(basepath,'r','utf-8')

	# s = file.read()
	# parsed_text = latex2text.latex2text(s.encode('ascii','ignore').decode('ascii'), main_doc = True, path = basepath+'/'+)

	# destfile = codecs.open("test.txt",'w','utf-8')

	# print(parsed_text,file=destfile)

	for foldername in folders:
		files = os.listdir(basepath+foldername)
		text = ""
		destfile = codecs.open(destpath+foldername+'.txt','w','utf-8')
		for filename in files:
			if filename.endswith('.tex'):
				try:
					file = codecs.open(basepath+foldername+'/'+filename,'r','utf-8')
					s = file.read()
					parsed_text = latex2text.latex2text(s.encode('ascii','ignore').decode('ascii'), main_doc = True, path = basepath+foldername)
					text = text+parsed_text
				except:
					print('Error',foldername,filename)
					err_cnt+=1
				print(foldername,filename)
		print(text,file=destfile)

	print("Parsing Complete")
				


if __name__ == "__main__":main()