import sys
import itertools
import multiprocessing as mp
import math
import random





def main(infile):

	print(f"start {infile}")


	class Contrib:
		def __init__(self, name, skills):
			self.name = name
			self.skills = skills
			self.busy = [] # (startday, endDay)

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return self.name + ':' + str(self.skills) + ':' + str(self.busy)

	class Skill:
		def __init__(self, name, level):
			self.name = name
			self.level = level

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.name) + ':' + str(self.level)

	class Proj:
		def __init__(self, name, duration, maxScore, bestBefore, skillsReq):
			self.name = name
			self.duration = duration
			self.maxScore = maxScore
			self.bestBefore = bestBefore
			self.skillsReq = skillsReq
			self.reset()

		def reset(self):
			self.startDay = -1
			self.contribs = [None] * len(self.skillsReq)

			
		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.name) + ':' + str(self.duration) + ':' + str(self.maxScore) + ':' + str(self.bestBefore) + ':' + str(self.skillsReq) 


	maxScore = 0

	while True:
		with open("in/" + infile, 'r') as inf:

			infoLine = inf.readline().rstrip("\n")
			info = infoLine.split(" ")

			numContrib = int(info[0])
			numProj = int(info[1])

			allContrib = []
			allContribBySkill = {}
			for contribI in range(numContrib):
				contribLine = inf.readline().rstrip("\n")
				contribInfo = contribLine.split(" ")
				name = contribInfo[0]
				numSkills = int(contribInfo[1])
				skills = []
				contrib = Contrib(contribInfo[0], skills)
				for skillI in range(numSkills):
					skillLine = inf.readline().rstrip("\n")
					skillInfo = skillLine.split(" ")
					skills.append(Skill(skillInfo[0], int(skillInfo[1])))
					if skillInfo[0] not in allContribBySkill:
						allContribBySkill[skillInfo[0]] = [contrib]
					else:
						allContribBySkill[skillInfo[0]].append(contrib)

				allContrib.append(contrib)

			lastDay = 0
			allProj = []
			for projI in range(numProj):
				projLine = inf.readline().rstrip("\n")
				projInfo = projLine.split(" ")
				name = projInfo[0]
				duration = int(projInfo[1])
				score = int(projInfo[2])
				bestBefore = int(projInfo[3])
				numRoles = int(projInfo[4])
				roles = []
				for roleI in range(numRoles):
					skillLine = inf.readline().rstrip("\n")
					skillInfo = skillLine.split(" ")
					roles.append(Skill(skillInfo[0], int(skillInfo[1])))

				lastDay = max(lastDay, bestBefore + duration)			
				proj = Proj(name, duration, score, bestBefore, tuple(roles))
				allProj.append(proj)

		# print(allContrib)
		# print(allProj)


		## random
		allProj = sorted(allProj, key=lambda x: x.maxScore, reverse=True)
		def fillDay(day):
			random.shuffle(allProj)
			for proj in allProj:
				if proj.startDay != -1: # project booked
					break
				random.shuffle(allContrib)
				unfilledSkills = list(proj.skillsReq)
				unfilledCount = len(unfilledSkills)
				# print(unfilledCount)
				for contrib in allContrib:
					# todo: check if person is busy
					isBusy = False
					for busy in contrib.busy:
						if busy[0] <= day and day < busy[1]:
							isBusy = True
							break
					if isBusy:
						break
					usedContrib = False
					for skillReqI in range(len(unfilledSkills)):
						skillReq = unfilledSkills[skillReqI]
						if skillReq is not None:
							for skill in contrib.skills:
								if skillReq.name == skill.name and skillReq.level <= skill.level:
									# print(skillReq)
									proj.contribs[skillReqI] = contrib
									unfilledSkills[skillReqI] = None
									usedContrib = True
									unfilledCount -= 1
									if unfilledCount == 0:
										proj.startDay = day
									break
						if usedContrib:
							break
					if proj.startDay != -1: # project booked now
						for contribI in range(len(proj.contribs)):
							contrib = proj.contribs[contribI]
							contrib.busy.append((day, day + proj.duration))
							for skill in contrib.skills:
								if skill.name == proj.skillsReq[contribI].name and skill.level <= proj.skillsReq[contribI].level:
									skill.level += 1
						break
					



		for day in range(0, lastDay, 100):
			fillDay(day)
			if day % 100 == 0 and day > 0:
						
				with open("outkak5" + infile, "w") as txt_file:
					plannedProj = []
					for proj in allProj:
						if proj.startDay != -1:
							plannedProj.append(proj)
							
					outProj = list(filter(lambda p: p.startDay != -1, allProj))
					outProj = sorted(outProj, key=lambda p: p.startDay)
					txt_file.write(f"{str(len(outProj))}\n")
					for proj in outProj:
						txt_file.write(f"{proj.name}\n")
						contribNames = []
						for contrib in proj.contribs:
							contribNames.append(contrib.name)
						txt_file.write(f"{' '.join(contribNames)}\n")

				print(f"done {infile} {day}")





		def getTotalScore():
			score = 0
			for proj in allProj:
				if proj.startDay != -1:
					score += max(proj.maxScore - max(proj.startDay + proj.duration - proj.bestBefore, 0), 0)
			return score

		score = getTotalScore()
		if score <= maxScore:
			continue
		print(score)
		maxScore = score
		

		# allProj[1].startDay = 0
		# allProj[1].contribs[1] = allContrib[0]
		# allProj[1].contribs[0] = allContrib[1]

		# allProj[0].startDay = 7
		# allProj[0].contribs[0] = allContrib[0]

		# allProj[2].startDay = 7
		# allProj[2].contribs[0] = allContrib[2]
		# allProj[2].contribs[1] = allContrib[1]


		# print(allContrib)

		
		with open("outkak2" + infile, "w") as txt_file:
			plannedProj = []
			for proj in allProj:
				if proj.startDay != -1:
					plannedProj.append(proj)
					
			outProj = list(filter(lambda p: p.startDay != -1, allProj))
			outProj = sorted(outProj, key=lambda p: p.startDay)
			txt_file.write(f"{str(len(outProj))}\n")
			for proj in outProj:
				txt_file.write(f"{proj.name}\n")
				contribNames = []
				for contrib in proj.contribs:
					contribNames.append(contrib.name)
				txt_file.write(f"{' '.join(contribNames)}\n")

		print(f"done {infile}")




if __name__ == "__main__":
	# main("a.txt")
	# main("b.txt")
	# main("c.txt")
	# main("d.txt")
	# main("e.txt")
	main("f.txt")