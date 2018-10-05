from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from docx import Document
from docx.shared import Inches
import docx
import re, datetime
from io import StringIO
#Offer letter Md.docx
ts = []

def getText(filename):
	doc = docx.Document(filename)
	fullText = []
	for para in doc.paragraphs:
		fullText.append(para.text)
	return '\n'.join(fullText)

def times(s,i=0):
	if i == -1:
		return ts

	s=s[i:]
	try:
					match = re.search('\d{2} : \d{2}', s)
					ts.append(match.group())
					i = s.index(match.group())
					i=i+5
	except:
		try:
					match = re.search('\d{2}:\d{2}', s)
					ts.append(match.group())
					i = s.index(match.group())
					i=i+5
		except:
			try:
					match = re.search('\d{1}:\d{2}', s)
					ts.append(match.group())
					i = s.index(match.group())
					i=i+5

			except:
				i=-1

	return times(s=s,i=i)
					



def challan( request ):
	print("Unknwny here")
	if request.method == 'POST' and request.FILES['later']:
		myfile = request.FILES['later']
		print("FileSystemStorage")
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		s7=s=getText(filename)

		t=0
		ts=[]

		s0=s
		date="Not Mentioned"
		try:
					match = re.search('\d{2}/\d{2}/\d{4}', s)
					date = match.group()
		except:
			try:
				match = re.search('\d{2}-\d{2}-\d{4}', s)
				date = match.group()
			except:
				try:
					match = re.search('\d{4}/\d{2}/\d{2}', s)
					date = match.group()
				except:
					try:
						match = re.search(r'\d\d\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s\d{4}\s\d{2}:\d{2}', s)
						date = match.group()
					except:
						try:
							match = re.search(r'\d\d \w\w\w \d\d\d\d', s)
							date = match.group()
						except:
							try:
								match = re.search(r'\d\d \w\w \d\d\d\d', s)
								date = match.group()
							except:
								try:
									match = re.search('\d{4}-\d{2}-\d{2}', s)
									date = match.group()
								except:
									pass
		salary = "Not Mentioned"
		for c in ["$","₹"]:
			try:
						match = re.search('\d\d' + c,s)
						salary = match.group()
			except:
						try:
							match = re.search(' \d\d\d '+c+' ',s)
							salary = match.group()
						except:
							try:
								match = re.search(' '+c+' \d ',s)
								salary = match.group()
							except:
								try:
									match = re.search(' '+c+'\d* ',s)
									salary = match.group()
								except:
									try:
										match = re.search('\d '+c+' ',s)
										salary = match.group()
									except:
										try:
											match = re.search('\d*'+ c +' ',s)
											salary = match.group()
										except:
											try:
												match = re.search('\d{5,7}',s)
												salary = match.group()
											except:
												try:
													match = re.search('\d{2,3} \d{2,3}',s)
													salary = match.group()
												except:
													pass
		s=s7
		director = "Not Mentioned"
		try:
			m1=match = s.index('(Director)')
			match = s[:match]
			m2=match = s[:m1].rindex('\n')
			m2=match = s[:m2].rindex('\n')
			director = s0[m2+1:m1]
		except:
			pass

		person_name = "Not Mentioned"
		try:
			m1=match = s.index('Dear')+5
			match = s[match:]
			m2=match.index('\n')
			person_name = match[:m2]
		except:
			pass

		"""
		Company's Name,
		Job Title,

		Person's Name,
		Benefits Information,
		Agreements
		"""

		os.remove(filename)
		return render(request, 'dash_upload.html', {'uploaded_file_url': uploaded_file_url,
			'director':director, 'salary':salary,'times':times(s),'date':date,
			'person_name':person_name,
		})
	return render(request, 'dash_upload.html', {'foo': 'bar',})

def review( request ):
	return render(request, 'review.html', {
		'foo': 'bar',
			})
