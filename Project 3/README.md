# Project 3 

### Phase 1

To run this sample, download or clone it to local and open the index.html directly without building anything.

This sample is from WebRTC official sample repository and it is one of the examples. For other examples in that repository, you can run it simply open the html file.

The expectation for this example is to show a peer to peer connection locally without a server right now.  The web design is pretty simple. When you open the website (index.html), the browser will request to access microphone and camera when you click the "Start". When you give the browser the access, the page will looks like this.

<img src="GetCamera.png">

Then, if you click "call", the js script will create a "remote" object to connect to other "user". If you run it locally, the other "user" is also yourself. The page will looks like this.

<img src="peer2peer.png">

#### Code explanation 

The website request access to user media when you click "Start" button. The code looks like this.

```javascript
async function start() {
  console.log('Requesting local stream');
  startButton.disabled = true;
  try {
    const stream = await navigator.mediaDevices.getUserMedia({audio: true, video: true});
    console.log('Received local stream');
    localVideo.srcObject = stream;
    localStream = stream;
    callButton.disabled = false;
  } catch (e) {
    alert(`getUserMedia() error: ${e.name}`);
  }
}
```

The start function is an async function so that it have to return something. When you click the button, it will become grey and unclickable. Then, It will create a variable called "stream" to get user camera and audio with permission. When you click "Yes" on the pop up, the browser will give permission and the camera will turns on.

The "Call" function, in the next, will create connection between users. It will transfer the video device and audio device data between users. The code looks like this.

```javascript
async function call() {
  callButton.disabled = true;
  hangupButton.disabled = false;
  console.log('Starting call');
  startTime = window.performance.now();
  const videoTracks = localStream.getVideoTracks();
  const audioTracks = localStream.getAudioTracks();
  if (videoTracks.length > 0) {
    console.log(`Using video device: ${videoTracks[0].label}`);
  }
  if (audioTracks.length > 0) {
    console.log(`Using audio device: ${audioTracks[0].label}`);
  }
  const configuration = getSelectedSdpSemantics();
  console.log('RTCPeerConnection configuration:', configuration);
  pc1 = new RTCPeerConnection(configuration);	//Create instance to build connection
  console.log('Created local peer connection object pc1');
  pc1.addEventListener('icecandidate', e => onIceCandidate(pc1, e));
  pc2 = new RTCPeerConnection(configuration);
  console.log('Created remote peer connection object pc2');
  pc2.addEventListener('icecandidate', e => onIceCandidate(pc2, e));
  pc1.addEventListener('iceconnectionstatechange', e => onIceStateChange(pc1, e));
  pc2.addEventListener('iceconnectionstatechange', e => onIceStateChange(pc2, e));
  pc2.addEventListener('track', gotRemoteStream);

  localStream.getTracks().forEach(track => pc1.addTrack(track, localStream));
  console.log('Added local stream to pc1');

  try {
    console.log('pc1 createOffer start');
    const offer = await pc1.createOffer(offerOptions);
    await onCreateOfferSuccess(offer);
  } catch (e) {
    onCreateSessionDescriptionError(e);
  }
}
```

This function will creates instance to hold the connection and add them to the listen to implement video meeting function. Once the connection established, the listener will keeps tracking the Media stream and load it to local stream and then display it .

The "hangup" function is pretty simple. It will closes pc instances and set them to null. Then , the meeting will be terminated. 

```javascript
function hangup() {
  console.log('Ending call');
  pc1.close();
  pc2.close();
  pc1 = null;
  pc2 = null;
  hangupButton.disabled = true;
  callButton.disabled = false;
}

```

That is the main function in this example, there are still a lot of help function to support the meeting.



### Phase 2



