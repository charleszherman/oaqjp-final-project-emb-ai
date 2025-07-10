from flask import Flask, render_template, request
from emotion_detection.emotion_detection import emotion_detector
import json

app = Flask("emotionDetector")

@app.route("/")
def index():
    """ root """
    return render_template("index.html")

@app.route('/emotionDetector', methods=["GET"])
def emotion_detector_caller():
  
    text_to_analyze = request.args["textToAnalyze"]
    result = emotion_detector(text_to_analyze)

       
    result_str = json.dumps(result)
    
    formatted_result = "For the given statement, the system response is " + result_str + " The dominant emotion is " + result["dominant_emotion"]
    
    return formatted_result

if __name__ == "__main__":
    app.run(debug = True)