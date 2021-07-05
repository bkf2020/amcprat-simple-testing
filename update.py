from bs4 import BeautifulSoup
import random
import os
from datetime import datetime, timezone
from shutil import copyfile

def generate_problem_url_name(test, level):
	if(test == "aime"):
		year = random.randint(2015, 2021)
		year = str(year)

		test_type = "I"
		if(random.randint(0, 1) == 1):
			test_type = "II"
		problem = 0
		if(level == "easy"):
			problem = random.randint(1, 5)
		elif(level == "medium"):
			problem = random.randint(6, 10)
		elif(level == "hard"):
			problem = random.randint(11, 13)
		elif(level == "veryhard"):
			problem = random.randint(14, 15)
		problem = str(problem)
		if(len(problem) == 1):
			problem = "0" + problem

		problem_url = "../../../../../" + test + "/" + year + "/" + test_type + "/" + problem
		problem_name = year + " " + test.upper() + " " + test_type + " Problem " + problem
		return [problem_url, problem_name]

	elif(test == "amc10" or test == "amc12"):
		year = random.randint(2015, 2021)
		year = str(year)

		test_type = "A"
		if(random.randint(0, 1) == 1):
			test_type = "B"
		problem = 0
		if(level == "easy"):
			problem = random.randint(1, 15)
		elif(level == "medium"):
			problem = random.randint(16, 18)
		elif(level == "hard"):
			problem = random.randint(19, 22)
		elif(level == "veryhard"):
			problem = random.randint(23, 25)
		problem = str(problem)
		if(len(problem) == 1):
			problem = "0" + problem

		problem_url = "../../../../../" + test + "/" + year + "/" + test_type + "/" + problem
		problem_name = year + " " + test.upper() + test_type + " Problem " + problem
		return [problem_url, problem_name]

	elif(test == "amc8"):
		year = random.randint(2014, 2020)
		year = str(year)

		problem = 0
		if(level == "easy"):
			problem = random.randint(1, 15)
		elif(level == "medium"):
			problem = random.randint(16, 18)
		elif(level == "hard"):
			problem = random.randint(19, 22)
		elif(level == "veryhard"):
			problem = random.randint(23, 25)
		problem = str(problem)
		if(len(problem) == 1):
			problem = "0" + problem

		problem_url = "../../../../../" + test + "/" + year + "/" + problem
		problem_name = year + " " + test.upper() + " Problem " + problem
		return [problem_url, problem_name]

####################################################################################################

# setting utc time

now_utc = datetime.now(timezone.utc)
year = str(now_utc.year)
month = str(now_utc.month)
if(len(month) == 1):
	month = "0" + month

day = str(now_utc.day)
if(len(day) == 1):
	day = "0" + day

####################################################################################################

tests = ["aime", "amc8", "amc10", "amc12"]
levels = ["easy", "medium", "hard", "veryhard"]

index_soup = BeautifulSoup(open("index.html"), features="html5lib")
problemset_links = index_soup.find_all('li')

counter = 0
for test in tests:
	for level in levels:
		try:
			os.mkdir("problemsets/" + test + "/" + month)
		except:
			pass

		try:
			os.mkdir("problemsets/" + test + "/" + month + "/" + day)
		except:
			pass

		path = "problemsets/" + test + "/" + year + "/" + month + "/" + day + "/" + level + ".html"
		copyfile("problemsets/" + test + "/" + level + ".html", path)
		problemset_links[counter].find('a')['href'] = path[:-5]
		soup = BeautifulSoup(open(path), features="html5lib")

		visited = {}

		for q in range(1, 6):
			link_to_change = soup.find(id="problem"+str(q))
			problem_url_name = generate_problem_url_name(test, level)

			while(problem_url_name[0] in visited and visited[problem_url_name[0]]):
				problem_url_name = generate_problem_url_name(test, level)

			visited[problem_url_name[0]] = True

			link_to_change["href"] = problem_url_name[0]
			link_to_change.string = problem_url_name[1]

		page = open(path, "w")
		page.write(str(soup))

		counter += 1

page = open("index.html", "w")
page.write(str(index_soup))
