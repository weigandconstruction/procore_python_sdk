# Body17


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the Resource belongs to | 
**resource** | [**Resource1**](Resource1.md) |  | 

## Example

```python
from procore_sdk.models.body17 import Body17

# TODO update the JSON string below
json = "{}"
# create an instance of Body17 from a JSON string
body17_instance = Body17.from_json(json)
# print the JSON string representation of the object
print(Body17.to_json())

# convert the object into a dict
body17_dict = body17_instance.to_dict()
# create an instance of Body17 from a dict
body17_from_dict = Body17.from_dict(body17_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


