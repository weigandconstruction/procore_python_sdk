# Body108


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**procore_item** | [**ProcoreItemDetails**](ProcoreItemDetails.md) |  | [optional] 

## Example

```python
from procore_sdk.models.body108 import Body108

# TODO update the JSON string below
json = "{}"
# create an instance of Body108 from a JSON string
body108_instance = Body108.from_json(json)
# print the JSON string representation of the object
print(Body108.to_json())

# convert the object into a dict
body108_dict = body108_instance.to_dict()
# create an instance of Body108 from a dict
body108_from_dict = Body108.from_dict(body108_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


