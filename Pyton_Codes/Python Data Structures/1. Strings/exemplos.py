#example files: mbox-short.txt ou mbox.txt
#open a txt file and startswith

#example_1:
fname=open('mbox-short.txt')
for line in fname:
    #line = line.rstrip()
  if line.startswith('X-DSPAM-Confidence: 0.8475'):
        print(line)


#example_2:
file=input('Enter the file name:').strip()
fname=open(file)
sum=count=0
for line in fname:
    #line = line.rstrip()
  if line.startswith('X-DSPAM-Confidence:'):
        start=line.find('0') # start position
        end=line.find('0')+6 # end position
        n=float(line[start:end])
        sum=sum+n
        count=count+1
print(f'Average spam confidence: {sum/count:2f}')