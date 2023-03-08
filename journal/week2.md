# Week 2 — Distributed Tracing

## Observability Security Considerations

After watching Ashish's video of Security consideration in observability, Here are some security considerations to keep in mind when implementing observability:

Data privacy: Make sure that sensitive data is not exposed through your observability infrastructure.

Access control: Limit access to your observability infrastructure to only those who need it.

Authentication and authorization: Use strong authentication and authorization mechanisms to control access to your observability infrastructure.

Encryption: Make sure that all data transmitted over the network is encrypted to prevent eavesdropping and tampering.

Monitoring and alerting: Monitor your observability infrastructure for signs of unauthorized access or suspicious activity. Set up alerts to notify you of potential security incidents.

Secure coding practices: Follow secure coding practices when developing your instrumentation and observability tools.

Incident response: Have an incident response plan in place in case of a security breach.

By keeping these security considerations in mind, you can help ensure that your observability infrastructure is both effective and secure.


## Add custom instrumentation to Honeycomb to add UserId

<img width="1285" alt="image" src="https://user-images.githubusercontent.com/110344576/223659558-74e4c8d2-b326-45b6-b75a-3e530b2ee3e0.png">

```
from datetime import datetime, timedelta, timezone
from opentelemetry import trace
tracer = trace.get_tracer("user.activities")
class UserActivities:
  def run(user_handle):
      with tracer.start_as_current_span("user-activities-mock-data"):
        span = trace.get_current_span()
        now = datetime.now(timezone.utc).astimezone()
        span.set_attribute("user.id", user_handle) 
        model = {
          'errors': None,
          'data': None
        }

        now = datetime.now(timezone.utc).astimezone()

        if user_handle == None or len(user_handle) < 1:
          model['errors'] = ['blank_user_handle']
        else:
          now = datetime.now()
          results = [{
            'uuid': '248959df-3079-4947-b847-9e0892d1bab4',
            'handle':  'Andrew Brown',
            'message': 'Cloud is fun!',
            'created_at': (now - timedelta(days=1)).isoformat(),
            'expires_at': (now + timedelta(days=31)).isoformat()
          }]
          model['data'] = results
        span.set_attribute("app.result_length", len(results))
        return model
```
## Run custom queries in Honeycomb

<img width="1285" alt="image" src="https://user-images.githubusercontent.com/110344576/223663203-d27d73c2-6f36-4be0-aca3-618ef8090783.png">
