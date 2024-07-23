# Multiplayer Hand Cricket Game

A real-time multiplayer hand cricket game developed using Python's socket programming. This game allows two players to compete against each other, alternating between batting and bowling.

## Features

- **Client-Server Communication:** Utilizes Python’s `socket` library for real-time data exchange between clients and the server.
- **Turn-Based Gameplay:** Players alternate between batting and bowling, with the server managing game state and scoring.
- **Error Handling:** Includes input validation and error handling to ensure smooth gameplay and accurate results.

## Technologies Used

- Python
- Socket Programming

## How to Run

1. **Start the Server:**
   - Open a terminal and navigate to the directory containing `server.py`.
   - Run the server with the command:
     ```bash
     python server.py
     ```

2. **Start the Client:**
   - Open another terminal and navigate to the directory containing `client.py`.
   - Run the client with the command:
     ```bash
     python client.py
     ```

3. **Gameplay:**
   - The client will prompt you for your name and provide instructions for playing.
   - Players alternate between bowling and batting as per the game rules.
   - The server will announce the winner based on the scores.

## Files

- `server.py`: Contains the server-side code for handling game logic and communication.
- `client.py`: Contains the client-side code for user interaction and game play.

## Notes

- Ensure that both the server and client are using the same host and port settings.
- This game is designed for local play on the same network.

