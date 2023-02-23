from flask import Flask, request, jsonify,render_template
import openai

app = Flask(__name__)

# 使用 OpenAI API 进行聊天
openai.api_key = 'YOUR_API_KEY'
# 使用Azure OpenAI
#openai.api_key = "REPLACE_WITH_YOUR_API_KEY_HERE"
#openai.api_base =  "REPLACE_WITH_YOUR_ENDPOINT_HERE" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
#openai.api_type = 'azure'
#openai.api_version = '2022-12-01' 

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
