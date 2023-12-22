from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

def split_text(text):
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

@app.route('/generate_summary', methods=['POST'])
def generate_summary_route():
    data = request.get_json()
    text = data['text']
    text_chunks = split_text(text)
    summary = generate_summary(text_chunks)
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(port=5001)  # Change the port as needed
