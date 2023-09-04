# CD: ASHKKAN

# Use this library to code.
import json5

"""
This function is supposed to be a function inside 
it to check what format the file is in order to read it.
"""
def CHECKING(file):

    # This function is the same as the checker function.
    def JSON_OR_TEXT():
        try:
            # cheking for file is json or it is not.
            json_data = json5.load(file())
        #If it is not json, it will receive an error and it will be redirected to except.
        except:
            try:
                # Checking whether the file is text or not.
                text_data = file().read()
            # If there is no text file, it will be directed to except.
            except:
                print("Such a file is not supported")
            else:
                # If file is text.
                print(text_data)
        else:
            # If file is json.
            return json_data

    return JSON_OR_TEXT

# Create a decorator to connect the open_file function to checking.
@CHECKING
def OPEN_FILEING():
    pass