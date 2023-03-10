from flask import Flask, render_template, request
import openai
app = Flask(__name__)
openai.api_key = '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'
conversations = []
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    if request.form['question']:
        question = 'Você: ' + request.form['question']

        response = openai.Completion.create(
            engine = 'text-davinci-003',
            prompt = question,
            temperature = 0.5,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6
        )

        answer = 'Chat: ' + response.choices[0].text.strip()

        conversations.append(question)
        conversations.append(answer)

        return render_template('index.html', chat = conversations)
    else:
        return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True, port=4000)