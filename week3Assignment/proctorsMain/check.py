import main
import testCases.loading as ltc
import os

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Traverse up one level
group = ["testingFolder", "SE-2437", "SE-2439"]
groupName = group[0]
group_directory = os.path.join(root, groupName)

def get_student_path():
    
    for groupName in group:
        group_directory = os.path.join(root, groupName)
        student_path = os.path.join(group_directory, student_name, "run.py")
        if os.path.exists(student_path):
            return student_path
    return None

# Function to check files for a specific student
def check_student_file(student_name, test_cases={}):

    RED = "\033[91m"   # ANSI code for red text
    RESET = "\033[0m"  # ANSI code to reset text color
    
    student_path = get_student_path()
    if student_path == None:
        print(f"{RED}File not found across all groups {RESET}")
        return []

    print(f"Checking {student_name}...")
    module = main.load_module_from_file(student_path, student_name)
    if not module:
        return []

    messages = []
    messages.append([])
    # Run test cases for each function
    for func_name, test_func in test_cases.items():
        if hasattr(module, func_name):
            success, message = test_func(student_name, module)
            if success:
                messages[-1].append(f"Success/{student_name}/{func_name}: - {message}")
            else:
                messages[-1].append(f"Failed/{student_name}/{func_name}: - {message}")
                if func_name != "prerequisites":
                    # Create a .txt file for failed test cases
                    failure_file_path = os.path.join(group_directory, student_name, f"{func_name}_failure.txt")
                    with open(failure_file_path, "w") as failure_file:
                        failure_file.write(f"Student: {student_name}\n")
                        failure_file.write(f"Function: {func_name}\n")
                        failure_file.write(f"Error Details: {message}\n")
                break
        else:
            messages[-1].append(f"FunctionNotFound/{student_name}/{func_name}")
            break
    return messages

if __name__ == "__main__":
    status = main.clean_student_directories(group_directory)  # Clean up directories before running tests

    if (status):
        # Mapping function names to test cases
        test_cases = ltc.load_test_cases()
        # messages = check_student_files(test_cases)
        # print_messages(messages)
        
        # To test a specific student's file
        student_name = input("Enter student name: ")
        messages_specific = check_student_file(student_name, test_cases)
        main.print_messages(messages_specific)