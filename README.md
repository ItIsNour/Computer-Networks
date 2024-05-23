# Proxy Server

## Overview

This project implements a simple proxy server using Python's socket module. The proxy server intercepts client requests, forwards them to the appropriate web server, retrieves the responses, and sends them back to the client. Additionally, it includes functionality to cache responses and block certain URLs.

## Getting Started

To run the proxy server, execute the `ProxyServer.py` script. Make sure you have Python installed on your system.

## Features

- Intercepts HTTP requests from clients and forwards them to web servers.
- Caches responses to improve performance and reduce bandwidth usage.
- Blocks access to specific URLs based on a predefined list.
- Handles errors gracefully, including file not found and illegal requests.

## Components Used

- **Socket Programming**: The server utilizes Python's socket module for creating and managing network connections.
- **Webbrowser Module**: Used for opening blocked URLs in a web browser window.
- **File I/O Operations**: The code includes file read and write operations for caching responses and managing the list of blocked URLs.

## Usage

1. Run the `ProxyServer.py` script.
2. Connect to the proxy server using a web browser or other HTTP client.
3. Send HTTP requests to the proxy server, which will forward them to the appropriate web servers.
4. Receive HTTP responses from the proxy server, which may be retrieved from the cache or fetched from the web servers.

## Prerequisites

- Python 3.10

## Contributors

- [Nour Hany](https://github.com/ItIsNour)


## What I Learned

Through this project, I gained practical experience in network programming using Python's socket module. I learned about proxy servers, caching mechanisms, and URL blocking techniques. Additionally, I improved my skills in handling HTTP requests and responses, as well as error handling and file I/O operations.
