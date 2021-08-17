import os
import img2pdf


def get_images_paths(path):
    """
    Get all images paths from a directory
    :param path: Path to the directory
    :return: List of paths
    """
    images_paths = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                images_paths.append(os.path.join(root, file))
    return images_paths

def convert_images_to_pdf(images_path, output_path):
    """
    Convert a list of images to a pdf
    :param images_paths: List of paths to the images
    :param output_path: Path to the output pdf
    :return:
    """
    images_paths = get_images_paths(images_path)
    with open(output_path, "wb") as f:
        f.write(img2pdf.convert(images_paths))
    