from transformers import (
    BertTokenizerFast,
    AutoModelForTokenClassification,
    pipeline,
)

tokenizer = BertTokenizerFast.from_pretrained("tokenizer")
model_fine_tuned = AutoModelForTokenClassification.from_pretrained("ner_model") 

nlp = pipeline("ner", model=model_fine_tuned, tokenizer=tokenizer)

example = "Anna is working as an Analytics Engineer at Egnyte in Poznan."
ner_results = nlp(example)
print(ner_results)