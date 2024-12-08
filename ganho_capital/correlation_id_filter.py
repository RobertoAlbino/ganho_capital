import logging
import contextvars


class CorrelationIdFilter(logging.Filter):

    correlation_id_var = contextvars.ContextVar("correlation_id", default="N/A")

    def filter(self, record):
        record.correlation_id = self.correlation_id_var.get()
        return True
