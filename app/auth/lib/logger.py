import logging


class FlaskLogger(object):
    logger = None

    def get_logger(self,  log_format='%(asctime)s [%(levelname)s] %(message)s',
                   level='ERROR'):
        self.logger = logging.getLogger('Womply-AWS-logger')
        if self.logger.handlers:
            return self.logger
        else:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(log_format)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

            if level == 'ERROR':
                self.logger.setLevel(logging.ERROR)
            elif level == 'INFO':
                self.logger.setLevel(logging.INFO)
            elif level == 'WARN':
                self.logger.setLevel(logging.WARN)
            elif level == 'FATAL':
                self.logger.setLevel(logging.FATAL)
            else:
                raise ValueError('Unsupported Logging Level. [ERROR, INFO, WARN, FATAL]')

            return self.logger
