# ChatGPTDemo
This is a Demo for application building with ChatGPT/OpenAI API via Python/Flask, deployment to Azure App Service.
Steps:

1. Build

Open your IDE such as VS Code for example. In a terminal,  

```bash
git clone https://github.com/ZEGUK/ChatGPTDemo.git
```

<aside>
💡 index.html for front render template.

Modify with your own OpenAI API Key and save file.
  
</aside>

Run the application in [localhost](http://localhost) to validating that the web app is ready.

```bash
cd chatGPTAppdemo

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

flask run
```

2. Deploy
- First, create App Service on Azure.

- Then, deploy our app to Azure App Service. Here, we choose Local Git. 在本地存储库中，配置一个指向 Azure 的、以将代码推送到 Azure 的 [Git remote 命令](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)可以使用 Azure 门户或 Azure CLI 检索用于配置的远程存储库 URL 和 Git 凭据。

<aside>
💡 Username: $chatGPTAppdemo

</aside>

git-deployment-url: [https://chatgptappdemo.scm.azurewebsites.net:443/chatGPTAppdemo.git](https://chatgptappdemo.scm.azurewebsites.net/chatGPTAppdemo.git)

```bash
git remote add azure <git-deployment-url>
```

本地repo commit:

```bash
git add app.py
git commit -m 'message'
```

```bash
git push azure
# Or
git push azure main: master
```

- When complete the deployment, you can find URL of the App Service

[https://chatgptappdemo.azurewebsites.net](https://chatgptappdemo.azurewebsites.net/).

Now, you can browse your Chatbot web application.
