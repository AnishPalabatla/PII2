import spacy
def pii_with_ner(text):
    nlp = spacy.load("en_core_web_sm") #Loading the NER model (Named Entity Recognition)
    doc = nlp(text) #Processing the text
    result = []
    for token in doc:
        if token.ent_type_ in ['PERSON', 'ORG', 'GPE', 'DATE', 'CARDINAL', 'MONEY']:
            result.append("[CENSORED]")
        else:
            result.append(token.text)
    redacted_text = ' '.join(result)
    return redacted_text
text_with_pii = "Anish's email is test@temp.com and his phone number is 123-456-7890, SSN is 765-433-123"
output = pii_with_ner(text_with_pii)
print(output)