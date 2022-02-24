import sys
import itertools
import multiprocessing as mp
import math

PRINTBOOKS = True

def main(infile):

	print(f"start {infile}")

	class Street:
		def __init__(self, index, begin, end, name, time):
			self.index = index
			self.begin = begin
			self.end = end
			self.name = name
			self.time = time
			self.startCars = []
			self.carsAtEnd = []

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index)


	class Car:
		def __init__(self, index, path, timeRemaining):
			self.index = index
			self.path = path
			self.timeRemaining = timeRemaining

		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index) + ':' + str(self.timeRemaining) + ':' + str(self.path).replace('[', '{').replace(']', '}')

	
	class Inter:
		def __init__(self, index):
			self.index = index
			self.ins = []
			self.outs = []
			self.schedule = []
			
		def __repr__(self):
			return self.__str__()
		def __str__(self):
			return str(self.index) + str(self.schedule).replace('[', '{').replace(']', '}')
			




	with open("in/" + infile, 'r') as inf:

		infoLine = inf.readline().rstrip("\n")
		info = infoLine.split(" ")

		maxTime = int(info[0])
		numInters = int(info[1])
		numStreets = int(info[2])
		numCars = int(info[3])
		bonusScore = int(info[4])


		allInters = []
		for interI in range(numInters):
			inter = Inter(interI)
			allInters.append(inter)


		allStreets = []
		streetDict = {}
		for streetI in range(numStreets):
			streetInfo = inf.readline().rstrip("\n").split(" ")
			street = Street(streetI, int(streetInfo[0]), int(streetInfo[1]), streetInfo[2], int(streetInfo[3]))
			allStreets.append(street)
			streetDict[street.name] = street
			
			allInters[street.begin].outs.append(street)
			allInters[street.end].ins.append(street)


		allCars = []
		for carI in range(numCars):
			carInfo = inf.readline().rstrip("\n").split(" ")
			path = []
			
			for i in range(1, len(carInfo)):
				street = streetDict[carInfo[i]]
				path.append(street)
				
			timeRemaining = maxTime - len(path[0].startCars)

			for streetI in range(1, len(path)):
				street = path[streetI]
				timeRemaining -= street.time
				
			car = Car(carI, path, timeRemaining)
			path[0].startCars.append(car)
			allCars.append(car)





	for inter in allInters:
		inter.ins = sorted(inter.ins, key=lambda s: -len(s.startCars))
		for s in inter.ins:
			inter.schedule.append((s.index, 1))










	
	with open("out" + infile, "w") as txt_file:
		outInt = tuple(filter(lambda i: len(i.schedule) > 0, allInters))
		txt_file.write(str(len(outInt)))
		for inter in outInt:
			txt_file.write(f"\n{inter.index}")
			txt_file.write(f"\n{len(inter.schedule)}")
			for step in inter.schedule:
				txt_file.write(f"\n{allStreets[step[0]].name} {step[1]}")


	print(f"done {infile}")




if __name__ == "__main__":
	main("a.txt")
	main("b.txt")
	main("c.txt")
	main("d.txt")
	main("e.txt")
	main("f.txt")