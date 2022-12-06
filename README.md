# Simplifying English Text  
The web application is located at the following url. http://ec2-18-212-86-77.compute-1.amazonaws.com:5000/form  
Presentation can be found in presentation.mp4 in this git repository https://github.com/ShubhamMMahajan/CS_410_CourseProject/blob/main/presentation.mp4  
  
## Code Overview  
This project takes in complex text and simplifies it. This can be useful when trying to read research papers with complex jargon. This will be helpful for people who may not be proficient in english.  
## Implementation
This code can be broken down into two distinct parts. The first part relates to the preprocessing of the data. The second part is the flask web application where a user can enter in text to get a simplied version of the text.  
### Preprocessing  
The preprocessing of the data is done in scrape_articles.py. We loop through each csv file in the data folder. Each csv file contains rows which represent the article text for that article. Each csv file represents one year of data from the New York Times. We tokenize all the data and calculate the tf and idf of each term. The processed data can be found in tf.txt and idf.txt.  
### Flask Web Application  
The primary file for the web application is in app.py. The web application has two endpoints. The first endpoint (/form), is used for retreiving the complex text. The second endpoint (/data) processes that data by finding complex words in the text and replacing them with more common words. We look at the tf.txt file to determine which is a more common word. The endpoint then returns the simplified text as well as the complex text. We have two templates in this web application both of which are located in the templates directory. The form.html file is the template used to retrieve the complex text. The data.html is the template used to display both the simplified and complex text.  
## Usage  
The web application is located at the following url. http://ec2-18-212-86-77.compute-1.amazonaws.com:5000/form  
The usage should be fairly intuitive. Users can enter in complex text using the input box provided then hit the submit button. The submit button will display the complex text as well as the simplified text. There is a button to go back to original page if the user wants to enter in another input.  
## Contribution  
This is a one person team so I (Shubham Mahajan) have written all this code.  
## Self Evaluation  
I have completed what I had planned. Unfortunately, I did not get the expected outcome as I did not account for sentence structure or word level ambiguity.

