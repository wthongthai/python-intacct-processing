# python code to add QA time to coding time

# final version that requires only one input file and prompts for path
def process():
    i = 0
    j = 0
    table = []
    table_WIP = []
    file_name1 = input("Enter path: ")
    file = open(file_name1, 'r')
    file_name2 = file_name1.replace(".csv", " QTT.csv")
    file2 = open(file_name2, 'w')

    # convert and process input into lists
    for f in file:
        mylist = f.split(",")
        j = len(mylist)  # for project, j == 4; for team, j == 5
        mylist[j - 3] = mylist[j - 3].replace(' - ', ',')
        mystringtemp = ",".join(mylist)
        mylist2 = mystringtemp.split(",")
        table.append(mylist2)
        i += 1

    # making sure the array is not being iterated over
    table_WIP = table
    # print(table)

    # change the number of hours from string to number
    for m in range(i):
        if len(table[m]) == 6:
               table_WIP[m][4] = float(table[m][4])
        else:
               table_WIP[m][3] = float(table[m][3])

    # updating original table
    table = table_WIP    

    # add hours coding to hours QA      
    for n in range(i):
        if table[n][j - 3] == 'Coding':  # for project, j == 4; for team, j == 5
            for l in range(n + 1, i):
                if table[n][0] == table[l][0] and table[n][j - 4] == table[l][j - 4] and table[l][j - 3] == 'QA' and table[n][j - 2] == table[l][j - 2]:
                    table_WIP[n][j - 1] = table_WIP[n][j - 1] + table_WIP[l][j - 1]


    # updating original table
    table = table_WIP    

    # print(table)
    
    # convert list into string and write to file
    for p in range(i):
        if j == 5:
            if len(table[p]) == 6:
                table[p][j - 3] = table[p][j - 3] + ' - ' + table[p][j - 2]
                del table[p][j - 2]
                table[p][j - 2] = str(table[p][j - 2])
            else:
                table[p][j - 2] = str(table[p][j - 2])
        else:
            table[p][j - 3] = table[p][j - 3] + ' - ' + table[p][j - 2]
            del table[p][j - 2]
            table[p][j - 2] = str(table[p][j - 2])
        mystring = ",".join(table[p])
        # print(mystring)
        file2.write(mystring)
        
    file.close()
    file2.close()

