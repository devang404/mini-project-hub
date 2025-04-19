# ✅ To-Do List – Streamlit Mini Project

A sleek productivity-focused To-Do List app built using **Python** and **Streamlit**. This app allows users to add, complete, and delete tasks interactively while storing them persistently in a local text file.

---

## 🚀 Features

- Add new tasks instantly
- Mark tasks as completed
- View active and completed tasks separately
- Delete all completed tasks
- Data saved in `todo.txt` for persistence

---

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## 🛠️ How to Run

```bash
streamlit run todolist.py
```

---

## 📁 Folder Structure

```
todo-list/
├── todolist.py          # Main app
├── functions.py         # File read/write utilities
├── todo.txt             # Persistent task storage
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧠 Notes

- `todo.txt` holds all tasks. Completed tasks include `[completed]` as a tag.
- Marking a checkbox marks a task as complete.
- You can remove all completed tasks using a button.

---

## 📜 License

This project is open-source under the MIT License.