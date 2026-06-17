#File word search : find all lines containing a keyword

with open("study_notes.txt", "w") as file:
    file.write("Python is easy to learn.\n")
    file.write("File handling.\n")
    file.write("Python is widely used.\n")
    file.write(" We learn data Science with Python.\n")
def search_file(filename, keyword):
    print(f"\nSearching for '{keyword}'")
    match_found = False
    
    try:
        with open(filename, "r") as file:
            # enumerate(file, 1) automatically gives us a line counter starting at 1
            for line_number, line in enumerate(file, 1):
                
                # We use .lower() on both so the search is case-insensitive
                if keyword.lower() in line.lower():
                    # .strip() removes the invisible newline character for clean printing
                    print(f"Line {line_number}: {line.strip()}")
                    match_found = True
                    
        if not match_found:
            print("Keyword not found in the document.")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' is missing.")
search_file("study_notes.txt", "Python")
search_file("study_notes.txt", "learn") # Notice this is lowercase, but it will still find it!
search_file("study_notes.txt", "Vygotsky")


