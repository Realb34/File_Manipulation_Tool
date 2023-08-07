# File Manipulator
## Overview
The File Manipulator is a Python script designed to interact with directories and perform specific GUI interactions. It's organized into a class that encapsulates the functionality, making it easy to modify or extend.

### Requirements
- Python 3
- pyautogui library

## Usage
- Clone the repository or download the code.
- Replace the placeholder in the perform_gui_actions method with the actual implementation for GUI interactions.
- Update the base path in the main code section with the actual path to your directory.
- Run the script and follow the prompts.

## Code Structure
1. Class Initialization and Attributes
Defines the initialization method for the FileManipulator class, setting up the base path, ID, and a dictionary to hold the sections.

2. Directory Changing and Processing Sections
Includes methods to change the directory and process the sections, handling file operations, and printing the results.

3. Sector Processing
Processes the sectors by counting the files in each sector and printing the total.

4. GUI Interaction Helper Method
Provides a helper function to perform click and write operations, reducing repetitive code.

5. GUI Interaction Method
A placeholder for the specific GUI interactions. It should be implemented with the actual code to interact with the GUI.

6. Main Code
Creates an instance of the FileManipulator class and calls its methods to perform the desired operations.

## Error Handling
The code includes error handling to catch exceptions that may occur during file operations or GUI interactions, allowing the program to continue running even if an individual operation fails.


