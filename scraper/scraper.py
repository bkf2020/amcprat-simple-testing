from bs4 import BeautifulSoup
from shutil import copyfile
import os
import fileinput
import requests
import re

tests = ["amc8", "amc10", "amc12", "aime"]

years = {}
years["amc8"] = range(2014, 2020 + 1)
years["amc10"] = range(2015, 2021 + 1)
years["amc12"] = range(2015, 2021 + 1)
years["aime"] = range(2015, 2021 + 1)

problems = {}
problems["amc8"] = range(1, 25 + 1)
problems["amc10"] = range(1, 25 + 1)
problems["amc12"] = range(1, 25 + 1)
problems["aime"] = range(1, 15 + 1)

types = {}
types["amc8"] = [""]
types["amc10"] = ["A", "B"]
types["amc12"] = ["A", "B"]
types["aime"] = ["I", "II"]

for test in tests:
	try:
		os.mkdir("./" + test)
	except:
		pass
	
	for year in years[test]:
		try:
			os.mkdir("./" + test + "/" + str(year))
		except:
			pass
		
		for test_type in types[test]:
			if(test_type != ""):
				try:
					os.mkdir("./" + test + "/" + str(year) + "/" + test_type)
				except:
					pass
			
			if(test == "amc8"):
				copyfile("problemsetamc8.html", test + "/" + str(year) + "/problemset.html")
			elif(test == "amc10" or test == "amc12"):
				copyfile("problemsetamc1012.html", test + "/" + str(year) + "/" + test_type + "/problemset.html")
			else:
				copyfile("problemsetaime.html", test + "/" + str(year) + "/" + test_type + "/problemset.html")
			
			URL = "https://artofproblemsolving.com/wiki/index.php/"
			URL += str(year) + "_"
			if(test == "aime"):
				URL += "AIME_" + test_type + "_Problems"
			elif(test == "amc8"):
				URL += "AMC_8" + "_Problems"
			elif(test == "amc10"):
				URL += "AMC_10" + test_type + "_Problems"
			elif(test == "amc12"):
				URL += "AMC_12" + test_type + "_Problems"
			
			page = requests.get(URL)
			soup = BeautifulSoup(page.content, 'html.parser')
			
			# use different img styles (scaling purposes):
			for img in soup.find_all(name="img"):
				try:
					if(img["style"][-1:] != ";"):
						img["style"] += ";"
					try:
						img["style"] += " width: calc(" + img["width"] + " * calc(1em/18));"
						del img["width"]
					except KeyError:
						continue
					try:
						img["style"] += " max-height: calc(" + img["height"] + " * calc(1em/18));"
						del img["height"]
					except KeyError:
						continue
				except KeyError:
					img["style"] = ""
					try:
						img["style"] += "width: calc(" + img["width"] + " * calc(1em/18)); "
						del img["width"]
					except KeyError:
						continue
					try:
						img["style"] += "max-height: calc(" + img["height"] + " * calc(1em/18));"
						del img["height"]
					except KeyError:
						continue
			
			solution_links = soup.find_all("a", text=re.compile("Solution"))
			
			for problem in problems[test]:
				if(test != "aime"):
					print("Creating " + str(year) + " " + test.upper() + test_type + " Problem #" + str(problem))
				else:
					print("Creating " + str(year) + " " + test.upper() + " " + test_type + " Problem #" + str(problem))
				
				file_name = str(problem) + ".html"
				if(1 <= problem and problem <= 9):
					file_name = "0" + str(problem) + ".html"
				
				f = open(test + "/" + str(year) + "/" + test_type + "/" + file_name, "w")
				
				f.write("<!DOCTYPE html>\n")
				f.write("<html>\n")
				f.write('<head>\n')
				f.write('\t<meta charset="utf-8">')
				f.write('\t<meta name="HandheldFriendly" content="true" />\n')
				f.write('\t<meta name="MobileOptimized" content="320" />\n')
				f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
				
				if(test == "amc8"):
					f.write('\t<link rel="stylesheet" href="../../../styleproblems.css">\n')
				else:
					f.write('\t<link rel="stylesheet" href="../../../../styleproblems.css">\n')
				
				f.write('</head>\n')
				f.write('<body>\n')
				f.write('\t<h1>AMCPRAT Problem</h1>\n')
				f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
				f.write('\t<hr/>\n')
				
				if(test != "aime"):
					f.write('\t<h2>' + str(year) + ' ' + test.upper() + test_type + ' Problem '  + str(problem) + '</h2>\n')
				else:
					f.write('\t<h2>' + str(year) + ' ' + test.upper() + ' ' + test_type + ' Problem '  + str(problem) + '</h2>\n')
				
				# scrapping the actual problem
				problem_html = ""
				start = soup.find("h2", text="Problem " + str(problem))
				avoid = solution_links[problem - 1].parent
				
				# in case the wiki is broken
				if(start == None):
					print("The Wiki Page: " + URL + ", is missing problem " + problem)
					print("Skipping this year. " + str(year) + ' ' + test.upper() + test_type + " is incomplete!")
					print("Fix the wiki with an Art of Problem Solving account, if possible.")
				if(avoid == None):
					print("The Wiki Page: " + URL + ", is missing a solution link for problem " + problem)
					print("Skipping this year. " + str(year) + ' ' + test.upper() + test_type + " is incomplete!")
					print("Fix the wiki with an Art of Problem Solving account, if possible.")
				
				content = start.next_sibling.next_sibling
				
				while(content != avoid):
					problem_html += str(content)
					content = content.next_sibling
				
				f.write('\t' + problem_html)
				f.write('\n\t<br/>\n')
				
				solution_url = URL + "/Problem_" + str(problem)
				f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
				
				f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
				f.write('</body>\n')
				f.write('</html>\n')
				f.close()
				
				with fileinput.FileInput(test + "/" + str(year) + "/" + test_type + "/" + file_name, inplace=True, backup='.bak') as file:
					for line in file:
						print(line.replace("//latex", "https://latex"), end='')

