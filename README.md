# Events-App
Simple mobile app that allows a client to send requests to a server and pull images, videos, messages and events set by another user.
This gives a two way form of communication.

Main System:
	1.Provide a clear GUI that is easy to follow and understand.
	2.Allow a user to connect to a database over a network.
	3.Establish a connection from the user and the server, using a diffie hellman key exchange to ensure that data is encrypted and safe.
	3.Data sent from database is of json format.
	4.Have information correctly recived from the database and displayed accordingly to the user.
	5.Allow a possible message system - events can be set and then sent to other users as a schedule system.
	6.All data will be stored on a servers database until the tagert date/time is met.

all data is encrypted before it is sent, using the aes block cipher and the diffiehellman key-exchange.
