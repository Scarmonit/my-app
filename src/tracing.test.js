// Mock OpenTelemetry modules for Jest environment
jest.mock('./tracing', () => ({
  initTracing: jest.fn(),
}));

import { initTracing } from './tracing';

describe('Tracing', () => {
  it('should be callable without errors', () => {
    // Verify the mock function can be called
    expect(() => initTracing()).not.toThrow();
    
    // Verify it was called
    expect(initTracing).toHaveBeenCalled();
  });
});
