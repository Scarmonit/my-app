# OpenTelemetry Tracing Examples

## Automatic Instrumentation

The application automatically traces:
- All `fetch()` API calls
- All `XMLHttpRequest` calls
- Page load events

No additional code is required for these operations to be traced.

## Adding Custom Spans

To add custom tracing to specific operations, use the OpenTelemetry API:

```javascript
import { trace } from '@opentelemetry/api';

function MyComponent() {
  const handleClick = async () => {
    const tracer = trace.getTracer('my-app');
    const span = tracer.startSpan('user-click-action');
    
    try {
      // Your business logic here
      await someOperation();
      span.setStatus({ code: SpanStatusCode.OK });
    } catch (error) {
      span.setStatus({ 
        code: SpanStatusCode.ERROR, 
        message: error.message 
      });
      throw error;
    } finally {
      span.end();
    }
  };

  return <button onClick={handleClick}>Click me</button>;
}
```

## Using Context for Nested Operations

```javascript
import { trace, context } from '@opentelemetry/api';

async function processOrder(orderId) {
  const tracer = trace.getTracer('my-app');
  
  return tracer.startActiveSpan('process-order', async (span) => {
    span.setAttribute('order.id', orderId);
    
    try {
      // These nested operations will be part of the same trace
      await validateOrder(orderId);
      await processPayment(orderId);
      await shipOrder(orderId);
      
      span.setStatus({ code: SpanStatusCode.OK });
    } catch (error) {
      span.recordException(error);
      span.setStatus({ code: SpanStatusCode.ERROR });
      throw error;
    } finally {
      span.end();
    }
  });
}
```

## Configuration

See the main README.md for configuration options.

## Viewing Traces

### Development
Traces are logged to the browser console. Open DevTools > Console to see trace output.

### Production
Configure `REACT_APP_OTEL_EXPORTER_OTLP_ENDPOINT` to send traces to your observability backend.
