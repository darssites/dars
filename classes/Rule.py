class Rule:

	ruleType = ""
	ruleEffects = ""

	def __init__(self, ruleType, ruleEffects):
		self.ruleType = ruleType
		self.ruleEffects = ruleEffects

	def text(self):
		return "\t" + str(self.ruleType) + ": " + str(self.ruleEffects) + ";\n"