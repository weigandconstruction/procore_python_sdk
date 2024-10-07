# Body123


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**procore_item** | [**ProcoreItemDetails1**](ProcoreItemDetails1.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body123 import Body123

# TODO update the JSON string below
json = "{}"
# create an instance of Body123 from a JSON string
body123_instance = Body123.from_json(json)
# print the JSON string representation of the object
print(Body123.to_json())

# convert the object into a dict
body123_dict = body123_instance.to_dict()
# create an instance of Body123 from a dict
body123_from_dict = Body123.from_dict(body123_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


