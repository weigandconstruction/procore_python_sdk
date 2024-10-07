# Body3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**line_item** | [**LineItem**](LineItem.md) |  | 

## Example

```python
from procore_sdk.models.body3 import Body3

# TODO update the JSON string below
json = "{}"
# create an instance of Body3 from a JSON string
body3_instance = Body3.from_json(json)
# print the JSON string representation of the object
print(Body3.to_json())

# convert the object into a dict
body3_dict = body3_instance.to_dict()
# create an instance of Body3 from a dict
body3_from_dict = Body3.from_dict(body3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


