# Import installed requiered dependencies
import joblib 
import tkinter as tk
from tkinter import messagebox 
from sklearn.feature_extraction.text import CountVectorizer
# Load the model and vectorizer
model = joblib.load('spam_classifier_model.joblib')
vectorizer = joblib.load('vectorizer.pkl')
# function for
def check_spam():
    # Get user input
    user_input = entry.get()

    # Vectorize the input
    input_vectorized = vectorizer.transform([user_input])

    # Make prediction
    prediction = model.predict(input_vectorized)

    # Display result in the GUI
    result = "Spam" if prediction[0] == 1 else "Ham"
    result_label.config(text=f"The email is {result}")
    # Create GUI window
window = tk.Tk()
window.title("Email Spam Classifier")

# Create Label for 'Email:'
email_label = tk.Label(window, text="Email:")
email_label.pack(pady=5)

# Create input entry
entry = tk.Entry(window, width=60)
entry.pack(pady=5)

# Create check button
check_button = tk.Button(window, text="Check Spam", command=check_spam)
check_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Run the GUI
window.mainloop()