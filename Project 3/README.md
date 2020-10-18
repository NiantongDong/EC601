# Project 3 

#### Phase 1

To run this sample, download or clone it to local and open the index.html directly without building anything.

This sample is from WebRTC official sample repository and it is one of the examples. For other examples in that repository, you can run it simply open the html file.

The expectation for this example is to show a peer to peer connection locally without a server right now.  The web design is pretty simple. When you open the website (index.html), the browser will request to access microphone and camera when you click the "Start". When you give the browser the access, the page will looks like this.

<img src="GetCamera.png">

Then, if you click "call", the js script will create a "remote" object to connect to other "user". If you run it locally, the other "user" is also yourself. The page will looks like this.

<img src="peer2peer.png">