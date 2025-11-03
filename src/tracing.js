import { WebTracerProvider } from '@opentelemetry/sdk-trace-web';
import { registerInstrumentations } from '@opentelemetry/instrumentation';
import { FetchInstrumentation } from '@opentelemetry/instrumentation-fetch';
import { XMLHttpRequestInstrumentation } from '@opentelemetry/instrumentation-xml-http-request';
import { DocumentLoadInstrumentation } from '@opentelemetry/instrumentation-document-load';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';
import { BatchSpanProcessor, ConsoleSpanExporter } from '@opentelemetry/sdk-trace-base';
import { resourceFromAttributes } from '@opentelemetry/resources';
import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from '@opentelemetry/semantic-conventions';
import { ZoneContextManager } from '@opentelemetry/context-zone';

/**
 * Initialize OpenTelemetry tracing for the React application.
 * This sets up automatic instrumentation for:
 * - HTTP fetch requests
 * - XMLHttpRequest calls
 * - Document/page load events
 */
export function initTracing() {
  // Create a resource to identify this service
  const resource = resourceFromAttributes({
    [ATTR_SERVICE_NAME]: 'my-app',
    [ATTR_SERVICE_VERSION]: '0.1.0',
  });

  // Create the Web Tracer Provider
  const provider = new WebTracerProvider({
    resource: resource,
  });

  // Determine the exporter based on environment
  // In development, use ConsoleSpanExporter for debugging
  // In production, use OTLPTraceExporter to send traces to a collector
  const isProduction = process.env.NODE_ENV === 'production';
  const otlpEndpoint = process.env.REACT_APP_OTEL_EXPORTER_OTLP_ENDPOINT || 'http://localhost:4318/v1/traces';

  if (isProduction && otlpEndpoint) {
    // Production: Send traces to OTLP collector
    const otlpExporter = new OTLPTraceExporter({
      url: otlpEndpoint,
    });
    provider.addSpanProcessor(new BatchSpanProcessor(otlpExporter));
  } else {
    // Development: Log traces to console for debugging
    provider.addSpanProcessor(new BatchSpanProcessor(new ConsoleSpanExporter()));
  }

  // Register the provider
  provider.register({
    contextManager: new ZoneContextManager(),
  });

  // Register automatic instrumentations
  registerInstrumentations({
    tracerProvider: provider,
    instrumentations: [
      // Instrument fetch API calls
      new FetchInstrumentation({
        propagateTraceHeaderCorsUrls: /.*/,
        clearTimingResources: true,
      }),
      // Instrument XMLHttpRequest calls
      new XMLHttpRequestInstrumentation({
        propagateTraceHeaderCorsUrls: /.*/,
      }),
      // Instrument document load events
      new DocumentLoadInstrumentation(),
    ],
  });

  console.log('OpenTelemetry tracing initialized');
}
