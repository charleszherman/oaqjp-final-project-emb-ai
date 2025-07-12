""" Flask Module for emotion detection """
import json
from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector

app = Flask("emotionDetector")

@app.route("/")
def index():
    """ root for home page / """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detector_caller():
    """ call emotion detector with text provded by user """

    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    result_str = json.dumps(result)

    formatted_result = "For the given statement, the system response is "  \
     + result_str + " The dominant emotion is " + result["dominant_emotion"] + '.'
    formatted_result = formatted_result.replace("{", "")
    formatted_result = formatted_result.replace("}", '')
    formatted_result = formatted_result.replace('"', "'")

    return formatted_result

if __name__ == "__main__":
    app.run(debug = True)
