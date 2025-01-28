# Cristal NFT

The project is designed to create unique avatar images by combining various layers of images. The layers consist of a **background**, a **base**, and several **additional items** (such as glasses, hats, and ties), allowing for infinite customization combinations.

### Folder Structure:
- **background/**: This folder contains various background images (e.g., apartment, beach, street). Each background image will serve as the base layer for the generated avatars.
- **base/**: This folder contains the default base image, which is required for every generated avatar (e.g., `cristal.png`). The base image will always be combined with one of the background images to form the core of the avatar.
- **Additional Layers (e.g., glasses, hats, ties)**: These folders contain various optional items that can be combined with the base and background layers. The items are optional and can be included or omitted from the final avatar.

### Avatar Generation Logic:
1. The generator starts by selecting a random background image from the **background/** folder.
2. The **base** image is then applied on top of the background image.
3. Optional items from the **additional layers** (like glasses, hats, and ties) are layered on top, forming different combinations.
4. The output is a unique avatar image generated randomly from the available combinations.

The project ensures that each avatar includes at least the background and base layers, and allows for dynamic combinations of additional layers to customize the final avatar image.

Based on [pixel-punk-avatars](https://github.com/pixegami/pixel-punk-avatars)

## Requirements

* Python 3.6 or higher
* [Pillow](https://pillow.readthedocs.io/en/stable/)

## Usage

```bash
python generate_avatar.py
```

## Examples
![ex-001](https://github.com/user-attachments/assets/221c5694-e7cc-495c-97f3-7526e193abda)
![ex-002](https://github.com/user-attachments/assets/62240245-3a71-4434-b63e-15eca0ab4f51)
![ex-003](https://github.com/user-attachments/assets/76067d3b-97ba-42c1-bc82-86507cabf58c)
