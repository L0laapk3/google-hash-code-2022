import sys
import itertools
import multiprocessing as mp
import math





def main(infile):

	print(f"start {infile}")


	class Contrib:
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

	class Proj:
		def __init__(self, name, duration, score, deadline, skillsReq):
			self.name = name
			self.duration = duration
			self.score = score
			self.deadline = deadline
			self.skillsReq = skillsReq
			self.startDay = -1
			self.contribs = []

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.name) + ':' + str(self.duration) + ':' + str(self.score) + ':' + str(self.deadline) + ':' + str(self.skillsReq) 




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

			contrib = Contrib(contribInfo[0], skills)
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
			
			proj = Proj(name, amountOfDays, score, deadline, tuple(roles))
			allProj.append(proj)

	print(allContrib)
	print(allProj)



	allProj[1].startDay = 0
	allProj[1].contribs.append(allContrib[2])
	allProj[1].contribs.append(allContrib[1])




	
	with open("out" + infile, "w") as txt_file:
		plannedProj = []
		for proj in allProj:
			if proj.startDay != -1:
				plannedProj.append(proj)
				
		outProj = list(filter(lambda p: p.startDay != -1, allProj))
		sorted(outProj, key=lambda p: p.startDay)
		txt_file.write(f"{str(len(outProj))}\n")
		for proj in outProj:
			txt_file.write(f"{proj.name}\n")
			contribNames = []
			for contrib in proj.contribs:
				contribNames.append(contrib.name)
			txt_file.write(f"{' '.join(contribNames)}\n")

	print(f"done {infile}")




if __name__ == "__main__":
	main("a.txt")
	# main("b.txt")
	# main("c.txt")
	# main("d.txt")
	# main("e.txt")
	# main("f.txt")