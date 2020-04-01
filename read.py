file = open("e.txt", "r")
edge_list = []
# Repeat for each song in the text file
for line in file:
    # Let's split the line into an array called "fields" using the ";" as a separator:
    if line.startswith("#"):
        continue
    else:
        fields = line.split(",")

        # and let's extract the data:
        vertex = int(fields[0])
        vertex1 = int(fields[1])
        distance = int(fields[2])
        edge_list.append([vertex,vertex1,distance])
        # Print the song


# It is good practice to close the file at the end to free up resources
file.close()
print(edge_list)

a = 58
b = 61

for sublist in edge_list:
    if a in sublist and b in sublist:
        print(sublist[2])
        break


