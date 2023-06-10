from datetime import datetime, timedelta, timezone
from opentelemetry import trace
from lib.db import db
tracer = trace.get_tracer("user.activities")

class UserActivities:
  def run(user_handle):
      with tracer.start_as_current_span("user-activities-mock-data"):
        span = trace.get_current_span()
        now = datetime.now(timezone.utc).astimezone()
        span.set_attribute("app.now", now.isoformat()) 
        model = {
          'errors': None,
          'data': None
        }

        now = datetime.now(timezone.utc).astimezone()

        if user_handle == None or len(user_handle) < 1:
          model['errors'] = ['blank_user_handle']
        else:
          sql = db.template('users','show')
          results = db.query_object_json(sql,{'handle': user_handle})
          model['data'] = results
        span.set_attribute("app.result_length", len(results))
        return model