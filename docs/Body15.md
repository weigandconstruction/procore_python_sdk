# Body15


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Schedule Type belongs to | 
**type** | [**ScheduleType**](ScheduleType.md) |  | 

## Example

```python
from procore_sdk.models.body15 import Body15

# TODO update the JSON string below
json = "{}"
# create an instance of Body15 from a JSON string
body15_instance = Body15.from_json(json)
# print the JSON string representation of the object
print(Body15.to_json())

# convert the object into a dict
body15_dict = body15_instance.to_dict()
# create an instance of Body15 from a dict
body15_from_dict = Body15.from_dict(body15_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


