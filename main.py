import pyaudio
import numpy as np
import asyncio
import websockets

def calculate_rms(data):
    if len(data) > 0:
        square_mean = np.mean(np.square(data))
        if np.isnan(square_mean):
            return 0.0
        return np.sqrt(square_mean)
    else:
        return 0.0

#async def body_tracking():
#    async with websockets.connect('wss://yourwebsocketurl:443') as websocket:
#        while True:
#            data = await websocket.recv()
            #kick or punch

def main():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    THRESHOLD = 75

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    print("FIGHT! ")
    #asyncio.get_event_loop().run_until_complete(body_tracking())


    try:
        while True:
            data = stream.read(CHUNK)
            audio_data = np.frombuffer(data, dtype=np.int16)
            rms = calculate_rms(audio_data)
            if rms > THRESHOLD:
                print("Punch and Kick stronger! Intensity: {:.2f}".format(rms))
    except KeyboardInterrupt:
        print("Good job!")

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
