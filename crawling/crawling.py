#!/usr/bin/python3
#*-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

if __name__ == '__main__':

	url = u'https://github.com/trending/python?since=monthly'
	res = requests.get(url)

	html = BeautifulSoup(res.content,"html.parser")

	tag = html.find_all(attrs={'class': 'h3 lh-condensed'})
	for i in tag:
		temp=i.a.text.split()
		print(temp[2])	
	
		


