from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector(): # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response is None or textToAnalyze.strip() == "":
        return "Invalid text! Please try again!"

    # Extract the desc and score from the response
    dom_key, dom_value = response.popitem()
    desc = ''
    for r in response:
        desc += "'" + str(r) + "'" + ': ' + str(response[r]) + ','
    # Return a formatted string with the emotion desc and score
    return """For the given statement, the system
    response is {}. The dominant emotion is {}.""".format(str(desc)
    .replace("{","").replace("}",""), dom_value)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
