import sys,os

#create some variables to hold values
score = 0

#open file and loop line by line until EOF
with open(os.path.join(sys.path[0],'puzzle.txt')) as challenge:
    for line in challenge:
        line = line.split()
        #check if they throw rock, then calculate score based on our response
        if line[0] == 'A':
            if line[1] == 'X':
                score = score  + 1 + 3
            elif line[1] == 'Y':
                score = score + 2 + 6
            elif line[1] == 'Z':
                score = score + 3 + 0
        #check if they throw paper, then calculate score based on our response
        if line[0] == 'B':
            if line[1] == 'X':
                score = score  + 1 + 0
            elif line[1] == 'Y':
                score = score + 2 + 3
            elif line[1] == 'Z':
                score = score + 3 + 6
        #check if they throw scissors, then calculate score based on our response
        if line[0] == 'C':
            if line[1] == 'X':
                score = score  + 1 + 6
            elif line[1] == 'Y':
                score = score + 2 + 0
            elif line[1] == 'Z':
                score = score + 3 + 3

print('If you follow the guide you will score: '+str(score))

#part 2
#reset the score
score = 0
with open(os.path.join(sys.path[0],'puzzle.txt')) as challenge:
    for line in challenge:
        line = line.split()
        #check if we need to lose, then based on what is thrown by the opponent figure out what we need to do
        if line[1] == 'X':
            if line[0] == 'A':
                score = score  + 3 + 0
            elif line[0] == 'B':
                score = score + 1 + 0
            elif line[0] == 'C':
                score = score + 2 + 0
        #check if we need to tie, then based on what is thrown by the opponent figure out what we need to do
        if line[1] == 'Y':
            if line[0] == 'A':
                score = score  + 1 + 3
            elif line[0] == 'B':
                score = score + 2 + 3
            elif line[0] == 'C':
                score = score + 3 + 3
        #check if we need to win, then based on what is thrown by the opponent figure out what we need to do
        if line[1] == 'Z':
            if line[0] == 'A':
                score = score  + 2 + 6
            elif line[0] == 'B':
                score = score + 3 + 6
            elif line[0] == 'C':
                score = score + 1 + 6

print('If you follow the guide correct you will score: '+str(score))
