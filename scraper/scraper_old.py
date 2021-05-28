from bs4 import BeautifulSoup
from shutil import copyfile
import os
import fileinput

soup = BeautifulSoup(open("index.html", encoding='utf-8'), 'html.parser')

def is_int(s):
	try:
		int(s)
		return True
	except ValueError:
		return False

def is_valid_test_name(s):
	if s == "AMC8" or s == "AMC10" or s == "AMC12" or s == "AIME":
		return True
	return False

print("Welcome to the AoPS Scrapper! First, make sure you have created the index.html file.")
print("If you are unsure of what this is, please look at the README.md file.")
try:
	input("Press enter if you are ready.")
except SyntaxError:
	pass

year_str = input("Enter the year: ")
while (not is_int(year_str)):
	print("Invalid year!")
	year_str = input("Enter the year: ")

test_name = input("Enter one of the following: AMC8, AMC10, AMC12, or AIME: ")
while(not is_valid_test_name(test_name)):
	print("Invalid test name!")
	test_name = input("Enter one of the following: AMC8, AMC10, AMC12, or AIME: ")

try:
	os.mkdir("./" + year_str)
except:
	print("the directory with the name " + year_str + " already exists. that's fine.")

all_text = [tag for tag in soup.find_all(class_ = "cmty-view-post-item-text")]

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
			img["style"] += " height: calc(" + img["height"] + " * calc(1em/18));"
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
			img["style"] += "height: calc(" + img["height"] + " * calc(1em/18));"
			del img["height"]
		except KeyError:
			continue

if(test_name == "AMC8"):
	copyfile("problemsetamc8.html", year_str + "/problemset.html")
	skip = input("How many rows before the problems should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before the problems should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 26):
		file_name = ""
		solution_url = "https://artofproblemsolving.com/wiki/index.php/"
		solution_url += year_str + "_AMC_8_Problems/Problem_" + str(i)
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/" + file_name, "w")
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write('<head>\n')
		f.write('\t<meta charset="utf-8">')
		f.write('\t<meta name="HandheldFriendly" content="true" />\n')
		f.write('\t<meta name="MobileOptimized" content="320" />\n')
		f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		f.write('\t<link rel="stylesheet" href="../../../templates/styleproblems.css">\n')
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('\t<h1>AMCPRAT Problem</h1>\n')
		f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
		f.write('\t<hr/>\n')
		f.write('\t<h2>' + year_str + ' ' + test_name + ' Problem '  + str(i) + '</h2>\n')
		f.write(str(all_text[counter]))
		f.write('\n\t<br/>')
		f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
		f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//latex", "https://latex"), end='')

elif(test_name == "AMC10" or test_name == "AMC12"):
	try:
		os.mkdir("./" + year_str + "/A")
		os.mkdir("./" + year_str + "/B")
	except:
		print("directories already exist. that's okay")
	copyfile("problemsetamc1012.html", year_str + "/A/problemset.html")
	copyfile("problemsetamc1012.html", year_str + "/B/problemset.html")
	skip = input("How many rows before test A should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test A should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 26):
		file_name = ""
		solution_url = "https://artofproblemsolving.com/wiki/index.php/"
		solution_url += year_str + "_AMC_10A_Problems/Problem_" + str(i)
		if(test_name == "AMC12"):
			solution_url = "https://artofproblemsolving.com/wiki/index.php/"
			solution_url += year_str + "_AMC_12A_Problems/Problem_" + str(i)
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/A/" + file_name, "w")
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write('<head>\n')
		f.write('\t<meta charset="utf-8">')
		f.write('\t<meta name="HandheldFriendly" content="true" />\n')
		f.write('\t<meta name="MobileOptimized" content="320" />\n')
		f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		f.write('\t<link rel="stylesheet" href="../../../../templates/styleproblems.css">\n')
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('\t<h1>AMCPRAT Problem</h1>\n')
		f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
		f.write('\t<hr/>\n')
		f.write('\t<h2>' + year_str + ' ' + test_name + 'A Problem '  + str(i) + '</h2>\n')
		f.write(str(all_text[counter]))
		f.write('\n\t<br/>')
		f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
		f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/A/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//latex", "https://latex"), end='')

	skip = input("How many rows before test B should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test B should be skipped? ")
		
	counter += int(skip)

	for i in range(1, 26):
		file_name = ""
		solution_url = "https://artofproblemsolving.com/wiki/index.php/"
		solution_url += year_str + "_AMC_10B_Problems/Problem_" + str(i)
		if(test_name == "AMC12"):
			solution_url = "https://artofproblemsolving.com/wiki/index.php/"
			solution_url += year_str + "_AMC_12B_Problems/Problem_" + str(i)
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/B/" + file_name, "w")
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write('<head>\n')
		f.write('\t<meta charset="utf-8">')
		f.write('\t<meta name="HandheldFriendly" content="true" />\n')
		f.write('\t<meta name="MobileOptimized" content="320" />\n')
		f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		f.write('\t<link rel="stylesheet" href="../../../../templates/styleproblems.css">\n')
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('\t<h1>AMCPRAT Problem</h1>\n')
		f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
		f.write('\t<hr/>\n')
		f.write('\t<h2>' + year_str + ' ' + test_name + 'B Problem '  + str(i) + '</h2>\n')
		f.write(str(all_text[counter]))
		f.write('\n\t<br/>')
		f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
		f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/B/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//latex", "https://latex"), end='')

elif(test_name == "AIME"):
	try:
		os.mkdir("./" + year_str + "/I")
		os.mkdir("./" + year_str + "/II")
	except:
		print("directories already exist. that's okay")
	copyfile("problemsetaime.html", year_str + "/I/problemset.html")
	copyfile("problemsetaime.html", year_str + "/II/problemset.html")
	
	skip = input("How many rows before test I should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test I should be skipped? ")
		
	counter = int(skip)
	
	for i in range(1, 16):
		file_name = ""
		solution_url = "https://artofproblemsolving.com/wiki/index.php/"
		solution_url += year_str + "_AIME_I_Problems/Problem_" + str(i)
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/I/" + file_name, "w")
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write('<head>\n')
		f.write('\t<meta charset="utf-8">')
		f.write('\t<meta name="HandheldFriendly" content="true" />\n')
		f.write('\t<meta name="MobileOptimized" content="320" />\n')
		f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		f.write('\t<link rel="stylesheet" href="../../../../templates/styleproblems.css">\n')
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('\t<h1>AMCPRAT Problem</h1>\n')
		f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
		f.write('\t<hr/>\n')
		f.write('\t<h2>' + year_str + ' ' + test_name + ' I Problem '  + str(i) + '</h2>\n')
		f.write(str(all_text[counter]))
		f.write('\n\t<br/>')
		f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
		f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/I/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//latex", "https://latex"), end='')

	skip = input("How many rows before test II should be skipped? ")
	while (not is_int(skip)):
		print("Invalid number!")
		skip = input("How many rows before test II should be skipped? ")
		
	counter += int(skip)

	for i in range(1, 16):
		file_name = ""
		solution_url = "https://artofproblemsolving.com/wiki/index.php/"
		solution_url += year_str + "_AIME_II_Problems/Problem_" + str(i)
		if 1 <= i and i <= 9:
			file_name = "0" + str(i) + ".html"
		else:
			file_name = str(i) + ".html"
		f = open(year_str + "/II/" + file_name, "w")
		f.write("<!DOCTYPE html>\n")
		f.write("<html>\n")
		f.write('<head>\n')
		f.write('\t<meta charset="utf-8">')
		f.write('\t<meta name="HandheldFriendly" content="true" />\n')
		f.write('\t<meta name="MobileOptimized" content="320" />\n')
		f.write('\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
		
		if(test == "amc8"):
			f.write('\t<link rel="stylesheet" href="../../../templates/styleproblems.css">\n')
		else:
			f.write('\t<link rel="stylesheet" href="../../../../templates/styleproblems.css">\n')
		
		f.write('</head>\n')
		f.write('<body>\n')
		f.write('\t<h1>AMCPRAT Problem</h1>\n')
		f.write('\t<h3><em>Do not give up! Zoom in if diagrams are unclear!</em></h3>\n')
		f.write('\t<hr/>\n')
		f.write('\t<h2>' + year_str + ' ' + test_name + ' II Problem '  + str(i) + '</h2>\n')
		f.write(str(all_text[counter]))
		f.write('\n\t<br/>')
		f.write('\t<a href="' + solution_url + '" target="_blank" rel="noopener noreferrer">Solution</a>\n')
		f.write('\t<p>The AMC/AIME problems are copyright &#169; Mathematical Association of America.</p>\n')
		f.write('</body>\n')
		f.write('</html>\n')
		f.close()
		counter += 1
		with fileinput.FileInput(year_str + "/II/" + file_name, inplace=True, backup='.bak') as file:
			for line in file:
				print(line.replace("//latex", "https://latex"), end='')
