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
        except:
            pass
        else:
            # if file is json.
            return json_data

    return JSON_OR_TEXT