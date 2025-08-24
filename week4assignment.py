def file_read_write():
    filename = input("Enter the filename to read:  ")

    try:

        with open(filename, "r") as f:
            content = f.read()
        
        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as f:
            f.write(modified_content)
        

        print(f"File successfully modified! check: {new_filename}")

    except FileNotFoundError:
        print(" Error: The file you entered does not exist. ")

    except PermissionError:
        print( "Error: You don't have the permission to read this file.")
    
    except Exception as e:
        print(f"Unexpected error: {e}")




#Run the program
file_read_write()