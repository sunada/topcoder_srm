class BinaryCode:
	string = ''

	def __init__(self, string):
		self.string = string
	
	def cal(self, start):
		#print
		res = [str(start)]
		cnt = len(self.string)
		if cnt == 1:
			next = int(self.string) - start
			#print next,
			if next < 0 or next > 1:
				return "NONE"
			else:
				res.append(str(next))
				return ''.join(res)

		for i in range(cnt):
			if i == 0:
				next = int(self.string[i]) - int(res[0])
			else:
				next = int(self.string[i]) - int(res[i]) - int(res[i - 1])
			#print next,
			if i == cnt - 1:
				if next != 0:
					return "NONE"
				else:
					return ''.join(res)
			elif next < 0 or next > 1:
				return "NONE"
			else:
			  	res.append(str(next))

	def decode(self):
		res = []
		res.append(self.cal(0))
		res.append(self.cal(1))
		return res


if __name__ == '__main__':
	b = BinaryCode('3')
	#print b.decode()

	b = BinaryCode('123210122')
	#print b.decode()

	b = BinaryCode('11')
	#print b.decode()

	b = BinaryCode('22111')
	#print b.decode()

	b = BinaryCode('123210120')
	#print b.decode()

	b = BinaryCode('12221112222221112221111111112221111')
	res = b.decode()
	if res[0] == '01101001101101001101001001001101001' and res[1] == '10110010110110010110010010010110010':
		print 'True'
	else:
		print 'False'
	