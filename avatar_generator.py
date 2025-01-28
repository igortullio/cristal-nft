from itertools import chain, product
import os
import random
from typing import List
from PIL import Image
from layer import Layer


class AvatarGenerator:
    def __init__(self, images_path: str):
        self.background_layers: Layer
        self.base_layers: Layer
        self.additional_layers: List[Layer] = []
        self.output_path: str = "./output"
        os.makedirs(self.output_path, exist_ok=True)
        self.load_all_layers(images_path)

    def load_all_layers(self, images_path: str):
        sub_paths = sorted(os.listdir(images_path))
        for sub_path in sub_paths:
            layer_path = os.path.join(images_path, sub_path)
            if sub_path == 'background':
                self.background_layers = Layer(layer_path)
            elif sub_path == 'base':
                self.base_layers = Layer(layer_path)
            else:
                self.additional_layers.append(Layer(layer_path))

    def execute(self):
        print("AvatarGenerator: generating avatars!")
        combinations = self.generate_combinations()
        sequences = self.generate_random_numbers(len(combinations))
        for i, combination in enumerate(combinations):
            self.save_image(sequences[i], self.render_avatar_image(combination), combination)

    def generate_random_numbers(self, numberOfCombinations):
        numbers = list(range(1, numberOfCombinations + 1))
        random.shuffle(numbers)
        return numbers

    def render_avatar_image(self, image_path_sequence: List[str]) -> Image.Image:
        image = Image.new("RGBA", (768, 1024), 0)
        for image_path in image_path_sequence:
            layer_image = Image.open(image_path).convert("RGBA")
            image = Image.alpha_composite(image, layer_image)
        return image

    def save_image(self, sequence: int, image: Image.Image, image_path_sequence: List[str]):
        image_postfix = '_'.join([os.path.basename(image_path).replace(".png", "") for image_path in image_path_sequence if 'base' not in image_path])
        image_file_name = f"{sequence:03}__{image_postfix}.png"
        image_save_path = os.path.join(self.output_path, image_file_name)
        image.save(image_save_path)

    def generate_combinations(self):
        all_combinations = []
        for background in self.background_layers.images:
            for base in self.base_layers.images:
                base_combination = [background, base]
                layer_images_by_layers = [layer.images for layer in self.additional_layers]
                for subset in self.generate_layer_subsets(layer_images_by_layers):
                    all_combinations.append(base_combination + subset)
        return all_combinations

    def generate_layer_subsets(self, layer_images_by_category):
        subsets = []
        for layer in layer_images_by_category:
            subsets.append([[]] + [[image] for image in layer])
        return [list(chain.from_iterable(combo)) for combo in product(*subsets)]
