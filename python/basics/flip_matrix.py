"""
# Reference code

for (int i = 0; i < reads[0].size(); i++) {
   vector<double> vertical_line;
   for (int j = 0; j < reads.size(); j++) {
       vector<double> horizontal_read = reads[j];
       vertical_line.push_back(horizontal_read[i]);
   }
   lines.push_back(vertical_line);
}
"""
def print_vector(vecofvec):
    for line in vecofvec:
        print(line)

original = [
    [1,1,1,1,1,1,1,0,0],
    [0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,1,0,0,0,0,0,0],
    [0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

lines = []
for i in range(len(original[0])):
    vertical_line = []
    for j in range(len(original)):
        horizontal_read = original[j]
        vertical_line.append(horizontal_read[i])
    lines.append(vertical_line)

print_vector(original)
print("-----------")
print_vector(lines)
