import cv2
import numpy as np
from PIL import Image, ImageDraw
import os
import argparse

def is_fully_white(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}.")
        return False

    return np.all(image == 255)

def detect_dot(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image {image_path}.")
        return None, None

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not contours:
        print(f"Warning: No dot detected in {os.path.basename(image_path)}")
        return None, None

    dot_contour = max(contours, key=cv2.contourArea)
    M = cv2.moments(dot_contour)

    if M["m00"] == 0:
        return None, None

    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])

    cx = min(max(cx, 0), image.shape[1] - 1)
    cy = min(max(cy, 0), image.shape[0] - 1)

    color = image[cy, cx].tolist()
    print(f"Detected dot at ({cx}, {cy}) with color {color} in {os.path.basename(image_path)}")

    return (cx, cy), color

def stitch_images(input_folder, output_image_path):
    def extract_layer_number(filename):
        try:
            return int(os.path.splitext(filename)[0].replace('Layer ', ''))
        except ValueError:
            return -1

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    image_files = [f for f in image_files if extract_layer_number(f) != -1]
    image_files = sorted(image_files, key=extract_layer_number)

    if not image_files:
        print("No valid images found in the specified folder.")
        return

    lines = []
    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)

        if is_fully_white(image_path):
            print(f"Line break detected at {image_file}, no line will be drawn from this image.")
            lines.append((None, None))
            continue

        dot, color = detect_dot(image_path)

        if dot is None:
            print(f"Skipping {image_file} due to no dot detected")
            continue

        lines.append((dot, color))

    if not lines:
        print("No dots detected, no image saved.")
        return

    max_x = max((dot[0] for dot, _ in lines if dot), default=0) + 20
    max_y = max((dot[1] for dot, _ in lines if dot), default=0) + 20

    output_image = Image.new('RGB', (max_x, max_y), (255, 255, 255))
    draw = ImageDraw.Draw(output_image)

    prev_dot = None
    for dot, color in lines:
        if dot is None:
            prev_dot = None
            continue

        if prev_dot:
            line_color = (255, 255, 0) if color == [7, 193, 255] else tuple(color)
            print(f"Drawing line from {prev_dot} to {dot} with color {line_color}")
            draw_line(prev_dot, dot, line_color, draw)

        prev_dot = dot

    output_image.save(output_image_path)
    print(f"Stitched image saved to {output_image_path}")

def draw_line(start, end, color, draw):
    if start == end:
        return
    draw.line([start, end], fill=color, width=2)

if __name__ == "__main__":
    input_folder = '/home/shruthik/Operation-Pixel-Merge/assets'  # Updated input folder
    output_file = 'stitched_image.png'  # You can modify the output file name if needed

    stitch_images(input_folder, output_file)
