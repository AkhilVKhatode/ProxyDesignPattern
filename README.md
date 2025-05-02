# Video Streaming Service with Proxy Design Pattern

This project demonstrates a **Proxy Design Pattern** implemented in Python for managing video streaming services. The proxy service controls access to the video content, including permissions, request limits, and caching of video streams.

## Overview

The system consists of:
1. **RealVideoService**: The actual service that streams the videos.
2. **ProxyVideoService**: A proxy service that adds additional functionality like:
   - **Caching**: Videos are cached after the first request for faster subsequent access.
   - **Access Control**: Prevents unauthorized access to premium videos.
   - **Request Limiting**: Limits the number of requests from a user to prevent overuse.

### Key Features:
- **User Permission Handling**: Only premium users can access premium videos.
- **Caching Mechanism**: Streams cached videos if they were previously requested, improving performance.
- **Request Limiting**: Limits the number of video requests a user can make to prevent abuse.
  
## How It Works

1. **RealVideoService**: 
   - The service that actually streams videos.
2. **ProxyVideoService**: 
   - Handles permissions, caching, and request limiting.
   - If a user is free, it restricts access to premium videos.
   - Caches videos after the first stream to speed up subsequent access.
   - Denies access if a user exceeds the allowed number of requests.

The output will demonstrate the following:
- A free user accessing a free video.
- A premium user accessing a premium video.
- An unauthorized user being denied access.
- A free user exceeding the allowed number of requests.

Example Output
```bash
Streaming video: Free Video 1
Streaming video: Premium Video 1
Access denied: Premium video requires a premium account.
Streaming video: Free Video 2
Streaming cached video: Free Video 2
Access denied: Too many requests.
```
