import logging

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format='[%(asctime)s.%(msecs)03d] %(module)s:%(leneno)d %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler()
        ]
    )