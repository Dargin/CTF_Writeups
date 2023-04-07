import sys,os

#create some variables to hold values
elfs = []
callories = 0

#open file and loop line by line until EOF
with open(os.path.join(sys.path[0],'puzzle.txt')) as challenge:
    for line in challenge:
        #check if the line is not just a new line; if not it's an integer
        if line != '\n':
            #as we're reading from a file it gets treated as a string, force it to be an int and add it
            callories += int(line)
        #if it is a new line then we are done with that elf and can add the total callories to the list, need to make sure we reset callories
        else:
            elfs.append(callories)
            callories = 0

#sort the list
elfs.sort()
#print the last item in the list; this is answer to question 1
print('The elf with the most callories is carrying ' + str(elfs[-1]))

#to get to the top three we reverse sort and then get the top three values
top3 = sorted(elfs, reverse=True)[0:3]
print('The top three elves are carrying '+ str(top3))
print('The total of those three is '+str(sum(top3)))
