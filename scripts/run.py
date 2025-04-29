from pathlib import Path

import hydra
from omegaconf import DictConfig

from dora_utils.launch.run import run

CONFIG_PATH = Path(__file__).parent / "configs"


@hydra.main(config_path=str(CONFIG_PATH), config_name="default", version_base="1.3")
def main(cfg: DictConfig) -> None:
    """Main function to run a dora stack via a hydra configuration yaml file."""
    run(cfg)


if __name__ == "__main__":
    main()
