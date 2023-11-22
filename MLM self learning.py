from transformers import BertTokenizer, BertForMaskedLM
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForMaskedLM.from_pretrained('bert-base-uncased')

def chunk_input(sequence, chunk_size):
    return [sequence[i:i+chunk_size] for i in range(0, len(sequence), chunk_size)]

with open(r"C:\Users\chris\OneDrive\Desktop\CODING\Fitness App\Txt Data Files\test.txt", 'r', encoding='utf-8') as f_in, open('MLM.txt', 'w', encoding='utf-8') as f_out:
    for line in f_in:
        # Chunk the line into pieces of size 512 or less
        chunks = chunk_input(line, 512)

        for chunk in chunks:
            # Prepare the data
            inputs = tokenizer(chunk, return_tensors='pt')

            outputs = model(**inputs)
            predictions = outputs.logits

            predicted_index = torch.argmax(predictions[0, -1, :]).item()
            predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]

            f_out.write(f"The masked word in '{chunk.strip()}' is: {predicted_token}\n")
