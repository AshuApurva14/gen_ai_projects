import os


def list_files_in_directory(directory):
    """
    Lists all files in the specified directory.

    Args:
        directory (str): The path for the directory to list files from.
    """
    try:
        files = os.listdir(directory)
        print(f"Files in '{directory}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    directory = "./workspaces/gen_ai_projects/work_with_LLMs"

    list_files_in_directory(directory)
    