import requests
import openai

# Set the OpenAI API key
openai.api_key = "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"
headers = {'Authorization': 'Bearer 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'} #authentication for openAI key

def split_text(text):
    max_chunk_size = 2048
    chunks = []
    current_chunk = ""
    for sentence in text.split("."):
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + "."
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + "."
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def generate_summary(text):
    input_chunks = text
    output_chunks = []
    for chunk in input_chunks:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(f"Please summarize the following text:\n{chunk}\n\nSummary:"),
            temperature=0.5,
            max_tokens=1024,
            n = 1,
            stop = None
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)

def main():
    
    url = "https://www.bbc.com/news/world-67418110"
    response = requests.get(url)
    text = response.text 
    #print(text)
    text2 = split_text(text)
    #print(text2)
    text3 = generate_summary(text2)
    print(text3)
    
main()