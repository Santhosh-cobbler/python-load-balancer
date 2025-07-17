# Python Load Balancer Simulation

This is a simple hash-based load balancer project I built while learning system design. It simulates request routing to different servers and stores data using MySQL and PyMySQL.

## Features
- Hash-based server selection
- Simulated servers (Server 1, Server 2)
- Data written to MySQL tables
- Modular OOP-based structure

## How it works
- Each request is given an ID and some data
- The load balancer hashes the ID to choose a server
- Data is routed and stored in the corresponding server table

## Future Improvements
- Add round-robin algorithm
- Add multi-threaded request handling
- Use Docker for simulating real servers

## Author
Santhosh R
