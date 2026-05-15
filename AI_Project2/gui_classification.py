from tkinter import *
from tkinter import messagebox

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# LOAD DATASET
iris = load_iris()

X = iris.data
y = iris.target

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# TRAIN MODEL
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# PREDICT FUNCTION
def predict_flower():

    try:

        sl = float(entry1.get())
        sw = float(entry2.get())
        pl = float(entry3.get())
        pw = float(entry4.get())

        prediction = model.predict(
            [[sl, sw, pl, pw]]
        )

        flower_name = iris.target_names[prediction[0]]

        result_label.config(
            text="Predicted Flower: " + flower_name,
            fg="green"
        )

        history_listbox.insert(
            END,
            f"{sl}, {sw}, {pl}, {pw} → {flower_name}"
        )

    except:

        messagebox.showerror(
            "Error",
            "Enter valid numbers"
        )

# CLEAR FUNCTION
def clear_fields():

    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)

    result_label.config(text="")

# DARK MODE
dark_mode = False

def toggle_theme():

    global dark_mode

    if dark_mode == False:

        root.config(bg="#222222")

        dark_mode = True

    else:

        root.config(bg="#dff6f0")

        dark_mode = False

# GUI WINDOW
root = Tk()

root.title("AI Flower Classification")

root.geometry("500x650")

root.config(bg="#dff6f0")

# TITLE
title = Label(
    root,
    text="AI Flower Classification",
    font=("Arial", 20, "bold"),
    bg="#dff6f0"
)

title.pack(pady=20)

# INPUTS
Label(
    root,
    text="Sepal Length",
    bg="#dff6f0"
).pack()

entry1 = Entry(root)
entry1.pack(pady=5)

Label(
    root,
    text="Sepal Width",
    bg="#dff6f0"
).pack()

entry2 = Entry(root)
entry2.pack(pady=5)

Label(
    root,
    text="Petal Length",
    bg="#dff6f0"
).pack()

entry3 = Entry(root)
entry3.pack(pady=5)

Label(
    root,
    text="Petal Width",
    bg="#dff6f0"
).pack()

entry4 = Entry(root)
entry4.pack(pady=5)

# PREDICT BUTTON
predict_button = Button(
    root,
    text="Predict Flower",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=predict_flower
)

predict_button.pack(pady=15)

# CLEAR BUTTON
clear_button = Button(
    root,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=clear_fields
)

clear_button.pack(pady=10)

# DARK MODE BUTTON
theme_button = Button(
    root,
    text="Toggle Theme",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white",
    command=toggle_theme
)

theme_button.pack(pady=10)

# RESULT LABEL
result_label = Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="#dff6f0"
)

result_label.pack(pady=20)

# HISTORY TITLE
history_title = Label(
    root,
    text="Prediction History",
    font=("Arial", 14, "bold"),
    bg="#dff6f0"
)

history_title.pack(pady=10)

# HISTORY BOX
history_listbox = Listbox(
    root,
    width=50,
    height=8
)

history_listbox.pack(pady=10)

# RUN GUI
root.mainloop()