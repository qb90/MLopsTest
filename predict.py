import datasets
import json
from transformers import (
    BertTokenizerFast,
    AutoModelForTokenClassification,
    pipeline,
)

label_mapping = {
    "LABEL_0": "O",
    "LABEL_1": "I-PER",
    "LABEL_2": "O-PER",
    "LABEL_3": "I-ORG",
    "LABEL_4": "O-ORG",
    "LABEL_5": "I-LOC",
    "LABEL_6": "O-LOC",
    "LABEL_7": "I-MISC",
    "LABEL_8": "O-MISC",
}


def format_ner_results(ner_results, label_mapping):
    formatted_results = []
    for entity in ner_results:
        label = label_mapping.get(entity["entity"], "UNKNOWN")
        formatted_result = {
            "Entity": entity["word"],
            "Type": label,
            "Score": entity["score"],
            "Start": entity["start"],
            "End": entity["end"],
        }
        formatted_results.append(formatted_result)
    return formatted_results


def merge_tokens(ner_results):
    merged_results = []
    current_entity = None

    for entity in ner_results:
        word = entity["word"]
        if word.startswith("##"):
            if current_entity:
                current_entity["Entity"] += word[2:]
                current_entity["End"] = entity["end"]
                current_entity["Score"] = float(
                    min(current_entity["Score"], entity["score"])
                )
        else:
            if current_entity:
                merged_results.append(current_entity)
            current_entity = {
                "Entity": word,
                "Type": label_mapping.get(entity["entity"], "UNKNOWN"),
                "Score": float(entity["score"]),
                "Start": entity["start"],
                "End": entity["end"],
            }

    if current_entity:
        merged_results.append(current_entity)

    return merged_results


# Load tokenizer and model
tokenizer = BertTokenizerFast.from_pretrained("tokenizer")
model_fine_tuned = AutoModelForTokenClassification.from_pretrained("ner_model")

# Initialize the pipeline
nlp = pipeline("ner", model=model_fine_tuned, tokenizer=tokenizer)

data_path = "./data-conll2003"
conll2003 = datasets.load_dataset("conll2003", data_dir=data_path)
res = {'results': []}
for idx, example in enumerate(conll2003["test"]):
    words = example['tokens']
    sentence = " ".join(words)
    ner_results = nlp(sentence)
    merged_results = merge_tokens(ner_results)
    new_res = {
        'sentence': sentence,
        'results': merged_results,
    }
    res["results"].append(new_res)

with open("ner_results.json", "w") as file:
    json.dump(res, file, separators=(',', ':'))

print("Results saved to ner_results.json")