# Body67


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Meeting Category belongs to | 
**meeting_id** | **int** | The ID of the Meeting the Meeting Category belongs to | 
**meeting_category** | [**MeetingCategory**](MeetingCategory.md) |  | 

## Example

```python
from procore_sdk.models.body67 import Body67

# TODO update the JSON string below
json = "{}"
# create an instance of Body67 from a JSON string
body67_instance = Body67.from_json(json)
# print the JSON string representation of the object
print(Body67.to_json())

# convert the object into a dict
body67_dict = body67_instance.to_dict()
# create an instance of Body67 from a dict
body67_from_dict = Body67.from_dict(body67_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


