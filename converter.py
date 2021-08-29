def converter():

    # read files and store contents in data string
    for X in range(7):
        file = open(f'{X}.txt')
        data = file.read()
        data = data.replace("(", "")
        data = data.replace("\t", "\n")
        data = data.replace(")", "")
        # print(data)

        with open(f'{X}.csv', 'w') as f:
            # f.write('strength,angle,distance\n')
            f.write(data)


converter()
