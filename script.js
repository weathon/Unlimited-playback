main = function () {
			var context = new AudioContext();
			var fileInput = document.getElementById("fileInput");

			fileInput.onchange = function () {
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
				
				console.log("mt.tempo");
				console.log(mt.tempo);
				console.log("mt.beats");
                console.log(String(mt.beats));
                console.log("Audio Data");
                console.log(audioData)
			}
        }
        

    
// function play()
// {
//     document.getElementById("myaudio").play();
//     var time=0;
//     console.log(mt.beats.length);
//     for(let i=0;i<mt.beats.length;i++)
//     {
//         time+=mt.beats[i];
//         setTimeout(function(){
//             console.log(i)
//         },time*1000)
//     }
// }

// function play()
// {
//     document.getElementById("myaudio").play();
//     console.log(mt.beats.length);
//     for(let i=0;i<mt.beats.length;i++)
//     {
//         setTimeout(function(){
//             console.log(i)
//         },i*1000)
//     }
        

// }


function play()
{
    document.getElementById("myaudio").play();
    console.log(mt.beats.length);
    for(let i=0;i<mt.beats.length;i++)
    {
        setTimeout(function(){
            console.log(i)
            document.getElementById("bar").setAttribute("style","background:#ffffff")
            setTimeout(function(){
                document.getElementById("bar").setAttribute("style","background:#000000")
            },250)
        },mt.beats[i]*1000)
    }
        

}