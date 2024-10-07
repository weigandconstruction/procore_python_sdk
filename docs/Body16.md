# Body16


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Schedule Type belongs to | 
**schedule_type** | [**ScheduleType1**](ScheduleType1.md) |  | 

## Example

```python
from procore_sdk.models.body16 import Body16

# TODO update the JSON string below
json = "{}"
# create an instance of Body16 from a JSON string
body16_instance = Body16.from_json(json)
# print the JSON string representation of the object
print(Body16.to_json())

# convert the object into a dict
body16_dict = body16_instance.to_dict()
# create an instance of Body16 from a dict
body16_from_dict = Body16.from_dict(body16_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


