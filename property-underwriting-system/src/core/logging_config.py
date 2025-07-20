import logging

def setup_logging(log_file: str = "logs/app.log"):
    # Create logs directory if it doesn’t exist
    import os
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logging.info("Logging setup complete.")
