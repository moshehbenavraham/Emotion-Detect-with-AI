/**
 * Run emotion analysis on the text input by the user.
 * Sends the text to the server and displays the result.
 */
let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    let systemResponse = document.getElementById("system_response");

    // Validate input
    if (!textToAnalyze.trim()) {
        systemResponse.innerHTML = "Please enter some text to analyze.";
        return;
    }

    // Encode the text for safe URL transmission
    let encodedText = encodeURIComponent(textToAnalyze);

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                systemResponse.innerHTML = xhttp.responseText;
            } else {
                systemResponse.innerHTML = "Error: Unable to process request. Please try again.";
            }
        }
    };
    xhttp.onerror = function() {
        systemResponse.innerHTML = "Network error: Please check your connection and try again.";
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodedText, true);
    xhttp.send();
};
