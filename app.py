from flask import Flask, render_template, request

app = Flask(__name__)

chat_history = []

def get_reply(message):
    msg = message.lower()

    if "hello" in msg or "hi" in msg:
        return "Hello! How can I help you?"

    elif "how are you" in msg:
        return "I'm just a bot, but I'm doing great!"

    elif "your name" in msg:
        return "I'm your personal chatbot "

    elif "bye" in msg:
        return "Goodbye! Have a nice day!"

    elif "time" in msg:
        from datetime import datetime
        return "Current time is " + datetime.now().strftime("%H:%M:%S")

    elif "date" in msg:
        from datetime import datetime
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "weather" in msg:
        return "I can't check real weather yet, but it's always cool in code "

    elif "help" in msg:
        return "You can ask me about time, date, greetings, etc."

    else:
        return "Sorry, I didn't understand that."

@app.route('/')
def home():
    return render_template("index.html", chats=chat_history)

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form.get('message')

    if not message:
        return render_template("index.html", chats=chat_history)

    reply = get_reply(message)

    chat_history.append(("You", message))
    chat_history.append(("Bot", reply))

    return render_template("index.html", chats=chat_history)

if __name__ == '__main__':
    app.run(debug=True)