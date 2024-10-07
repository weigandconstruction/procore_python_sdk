# RestV10ScheduleTypeGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | Schedule type key | [optional] 
**p6_id** | **str** | Schedule type Primavera P6 Identifier | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_schedule_type_get200_response import RestV10ScheduleTypeGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ScheduleTypeGet200Response from a JSON string
rest_v10_schedule_type_get200_response_instance = RestV10ScheduleTypeGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ScheduleTypeGet200Response.to_json())

# convert the object into a dict
rest_v10_schedule_type_get200_response_dict = rest_v10_schedule_type_get200_response_instance.to_dict()
# create an instance of RestV10ScheduleTypeGet200Response from a dict
rest_v10_schedule_type_get200_response_from_dict = RestV10ScheduleTypeGet200Response.from_dict(rest_v10_schedule_type_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


