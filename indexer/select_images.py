from pathlib import Path
import random


def select_images(image_dir, output_file, num_images=800):

    image_paths = sorted(Path(image_dir).glob("*"))

    random.seed(42)
    random.shuffle(image_paths)

    selected = image_paths[:num_images]

    with open(output_file, "w") as f:
        for path in selected:
            f.write(path.as_posix() + "\n")

    print(f"Selected {len(selected)} images.")