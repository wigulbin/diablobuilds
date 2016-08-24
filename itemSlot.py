class itemSlot(object):

	def __init__(self, required, itemType, recommended, buildLink, statPriority):
		self.itemType = itemType
		self.required = required
		if(recommended[0] != None):
			self.recommended = recommended
		self.buildLink = buildLink
		self.statPriority = statPriority
		
	def getRequired(self):
		print self.required
	
	def getitemType(self):
		print self.itemType
		
	def getRecommended(self):
		if(recommended[0] != None):
			for i in recommended:
				print self.i + "/n"
	
