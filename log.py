import logging
import mysqlx

logger = logging.getLogger("mysqlx")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s- %(message)s")
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
file_handler = logging.FileHandler("cpy.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler) 