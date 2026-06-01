from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import RESOURCE_ATTRIBUTES, Resource

def setup_opentelemetry(app: FastAPI):
    resource = Resource.create(attributes={
        RESOURCE_ATTRIBUTES.SERVICE_NAME: "agentbridge-backend"
    })
    
    provider = TracerProvider(resource=resource)
    processor = BatchSpanProcessor(ConsoleSpanExporter())
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
