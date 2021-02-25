import logging
import sys
from pathlib import Path

import click

from extra_model._errors import ExtraModelError
from extra_model._run import run


logger = logging.getLogger(__name__)


@click.command()
@click.argument(
    "input_path",
    type=Path
)
@click.argument(
    "output_path",
    type=Path,
    default="/app/output"
)
@click.option(
    "--debug",
    is_flag=True,
    help="Enable debug logging"
)
def entrypoint(input_path: Path, output_path: Path, debug: bool = False) -> None:
    """Run the Extra algorithm for unsupervised topic extraction.

    INPUT_PATH is the path to the input parquet file with the user generated texts.
    
    OUTPUT_PATH is the path to the output directory. Default is /app/output
    \f
    
    :param input_path: Path to the input parquet file.
    :param output_path: Path to the output directory.
    :param debug: Enable debug logging.
    """
    logging.getLogger("extra_model").setLevel("DEBUG" if debug else "INFO")

    try:
        run(input_path, output_path)
    except ExtraModelError as e:
        logger.exception(e) if debug else logger.error(e)
        sys.exit(1)
