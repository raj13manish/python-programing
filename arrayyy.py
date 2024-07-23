import array as arr

# Define the integer array
int_array = arr.array('i', [1, 2, 3])

# Define the double (float) array
double_array = arr.array('d', [1.1, 2.2, 3.3])

# Print the original integer array
print("Original integer array: ", end="")
for i in range(len(int_array)):
    print(int_array[i], end=" ")
print()  # Newline for better readability

# Print the original double (float) array
print("Original double array: ", end="")
for i in range(len(double_array)):
    print(double_array[i], end=" ")
print()  # Newline for better readability
