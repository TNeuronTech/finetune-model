# Copyright (c) TNeuron Technology
# All rights reserved.
#
# This source code's license can be found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    LLM_NAME: str = "openai_chat"
    DB_LOCATION: str = "./data"
    pass


path = Path(__file__).parent.parent.absolute()
settings = Settings(_env_file=path.joinpath(".env"), _env_file_encoding="utf-8")