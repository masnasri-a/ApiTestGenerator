import os

def folder_creator(folder_path):
    """
    Create folder if not exist

    Args:
        folder_path (str): forlder path wanna creation.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)