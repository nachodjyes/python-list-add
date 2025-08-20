# File Read & Write Challenge + Error Handling Lab

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Open the given file
    with open(filename, "r") as infile:
        content = infile.read()

    # Modify the content (example: uppercase)
    modified_content = content.upper()

    # Create a new filename for output
    new_filename = "modified_" + filename

    # Write the modified content into the new file
    with open(new_filename, "w") as outfile:
        outfile.write(modified_content)

    print(f"✅ File has been modified and saved as '{new_filename}'.")

# Error handling
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except PermissionError:
    print("❌ Error: You don't have permission to read this file.")
except Exception as e:
    print("❌ An unexpected error occurred:", e)