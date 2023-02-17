from flask import Flask, request, jsonify,render_template
import openai

app = Flask(__name__)

# 使用 OpenAI API 进行聊天
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data['message']
    

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    
    # return answer
    return jsonify({'answer': answer})


if __name__ == '__main__':
    app.run()