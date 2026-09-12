# 🤖 Rule-Based AI Chatbot

A simple **rule-based AI chatbot** built in Python as part of **Artificial Intelligence Project 1**.

This project demonstrates the fundamentals of chatbot development using **control flow, decision-making, and predefined rules**. Instead of using machine learning, the chatbot responds to specific user inputs using `if-elif-else` conditions.

## 📌 Project Overview

The chatbot continuously takes input from the user and provides a predefined response based on the entered message.

It can recognize common greetings, answer basic questions, provide help, and exit the conversation when the user enters an exit command.

The project focuses on understanding how explicit programming rules can be used to simulate basic human-computer interaction.

## ✨ Features

* 👋 Responds to greetings such as `hello`, `hi`, and `hey`
* 😊 Responds to "how are you"
* 🤖 Tells the user what type of chatbot it is
* ❓ Provides instructions when `help` is entered
* 🌞 Responds to questions about having a good day
* 👍 Responds when the user says they are doing well
* 🚪 Supports exit commands such as:

  * `bye`
  * `exit`
  * `quit`
* 🔄 Runs continuously until the user chooses to exit
* 🧹 Converts user input to lowercase and removes extra spaces for easier matching

## 🛠️ Technologies Used

* **Python 3**
* `if-elif-else` conditional statements
* `while` loop
* User input/output
* String methods such as `.strip()` and `.lower()`

## 🧠 How It Works

The chatbot follows a simple rule-based decision-making process:

1. The program starts and displays a welcome message.
2. It asks the user to enter a message.
3. The input is cleaned using `.strip()` and `.lower()`.
4. The chatbot checks the input against predefined conditions.
5. If a matching rule is found, the corresponding response is displayed.
6. If the user enters `bye`, `exit`, or `quit`, the chatbot ends the conversation.
7. If no rule matches, the chatbot responds that it does not understand the input.
8. The process continues until an exit command is entered.

### Example

```text
Chatbot: Hello! Type 'bye' to exit.
You: hello
Chatbot: Hello! How can I help you?

You: how are you
Chatbot: I'm doing well, thanks for asking!

You: what is your name
Chatbot: I'm a simple rule-based chatbot.

You: bye
Chatbot: Goodbye!
```

## 📂 Project Structure

```text
rule-based-chatbot/
│
├── chatbot.py
└── README.md
```

* `chatbot.py` — Contains the complete Python chatbot program.
* `README.md` — Contains information about the project, its features, and how to run it.

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 3. Open the Project Folder

```bash
cd rule-based-chatbot
```

### 4. Run the Chatbot

```bash
python chatbot.py
```

## 💬 Supported Inputs

| User Input                  | Chatbot Response                          |
| --------------------------- | ----------------------------------------- |
| `hello` / `hi` / `hey`      | Greeting                                  |
| `how are you`               | Gives its current status                  |
| `what is your name`         | Identifies itself as a rule-based chatbot |
| `help`                      | Shows available interactions              |
| `are you having a good day` | Responds positively                       |
| `is your day going well`    | Responds positively                       |
| `I'm doing well, thank you` | Responds positively                       |
| `bye` / `exit` / `quit`     | Ends the chatbot                          |

Any input that is not included in the predefined rules receives:

```text
Chatbot: I don't understand that yet.
```

## 🎯 Learning Objectives

This project demonstrates the following foundational concepts:

* **Control Flow**
* **Decision-Making Logic**
* **Conditional Statements**
* **Loops**
* **User Input Handling**
* **String Processing**
* **Basic Rule-Based AI Concepts**

The project demonstrates how a machine can be taught to respond to specific situations through explicit `if-else` instructions rather than learning from data.

## 🚀 Possible Improvements

The chatbot can be expanded by:

* Adding more questions and responses
* Supporting more variations of the same input
* Adding nested conditions
* Giving the chatbot a unique personality
* Expanding its vocabulary
* Adding more advanced conversation rules

These types of extensions are also suggested in the project material as ways to experiment beyond the basic implementation.

## 👩‍💻 Author

**Laiba Noor**

Artificial Intelligence — Project 1
Rule-Based AI Chatbot
