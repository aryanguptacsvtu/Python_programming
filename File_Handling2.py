f = open('myfile2.txt','r')
while True:
    line=f.readline()     # 'readline()' reads all lines of file & returns them as strings.
    if not line:
        break
    print(line)


g = open('myfile3.txt','r')
i=0
while True:
    i=i+1
    lines = g.readline()
    if not lines:
        break

    m1 = int(lines.split(",")[0])
    m2 = int(lines.split(",")[1])
    m3 = int(lines.split(",")[2])
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in Science is: {m3}")

    print(lines)


h = open('myflie.txt4','w')      # 'writeline()' writes a sequence of strings to a file.
points=['line1\n','line2\n']
h.writelines(points)

bullets=['first','second','third']
for bullet in bullets:                 # It doesn't add newline char. between the strings. Add them separately.
    h.write(bullet +'\n')                   
h.close()
