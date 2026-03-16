import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml


def export_envs(environment: str = "dev") -> None:
    load_dotenv(f"config/.env.{environment}")


def load_yaml():
    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
    API = secrets["API"]
    os.environ["API"] = API


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_yaml()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API: ", settings.API)
