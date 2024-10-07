# RestV10CalendarEventsGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_tasks_last_updated_at** | **datetime** | Timestamp of the most recent change to any task in the schedule | [optional] 
**tasks** | [**List[Task]**](Task.md) | Tasks | [optional] 
**todos** | [**List[ToDo1]**](ToDo1.md) | ToDos | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_calendar_events_get200_response import RestV10CalendarEventsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10CalendarEventsGet200Response from a JSON string
rest_v10_calendar_events_get200_response_instance = RestV10CalendarEventsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10CalendarEventsGet200Response.to_json())

# convert the object into a dict
rest_v10_calendar_events_get200_response_dict = rest_v10_calendar_events_get200_response_instance.to_dict()
# create an instance of RestV10CalendarEventsGet200Response from a dict
rest_v10_calendar_events_get200_response_from_dict = RestV10CalendarEventsGet200Response.from_dict(rest_v10_calendar_events_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


