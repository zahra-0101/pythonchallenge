
class Level_1():
	string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

	def __init__(self, string=string):
			self.string = string

	def decoder(self):
		decoded_str = ""
		for ltr in self.string:
			ltr_ASCII = ord(ltr)
			if ltr_ASCII == ord('z'):
				ltr_ASCII = ord('b')
			elif  ltr_ASCII == ord('Z'):
				ltr_ASCII = ord('B')
			elif ltr_ASCII == ord('y'):
				ltr_ASCII = ord('a')
			elif ltr_ASCII == ord('Y'):
				ltr_ASCII = ord('A')
			elif ord('A') <= ltr_ASCII <= ord('Z') or ord('a') <= ltr_ASCII <= ord('z'):
				# print (chr(ltr_ASCII), '\n')
			# else:	
				ltr_ASCII = ltr_ASCII + 2
			
			decoded_str += chr(ltr_ASCII)

		print(decoded_str)


L1 = Level_1()
L1.decoder()

L1_url = Level_1('map')
L1_url.decoder()