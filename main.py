import sys
import itertools
import multiprocessing as mp
import math





def main(infile):

	print(f"start {infile}")

	class ProjectInfo:
		def __init__(self, contributers, projects):
			self.contributers = contributers
			self.projects = projects

		def __repr(self):
			return self.__str__()
		def __str__(self):
			return str(self.contributers) + ':' + str(self.projects) 

	class Contributor:
		def __init__(self, name, skills):
			self.name = name
			self.skills = skills

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return self.name + ':' + str(self.skills)

	class Skill:
		def __init__(self, name, level):
			self.name = name
			self.level = level

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.name) + ':' + str(self.level)

	class Project:
		def __init__(self, name, amountOfDays, score, deadline, rolesRequired):
			self.name = name
			self.amountOfDays = amountOfDays
			self.score = score
			self.deadline = deadline
			self.rolesRequired = rolesRequired

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.name) + ':' + str(self.amountOfDays) + ':' + str(self.score) + ':' + str(self.deadline) + ':' + str(self.rolesRequired) 




	with open("in/" + infile, 'r') as inf:

		infoLine = inf.readline().rstrip("\n")
		info = infoLine.split(" ")

		numContrib = int(info[0])
		numProj = int(info[1])

		allContrib = []
		for contribI in range(numContrib):
			contribLine = inf.readline().rstrip("\n")
			contribInfo = contribLine.split(" ")
			name = contribInfo[0]
			numSkills = int(contribInfo[1])
			skills = []
			for skillI in range(numSkills):
				skillLine = inf.readline().rstrip("\n")
				skillInfo = skillLine.split(" ")
				skills.append(Skill(skillInfo[0], int(skillInfo[1])))

			contrib = Contributor(contribInfo[0], skills)
			allContrib.append(contrib)

		allProj = []
		for projI in range(numProj):
			projLine = inf.readline().rstrip("\n")
			projInfo = projLine.split(" ")
			name = projInfo[0]
			amountOfDays = int(projInfo[1])
			score = int(projInfo[2])
			deadline = int(projInfo[3])
			numRoles = int(projInfo[4])
			roles = []
			for roleI in range(numRoles):
				skillLine = inf.readline().rstrip("\n")
				skillInfo = skillLine.split(" ")
				roles.append(Skill(skillInfo[0], int(skillInfo[1])))
			
			proj = Project(name, amountOfDays, score, deadline, tuple(roles))
			allProj.append(proj)

	print(allContrib)
	print(allProj)



		
	# 	CYCLETIME = 3
	# 	for s in inter.ins:
	# 		onTime = min(math.ceil(len(s.cars) * CYCLETIME / inter.totalCars), maxTime)
	# 		if onTime > 0:
	# 			inter.schedule.append((s.index, onTime))



	





	
	# with open("out" + infile, "w") as txt_file:
	# 	outInt = tuple(filter(lambda i: len(i.schedule) > 0, allInters))
	# 	txt_file.write(str(len(outInt)))
	# 	for inter in outInt:
	# 		txt_file.write(f"\n{inter.index}")
	# 		txt_file.write(f"\n{len(inter.schedule)}")
	# 		for step in inter.schedule:
	# 			txt_file.write(f"\n{allStreets[step[0]].name} {step[1]}")


	# print(f"done {infile}")




if __name__ == "__main__":
	main("a.txt")
	# main("b.txt")
	# main("c.txt")
	# main("d.txt")
	# main("e.txt")
	# main("f.txt")