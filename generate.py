import requests
import openai
import os
#from dotenv import load_dotenv

# Set the OpenAI API key using an environment variable
#openai.api_key = os.getenv('api_key')
openai.api_key = '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'
#def configure():
    #load_dotenv()

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
    #configure()
    input_text = """
    Swift has been credited with making a profound impact on the music industry, popular culture and the economy.[481][482] She dominates cultural conversations,[483][484] which has led publications to describe her as a cultural "vitality" or zeitgeist.[485][486][487] Her music, life and public image are points of attention in global celebrity culture.[295] Initially a teen idol,[488] she has been referred to as a pop icon;[310][489] publications describe her immense popularity and longevity as a kind of fame unwitnessed since the 20th century.[490][491] In 2013, New York magazine's Jody Rosen dubbed Swift the "world's biggest pop star" and opined that the trajectory of her stardom has defied established patterns. Rosen added that Swift "falls between genres, eras, demographics, paradigms, trends", leaving her contemporaries "vying for second place".[308] Critics regard Swift as a rare yet successful combination of the pop star and singer-songwriter archetypes.
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
