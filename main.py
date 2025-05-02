# VideoServiceInterface.py
from abc import ABC, abstractmethod

class VideoServiceInterface(ABC):
    @abstractmethod
    def play_video(self, user_type, video_name):
        pass

# RealVideoService.py
class RealVideoService(VideoServiceInterface):
    def play_video(self, user_type, video_name):
        print(f"Streaming video: {video_name}")

# ProxyVideoService.py
class ProxyVideoService(VideoServiceInterface):
    def __init__(self, real_video_service):
        self.real_video_service = real_video_service
        self.cached_videos = {}
        self.request_counts = {}

    def play_video(self, user_type, video_name):
        # Check user permissions
        if user_type != "premium" and video_name.startswith("Premium"):
            print("Access denied: Premium video requires a premium account.")
            return

        # Limit requests
        self.request_counts[user_type] = self.request_counts.get(user_type, 0) + 1
        if self.request_counts[user_type] > 5:
            print("Access denied: Too many requests.")
            return

        # Caching logic
        if video_name in self.cached_videos:
            print(f"Streaming cached video: {video_name}")
        else:
            self.real_video_service.play_video(user_type, video_name)
            self.cached_videos[video_name] = video_name

# Main.py
def main():
    real_service = RealVideoService()
    proxy_service = ProxyVideoService(real_service)
    
    # Free user trying to watch a video
    proxy_service.play_video("free", "Free Video 1")
    
    # Premium user trying to watch a video
    proxy_service.play_video("premium", "Premium Video 1")
    
    # Unauthorized user
    proxy_service.play_video("guest", "Video 1")
    
    # Too many requests
    for _ in range(6):
        proxy_service.play_video("free", "Free Video 2")

if __name__ == "__main__":
    main()
