"""
import requests
import openai

# Set the OpenAI API key
openai.api_key = "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"
# headers = {'Authorization': 'Bearer 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'} #authentication for openAI key


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
            max_tokens=500,
            n=1,
            stop=None,
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)


def main():
    url = "https://www.bbc.com/news/world-67418110"
    response = requests.get(url)
    text = response.text
    # print(text)
    text2 = split_text(text)
    # print(text2)
    text3 = generate_summary(text2)
    print(text3)

if __name__ == '__main__':
    main()
"""

"""
import requests
import openai
import os

# Set the OpenAI API key using an environment variable
openai.api_key = "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"


def split_text(text):
    # Implement a more sophisticated text segmentation method if needed
    # For example, you can use nltk.sent_tokenize() for sentence segmentation
    return [text]


def generate_summary(chunks, max_tokens_per_chunk=30):
    output_chunks = []
    for chunk in chunks:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(f"Please summarize the following text:\n{chunk}\n\nSummary:"),
            temperature=0.5,
            max_tokens=max_tokens_per_chunk,
            n=1,
            stop=None,
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)



def main():
    url = "https://www.bbc.com/news/world-67418110"
    response = requests.get(url)
    text = response.text

    # Split text into chunks
    text_chunks = split_text(text)

    # Generate summary for each chunk
    summary = generate_summary(text_chunks)

    print(summary)


if __name__ == "__main__":
    main()
"""

import requests
import openai
import os

# Set the OpenAI API key using an environment variable
openai.api_key = "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"

def split_text(text):
    # Implement a more sophisticated text segmentation method if needed
    # For example, you can use nltk.sent_tokenize() for sentence segmentation
    return [text]

def generate_summary(chunks):
    output_chunks = []
    for chunk in chunks:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(f"Please summarize the following text:\n{chunk}\n\nSummary:"),
            temperature=0.3,
            max_tokens=500,
            n=1,
            stop=None,
        )
        summary = response.choices[0].text.strip()
        output_chunks.append(summary)
    return " ".join(output_chunks)

def main():
    # Provide the text directly instead of fetching from a URL
    input_text = """
    The September 11 attacks, commonly known as 9/11,[d] were four coordinated Islamist suicide terrorist attacks carried out by al-Qaeda against the United States in 2001. That morning, 19 terrorists hijacked four commercial airliners scheduled to travel from the New England and Mid-Atlantic regions of the East Coast to California. The hijackers crashed the first two planes into the Twin Towers of the World Trade Center in New York City, two of the world's five tallest buildings at the time, and aimed the next two flights toward targets in or near Washington, D.C., in an attack on the nation's capital. The third team succeeded in striking the Pentagon, the headquarters of the U.S. Department of Defense in Arlington County, Virginia, while the fourth plane went down in rural Pennsylvania during a passenger revolt. The attacks killed nearly 3,000 people and instigated the multi-decade global war on terror.
    """

    # Split text into chunks
    text_chunks = split_text(input_text)
    #print(text_chunks)

    # Generate summary for each chunk
    summary = generate_summary(text_chunks)

    #print("here")
    print(summary)

if __name__ == "__main__":
    main()
