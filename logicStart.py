##list of boolean values and last field is integer number
##           Math   Calc  Hist   Eng   PubSp  Art  Legal  Cyber  Acct  Credit
b_record  = [False, True, True, True, False, False, False, True, False, 60]
c_record  = [False, False, True, False, True, False, True, True, False, 75]
a_record  = [True, False, True, True, True, False, False, False, False, 54]

for x in a_record:
    print(x)
    
Math = a_record[0]
Calc = a_record[1]
Hist = a_record[2]
Eng = a_record[3]
PubSp = a_record[4]
Art = a_record[5]
Legal = a_record[6]
Cyber = a_record[7]
Acct = a_record[8]
Credit = a_record[9]

#checking credit levels.
if Credit >=60:
	reqcredit =True
	print("required minimum credits have been met.")
else:
	reqcredit=False
	print("required minimum credits have not been met.")


#checking gen ed course
if (Math or Calc) and Hist and (Eng or PubSp):
	reqGenED =True
	print("Required Gen Ed courses are complete.")
else:
	reqGenED=False
	print("required Gen Ed courses have not been met")


#checking if one major course has been completed;
if Art or Legal or Cyber or Acct :
	reqMajor =True
	print("Completed one major course")
else:
	reqMajor=False
	print("Did not complete one major course")


#are they ready to graduate;
if reqcredit and reqGenED and reqMajor:
	reqGrad=True
	print("Ready to graduate")
else:
	print("NOT ready to graduate")
	reqGrad=False


if reqGrad and Credit >= 75 and Legal and Cyber:
	print("Double Major!!")
else:
	print("Nope, No Double Major")


print("Script complete.")
#print("Math", Math)