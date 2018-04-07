#VITERBI'S ALGORITHM

#taking input sequence
seq=raw_input()

#converting to upper case
seq=seq.upper()

#convert sequence string to list
seq1=list(seq)

#starting probabilities
s1=-1
s2=-1

#Emission Probabilities(log odd scores) of high and low states
h={'A': -2.322 , 'C': -1.737 , 'G': -1.737 , 'T': -2.322}
l={'A': -1.737 , 'C': -2.322 , 'G': -2.322 , 'T': -1.737}

#Transition Probabilities(log odd scores)
h_h=-1		#high to high
l_l=-0.737	#low to low
h_l=-1		#high to low
l_h=-1.322	#low to high

#lists to store the probability of element coming from high or low state
h1=[]
l1=[]

#for first nucleotide
h1.append(s1 + h[seq1[0]])
l1.append(s2 + l[seq1[0]])

#appending probabilities for rest of the sequence
for i in range(1,len(seq)):
	h1.append(h[seq1[i]] + max((h1[i-1] + h_h) , (l1[i-1] + l_h)))
	l1.append(l[seq1[i]] + max((h1[i-1] + h_l) , (l1[i-1] + l_l)))

print 
print("probabilities of nucleotide being selected from high state\n")
print h1
print
print("probabilities of nucleotide being selected from low state\n")
print l1
print

#output sequence corresponding to H and L
output=[]

#back-tracing for maximum probabilities
for i in range(len(seq)-1, -1, -1):
	if(h1[i]>l1[i]):
		output.append('H')
	else:
		output.append('L')

#reversing the final output
output=output[ : :-1]

print("Final output:\n")
print output
