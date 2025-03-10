# replace ___ with your code

def find_duplicates(input_list):
    # List to track elements we've seen so far
    seen_elements = []
    
    # List to store duplicate elements
    duplicates = []

    # Loop through each element in the input list
    
    for elements in input_list:

        # If the item is already in seen_elements and not already in duplicates,
        # then it's a duplicate, so we add it to duplicates
        if(seen_elements.__contains__(elements)and not duplicates.__contains__(elements)):
            duplicates.append(elements)

            # Otherwise, we add the item to seen_elements to keep track of it
        else:
            seen_elements.append(elements)

    # Return the list of duplicates
    return duplicates

my_list = [2, 'python', 5, 7, 'python', 'java', 5]

# Call the function to find duplicates in the list
duplicates = find_duplicates(my_list)

# Print the duplicate elements
print(duplicates)