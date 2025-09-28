from pathlib import Path

from click.testing import CliRunner
from PIL import Image
from PIL import ImageChops
import tomli_w

from random_tile_generator.__main__ import cli


def test_100_percent_one_tile(
    data_dir: Path, runner: CliRunner, tmp_path: Path
) -> None:
    config_path = tmp_path / "config.toml"
    config_path.write_text(
        tomli_w.dumps(
            {
                "images": {"blue": str(data_dir / "blue-tile.png")},
                "tile-size": {"width": 16, "height": 16},
                "grout": {"color": "white", "width": 1},
                "layout": {"width": 10, "height": 5},
                "ratios": {"blue": 100},
            }
        )
    )

    output_path = tmp_path / "out.png"

    result = runner.invoke(cli, [str(config_path), str(output_path)])
    assert result.exit_code == 0

    output = Image.open(output_path)
    expected = Image.open(data_dir / "test_100_percent_one_tile.png")
    diff = ImageChops.difference(output, expected)
    assert diff.getbbox(alpha_only=False) is None
