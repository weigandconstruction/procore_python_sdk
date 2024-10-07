# ScheduleIntegration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **str** | File to use as file data. Note that it&#39;s only possible to post a   file using a multipart/form-data body (see RFC 2388). Most HTTP   libraries will do the right thing when you pass in an open file or   IO stream. | 

## Example

```python
from procore_sdk.models.schedule_integration import ScheduleIntegration

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleIntegration from a JSON string
schedule_integration_instance = ScheduleIntegration.from_json(json)
# print the JSON string representation of the object
print(ScheduleIntegration.to_json())

# convert the object into a dict
schedule_integration_dict = schedule_integration_instance.to_dict()
# create an instance of ScheduleIntegration from a dict
schedule_integration_from_dict = ScheduleIntegration.from_dict(schedule_integration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


