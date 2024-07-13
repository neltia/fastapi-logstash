import platform
import logging
from logstash_async.handler import AsynchronousLogstashHandler


def get_logger(logger_name):
    os_system = platform.system()
    # windows면 로그 파일에 기록
    if os_system.lower() == "windows":
        # return create_logger_test(logger_name)
        return create_logger_logstash(logger_name)
    # 구성된 ELK 환경에 전송
    else:
        return create_logger_logstash(logger_name)


def create_logger_test(logger_name):
    logger = logging.getLogger(logger_name)
    # logger exists
    if len(logger.handlers) > 0:
        return logger

    # Configure logging
    logging.basicConfig(
        filename="app/log/app.log",
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    return logger


def create_logger_logstash(logger_name):
    logger = logging.getLogger(logger_name)
    # logger exists
    if len(logger.handlers) > 0:
        return logger

    logger.setLevel(logging.INFO)
    log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # logger에 핸들러 추가
    console = logging.StreamHandler()
    console.setFormatter(log_format)
    logger.addHandler(console)

    # Logstash에 TCP 전송 이벤트 설정
    async_handler = AsynchronousLogstashHandler(host='127.0.0.1', port=5044, database_path=None)
    logger.addHandler(async_handler)
    return logger
