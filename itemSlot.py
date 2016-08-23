class itemSlot:

	def __init__(required, itemType, recommended, buildLink, statPriority):
		self.itemType = itemType
		self.required = required
		if(recommended[0] != None):
			self.recommended = recommended
		self.buildLink = buildLink
		self.statPriority = statPriority
		
	def getRequired():
		print required
	
	def getitemType():
		print itemType
		
	def getRecommended():
		if(recommended[0] != None):
			for i in range len(recommended):
				print recommended(i) + "/n"