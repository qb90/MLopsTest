import os
from datasets import load_dataset


def load_data(dir_path):

    conll2003 = load_dataset("conll2003")
    os.makedirs(dir_path, exist_ok=True)
    conll2003.save_to_disk(dir_path)
    print(f"Dataset successfully saved to {dir_path}")


load_data("./data")
