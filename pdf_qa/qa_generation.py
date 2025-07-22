from transformers import pipeline

# Lightweight model
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(context, question):
    prompt = f"Context: {context}\n\nQuestion: {question}"
    output = generator(prompt, max_length=256, do_sample=True)
    return output[0]['generated_text'].strip()
