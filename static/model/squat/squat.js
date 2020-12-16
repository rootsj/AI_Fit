//처음 상태는 stand, count는 0개
let status = "stand";
let count = 0;
let bentcount = 0;

//predict() 예측합수는 model을 이용하여 webcam.canvas 이미지로 예측한다.
async function predict() {
    // Prediction #1: run input through posenet
    // estimatePose can take in an image, video or canvas html element
    const { pose, posenetOutput } = await model.estimatePose(webcam.canvas);
    // Prediction 2: run input through teachable machine classification model
    const prediction = await model.predict(posenetOutput);

    if (prediction[0].probability.toFixed(2) > 0.50) {
        console.log("stand, squat")
        if (status == "squat") {
            count++;
            document.getElementById('counter').innerHTML = count;
            let audio = new Audio('/static/sound/' + count % 10 + '.mp3');
            audio.play();
        }
        status = "stand"
    }

    else if (prediction[1].probability.toFixed(2) > 0.70) {
        console.log("sqaut")
        status = "squat"
    }

    else if (prediction[2].probability.toFixed(2) > 0.90) {
        console.log("bent")

        bentcount++;
        console.log(bentcount)

        if (bentcount % 40 == 0) {
            status = "bent"
            console.log(bentcount)
            let audio = new Audio('/static/sound/bent.mp3');
            audio.play();
        }
    }

    for (let i = 0; i < maxPredictions; i++) {
        const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
        labelContainer.childNodes[i].innerHTML = classPrediction;
    }

    // finally draw the poses
    drawPose(pose);
}