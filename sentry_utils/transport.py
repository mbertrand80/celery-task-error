from __future__ import absolute_import
import json
import zlib
import logging

from sentry_sdk.transport import Transport as SentrySDKTransport


logger = logging.getLogger()

class TestSentrySDKTransport(SentrySDKTransport):
    """A Sentry transport that collects captured output and stores it for use in testing

    This transport will NOT send data to Sentry.

    To access this data, do the following:

    ```
    from sentry_sdk.hub import Hub
    captured_events = Hub.current.client.transport.captured
    ```
    If `transport` is `None` that means no events were captured. The tranport is
    instantiated on the first event report.
    """
    captured = []

    def capture_event(self, event):
        logger.debug('~~Capturing an event in the test transport %s' % event.get('event_id'))
        self.captured.append(event)
