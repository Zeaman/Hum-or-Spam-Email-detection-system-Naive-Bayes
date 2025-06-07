# Hum-or-Spam-Email-detection-system: Email Spam Detection System Using Naive Bayes Algorithm

## Introduction
The Naive Bayes algorithm is a simple yet effective method for classifying emails as either ham (genuine) or spam. It works by calculating the probability that an email is spam given the presence of certain words or phrases. The algorithm is based on the assumption that the presence of words or phrases in an email is independent of each other, which is not always true, but it can still be a very effective classifier.

## Naive Bayes Algorithm for Spam Classification
The Naive Bayes algorithm for spam classification can be summarized as follows:

## Training
Train the algorithm on a dataset of labeled emails, where each email is labeled as either ham or spam. This involves calculating the probability of each word or phrase appearing in both ham and spam emails.

## Classification
For a new email, calculate the probability that the email is spam given the presence of certain words or phrases. If the probability is greater than a threshold, classify the email as spam.

## Implementation with TKinter GUI

To implement the Naive Bayes algorithm for spam classification using TKinter GUI, follow these steps:
Import Libraries: Import the necessary libraries, including tkinter, pandas, and numpy.
Load Training Data: Load the training dataset into a pandas DataFrame.
Train Naive Bayes Classifier: Train the Naive Bayes classifier using the training dataset.
Create GUI: Create the TKinter GUI for the spam classification application.
Handle User Input: Implement functions to handle user input, such as selecting an email file to classify.
Classify Email: Use the trained Naive Bayes classifier to classify the selected email file.
Display Classification Result: Display the classification result (ham or spam) in the GUI.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

MIT License

Copyright (c) 2025 Amanuel Mihiret

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
In the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS ARE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OF OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Amanuel Mihiret (MSc. in Mechatronics Engineering)
zeaman44@gmail.com,
amanmih@dtu.edu.et
