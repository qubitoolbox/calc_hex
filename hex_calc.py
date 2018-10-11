#Author Osman D morales.
#A program I wrote prior to any
#binary/hex learning at my current University.
#

class conVersion():

	#print the different options to the user

	optionz = "1. Type 'hex' for hex values."
	optionz1 = "2. Type 'bin' for binary values."
	optionz2 = "3. Type 'dec' for decimal values."
	optionz3 = "4. Type '+', or '-', or '/', or '*' \n"

	print(optionz)
	print(optionz1)
	print(optionz2)
	print(optionz3)

	#Ask the user for input
	#what kind of value to convert
	user_input = input("Enter hex, bin, or dec: \n")

	#check for kind of input that user enters
	if(user_input == "dec"):
		value_ = input("Number? \n")
		_value = input("Number? \n")
	elif(user_input == "hex"):
		value_ = input("Hexadecimal? \n")
		_value = input("Hexadecimal? \n")
		value__ = value_
		__value = _value
	elif(user_input == "bin"):
		value_ = input("Binary? \n")
		_value = input("Binary? \n")
		value__ = value_
		__value = _value
	
	#Functions to convert values from dec to bin, dec to hex
	def decTobin(self):
		binconver = self.value__
		_binconver = self.__value
		binconver1 = int(binconver, 2)
		_binconver1 = int(_binconver, 2)

		suma = binconver1 + _binconver1
		sumax = bin(suma)
		nega = binconver1 - _binconver1
		negax = bin(nega)
		divi = binconver1 // _binconver1
		divix = bin(divi)
		mult = binconver1 * _binconver1
		multx = bin(mult)
		
		bin_prompt = input("What type of calculation? \n")
		
		if bin_prompt == "+":
			print(sumax[2:])
		elif bin_prompt == "-":
			print(negax[2:])
		elif bin_prompt == "/":
			print(divix[2:])
		elif bin_prompt == "*":
			print(multx[2:])
		
	#function to calculate decimal to hexadecimal	
	def decTohex(self):
		hexconver = self.value__
		_hexconver = self.__value
		hexconver1 = int(hexconver, 16)
		_hexconver = int(_hexconver, 16)
		
		sumat = hexconver1 + _hexconver
		sumat_ = hex(sumat)
		negat = hexconver1 - _hexconver
		negat_ = hex(negat)
		divit = hexconver1 // _hexconver
		divit_ = hex(divit)
		mutlt = hexconver1 * _hexconver
		mutlt_ = hex(mutlt)
		
		hex_prompt = input("What kind of calculation? \n")
		
		if hex_prompt == "+":
			print(sumat_[2:])
		elif hex_prompt == "-":
			print(negat_[2:])
		elif hex_prompt == "/":
			print(divit_[2:])
		elif hex_prompt == "*":
			print(mutlt_[2:])
			
	#function to calculate decimal to decimal	
	def decTodec(self):
		
		deconver = self.value_
		deconver_ = self._value
		deconver = int(deconver)
		deconver_ = int(deconver_)
		
		
		sumdec = deconver + deconver_
		negdec = deconver - deconver_
		divdec = deconver / deconver_
		multdec = deconver * deconver_
		
		dec_prompt = input("What kind of calculation? \n")
		
		if dec_prompt == "+":
			print(sumdec)
		elif dec_prompt == "-":
			print(negdec)
		elif dec_prompt == "/":
			print(divdec)
		elif dec_prompt == "*":
			print(multdec)
	

#create object for testing
con = conVersion()
test = bb.decTobin()
print(test)
