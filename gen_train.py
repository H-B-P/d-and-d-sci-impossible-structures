import pandas as pd
import random

random.seed(0)

backgroundList = ["Self-Taught"]*37 + ["Apprenticed under T. Geisel"]*15 +["Apprenticed under P. Stamatin"]*16 + ["Apprenticed under R. Penrose"]*11 + ["Apprenticed under B. Johnson"]*15 +["Apprenticed under M. Escher"]*9
structureList = ["Tower"]*34 + ["Mansion"]*22 + ["Mechanism"]*27 + ["Library"]*13
materialDict = {"Dreams":[0,0],"Wood":[500,1000], "Steel":[2000,10000], "Glass":[20000,40000], "Silver":[50000,100000], "Nightmares":[200000,1000000]}
blueprintList = ["Hastily Sketched"]*21 +  ["Deceptively Ordinary"]*13 + ["Obsessively Detailed"]*19

backgrounds = []
structures = []
materials = []
blueprints = []
impossibilities = []
costs = []

for i in range(954):
 background = random.choice(backgroundList)
 structure = random.choice(structureList)
 materialTwo = random.choice([x for x in materialDict])
 materialOne = random.choice([x for x in materialDict if x not in ["Dreams","Nightmares",materialTwo]])
 blueprint = random.choice(blueprintList)
 
 impossibility="No"
 if background in ["Apprenticed under P. Stamatin", "Apprenticed under B. Johnson"]:
  impossibility="Yes"
 if background=="Self-Taught":
  impossibility=random.choice(["Yes"]*43 + ["No"]*57)
 
 cost = round(random.uniform(materialDict[materialOne][0],materialDict[materialOne][1]) + random.uniform(materialDict[materialTwo][0],materialDict[materialTwo][1]))
 
 backgrounds.append(background)
 structures.append(structure)
 materials.append(materialOne+" and "+materialTwo)
 blueprints.append(blueprint)
 impossibilities.append(impossibility)
 costs.append(cost)

dataDict = {"Background of Architect":backgrounds, "Proposed Structure Type":structures, "Required Construction Materials":materials, "Characterization of Blueprints":blueprints, "Is Structure Impossible?":impossibilities, "Cost of Structure":costs}
df = pd.DataFrame(dataDict)

df.to_csv("data.csv", index=False)