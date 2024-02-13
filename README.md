# Detect Emotion from a Given Text
This repo is for a reflection on my attempt to learn and implement my gained knowledge in the area of Flask Web Application framework, Python programming (Unit Testing, Packaging Modules, Error handling & PEP8 guidelines) and RESTful Api. 

This is a practice project where in I have demonstrated my programming skills in developing an AI based Application using Python and Flask. I have integrated the Web app with Watson-NLP AI library <b>(based on Emotion Detection Function of the Watson NLP Library)</b> which is used to perfome <b>"Emotion Detection"</b> for a given text. In other words, this AI application will detect the emotion with which a given text was written.

## A sample code for such an application could be
```python
import requests
def <function_name>(<input_args>):
    url = '<relevant_url>'
    headers = {<header_dictionary>}
    myobj = {<input_dictionary_to_the_function>}
    response = requests.post(url, json = myobj, headers=header)
    return response.text
``` 

Since I made use of the IBM Watson AI Library services, to access this function, the UTL, headers and input json format is as follows
```python 
URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
Input json: { "raw_document": { "text": text_to_analyse } }
````
A sample application response for a given etxt input <i>"I love this new technology"</i> is something like this 
```json
{'anger': 0.025952177, 'disgust': 0.022372011, 'fear': 0.17840633, 'joy': 0.61990315, 'sadness': 0.20243862, 'dominant_emotion': 'joy'}
````
## Summary
With this project, I have successfully
* Created an Emotion Detection application using the functions from embeddable AI libraries

* Extracted relevant information from the output received from the function

* Tested and packaged the application created using the Emotion Detection function

* Completed web deployment of my application using Flask

* Incorporated error handling in my application to account for invalid input to your application

* Written codes that are in perfect compliance with PEP8 guidelines, getting 10/10 score in static code analysis

© IBM Corporation 2023. All rights reserved.