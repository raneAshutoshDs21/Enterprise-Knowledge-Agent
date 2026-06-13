import logging

from azure.monitor.opentelemetry import configure_azure_monitor

from src.config import APPLICATIONINSIGHTS_CONNECTION_STRING

print(f"APPLICATIONINSIGHTS_CONNECTION_STRING loaded: {bool(APPLICATIONINSIGHTS_CONNECTION_STRING)}")


if APPLICATIONINSIGHTS_CONNECTION_STRING:
    configure_azure_monitor(
        connection_string=APPLICATIONINSIGHTS_CONNECTION_STRING
    )

logger = logging.getLogger("enterprise_knowledge_agent")
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(logging.StreamHandler())