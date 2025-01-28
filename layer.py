import os
from typing import List


class Layer:
    def __init__(self, path: str):
        self.path = path
        self.images = self.build_images()

    def build_images(self) -> List[str]:
        image_file_names = os.listdir(self.path)
        images = [os.path.join(self.path, f) for f in image_file_names if f.endswith('.png')]
        return images
