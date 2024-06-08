import io
import math
import random
import tomllib

import click
from PIL import Image


@click.command()
@click.argument("config", type=click.File("rb"))
@click.argument("output", type=click.Path(dir_okay=False))
def cli(config: io.BytesIO, output: str) -> None:
    parsed_config = tomllib.load(config)

    image_mapping = parsed_config["images"]
    ratios = parsed_config["ratios"]

    # Validate ratios
    if sum(ratios.values()) != 100:
        raise RuntimeError("Tile ratios do not add up to 100!")
    for name in ratios:
        if name not in image_mapping:
            raise RuntimeError(f"{name!r} missing from 'images' config")

    num_tiles_wide = parsed_config["layout"]["width"]
    num_tiles_high = parsed_config["layout"]["height"]
    num_tiles = num_tiles_wide * num_tiles_high

    tile_width = parsed_config["tile-size"]["width"]
    tile_height = parsed_config["tile-size"]["height"]

    # Create the (shuffled) list of tiles
    tiles = []
    for name, percentage in ratios.items():
        tiles.extend([name for _ in range(math.ceil(num_tiles * percentage / 100))])
    random.shuffle(tiles)

    # Generate the tile layout
    result = Image.new(
        "RGBA",
        (
            (num_tiles_wide * tile_width),
            (num_tiles_high * tile_height),
        ),
    )

    for col in range(num_tiles_wide):
        for row in range(num_tiles_high):
            tile_name = tiles.pop()

            with Image.open(image_mapping[tile_name]) as im:
                tile = im.resize((tile_width, tile_height))

            result.paste(tile, (col * tile_width, row * tile_height))

    # Save the tile layout
    result.save(output)


if __name__ == "__main__":
    cli()
