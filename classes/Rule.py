class Rule:

	ruleType = ""
	ruleEffects = ""

	text = ""

	def __init__(self, ruleType, ruleEffects):
		self.ruleType = ruleType
		self.ruleEffects = ruleEffects

		self.text = "\t" + str(self.ruleType) + ": " + str(self.ruleEffects) + ";\n"