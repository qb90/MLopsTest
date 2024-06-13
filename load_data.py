import os
import shutil
from datasets import load_dataset

DATA_PATH = "./data"


"""
Loads the Conll2003 dataset and save it to the specified DATA_PATH directory.
Compress the dataset into a zip archive and delete the original directory.
"""
def main():
    conll2003 = load_dataset("conll2003")
    os.makedirs(DATA_PATH, exist_ok=True)
    conll2003.save_to_disk(DATA_PATH)
    print(f"Dataset successfully saved to {DATA_PATH}")
    archive = shutil.make_archive('data', 'zip', DATA_PATH)
    print(f"Dataset compressed to {archive}")
    shutil.rmtree(DATA_PATH)
    print(f"Succesfully deleted {DATA_PATH}")



if __name__ == "__main__":
    main()
