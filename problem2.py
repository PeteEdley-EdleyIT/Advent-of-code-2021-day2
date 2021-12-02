depth=0
position =0
aim =0 

with open('p1-finaldata.txt') as file:
    for line in file:
        command = line.split()
        if (command[0] == 'forward') :
            position += int(command[1])
            depth += aim*int(command[1])
        
        elif (command[0] == 'down' ) :
            aim += int(command[1])
        
        elif (command[0] == 'up') :
            aim -= int(command[1])
        else :
            print('opps invlid command')
            break
            
answer = depth*position

print ('position ' +str(position))
print ('depth ' + str(depth))

print(answer)