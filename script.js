function upload() {
    var context = new AudioContext();
    var files = fileInput.files;

    if (files.length == 0) return;
    var reader = new FileReader();

    reader.onload = function (fileEvent) {
        context.decodeAudioData(fileEvent.target.result, calcTempo);
    }

    reader.readAsArrayBuffer(files[0]);
}

var calcTempo = function (buffer) {
    var audioData = [];
    // Take the average of the two channels
    if (buffer.numberOfChannels == 2) {
        var channel1Data = buffer.getChannelData(0);
        var channel2Data = buffer.getChannelData(1);
        var length = channel1Data.length;
        for (var i = 0; i < length; i++) {
            audioData[i] = (channel1Data[i] + channel2Data[i]) / 2;
        }
    } else {
        audioData = buffer.getChannelData(0);
    }
    mt = new MusicTempo(audioData);

    //做了这么大半天居然没有想到直接输出mt，文档不全？没看DEMO~
    console.log(mt);
}




function play() {
    document.getElementById("link").setAttribute("src", document.getElementById("fileInput").files)
    document.getElementById("myaudio").play();
    console.log(mt.beats.length);
    for (let i = 0; i < mt.beats.length; i++) {
        setTimeout(function () {
            console.log(i)
            document.getElementById("bar").setAttribute("style", "background:#ffffff")
            setTimeout(function () {
                document.getElementById("bar").setAttribute("style", "background:#000000")
            }, 250)
        }, mt.beats[i] * 1000)
    }


}