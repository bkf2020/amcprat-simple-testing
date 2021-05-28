from bs4 import BeautifulSoup
import random

def generate_problem_url(test, level):
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
		
		return year + "/" + test_type + "/" + problem + ".html"
	
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
		
		return year + "/" + test_type + "/" + problem + ".html"
	
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
		
		return year + "/" + problem + ".html"
		

tests = ["aime", "amc8", "amc10", "amc12"]
levels = ["easy", "medium", "hard", "veryhard"]

for test in tests:
	for level in levels:
		path = "problemsets/" + test + "/" + level + ".html"
		soup = BeautifulSoup(open(path), features="html5lib")
		
		visited = {}
		
		for q in range(1, 6):
			link_to_change = soup.find(id="problem"+str(q))
			problem_url = generate_problem_url(test, level)
			while(problem_url in visited and visited[problem_url]):
				problem_url = generate_problem_url(test, level)
			visited[problem_url] = True
				
			link_to_change["href"] = problem_url
		
		page = open(path, "w")
		page.write(str(soup))
