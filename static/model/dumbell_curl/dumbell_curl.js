let status = "straight"
let count = 0
async function predict() {
    // Prediction #1: run input through posenet
    // estimatePose can take in an image, video or canvas html element
    const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
    // Prediction 2: run input through teachable machine classification model
    const prediction = await model.predict(posenetOutput);
    if(prediction[0].probability.toFixed(2) > 0.70){
        console.log("straight")
        status = "straight"
    } else if(prediction[1].probability.toFixed(2) > 0.90){
        console.log("no straight dumbell_curl")
        if(status == "straight"){
            console.log("dumbell_curl")
            count++
            console.log("count", count)
            var audio = new Audio('/static/sound/' + count%10 + '.mp3');
            audio.play();
            
        }
        status = "dumbell_curl"         
    } else if(prediction[2].probability.toFixed(2) > 0.50){
        console.log("bent")
        if(status == "straight" || status == "dumbell_curl"){
            var audio = new Audio('/static/sound/bent.mp3');
            audio.play();
        }
        status = "bent"
    }
    for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
    }

    // finally draw the poses
    drawPose(pose);
}