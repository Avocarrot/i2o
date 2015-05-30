
<img src="https://cloud.githubusercontent.com/assets/1907604/7896840/4cb417da-06cf-11e5-9e17-b21b37839323.jpg" width=70>

# i2o
A library to connect input connectors to specific outputs

#### Play sounds

**Endpoint** 

```
http://localhost:8000/events/send
```


**Request body - Play sound from file**

```json
{
	"cmd" : "play -f users/batman.wav"
}
```

**Request body - Play sound from url**

```json
{
	"cmd" : "play -u https://www.youtube.com/watch?v=3R5gHF0vzew"
}
```

#### Text to speech

**Endpoint** 

```
http://localhost:8000/events/send
```

**Request body**

```json
{
	"cmd" : "speak -m 'hello Pano'"
}
```
