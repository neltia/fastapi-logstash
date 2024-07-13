import platform
import logging
import logstash


def get_logger(logger_name):
    os_system = platform.system()
    # windows면 로그 파일에 기록
    print(os_system)
    if os_system.lower() == "windows":
        return create_logger_test(logger_name)
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
    logger.addHandler(logstash.TCPLogstashHandler('logstash', 5044, version=1))
    return logger
