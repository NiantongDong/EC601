# Project 3 

### Phase 1

To run this sample, download or clone it to local and open the index.html directly without building anything.

This sample is from WebRTC official sample repository and it is one of the examples. For other examples in that repository, you can run it simply open the html file.

The expectation for this example is to show a peer to peer connection locally without a server right now.  The web design is pretty simple. When you open the website (index.html), the browser will request to access microphone and camera when you click the "Start". When you give the browser the access, the page will looks like this.

<img src="GetCamera.png">

Then, if you click "call", the js script will create a "remote" object to connect to other "user". If you run it locally, the other "user" is also yourself. The page will looks like this.

<img src="peer2peer.png">

#### Key feature

This example shows the very simple usage for WebRTC. It can establish connection between user and also access camera and audio on client side. The WebRTC provides various API to implement every function we need for a online meeting.

##### Access camera and audio

###### API usage

We use navigator.mediaDevices.getUserMedia to request access for user media device such as camera and audio. It pass a constraints to get which media we want. For example, if we only need camera, we can set the constraint as 

```javascript
{ video: true}
```

Then, it will only request permission for camera. Also, the script can require permission with parameter. For example, it can set up the resolution for camera.

```javascript
{
  video: {
    width: { min: 1280 },
    height: { min: 720 }
  }
}
```

###### Return Value

The return value of this API is an object and can be stored in local variable, LocalStream. 

###### Exceptions

This API can also raises some exceptions. One of the most common exceptions is that if the user does not give permission, it will throw "NotAllowedError". The other common exceptions are "NotFoundError", which is no device founded, "AbortError", which device prevents the script to use.

##### Call

The next feature for this demo is the RTCPeerConnection API. This API constructs a object which represents the connection between the local user and the remote user. You can also pass your configuration for the connection to construct the object. Otherwise, it will configure to appropriate basic defaults for the connection.

Once you construct the object, you can add them to the event listener to exchange data between local and remote, which is building online meeting.

##### SDP Semantics

This script also support two types of SDP semantics, plan B and unified plan. The Google is preparing to remove the plan B and migrate all current WebRTC app to unified plan.

###### What is SDP Semantics

The SDP message is a message which contains information that describes individual media tracks which is important for us to do peer-to-peer connection. 

###### Difference between plan B and unified plan

Why we don't need plan B anymore?  The first reason is that the plan B assumes all media tracks that share a media type also share a single transport, which will cause a large amount of connections when you do a group meeting. The unified plan will significantly reduces the number of connections by using the SDP specification called BUNDLE.

On the other hands, the plan B also have compatibility issue. A great example from Temasys that "when a peer on a Chrome 71 browser connects to a peer on any Firefox browser updated since 2015. In this case, the peer using Firefox would only be able to see the first tracks of each m= line in a “plan-b” formatted SDP message; Firefox ignores the rest of the tracks in the m= line because it expects to find only one media track in it.".  In that case, the Google is trying to remove plan B so that it won't cause any compatibility issues between peer to peer connection using different browser.



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





### Reference

https://temasys.io/ripping-off-the-band-aid-chromes-shift-to-unified-plan/

