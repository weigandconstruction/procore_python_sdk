# Body14


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | ID of the project this task belongs to. | 
**task** | [**Task1**](Task1.md) |  | 

## Example

```python
from procore_sdk.models.body14 import Body14

# TODO update the JSON string below
json = "{}"
# create an instance of Body14 from a JSON string
body14_instance = Body14.from_json(json)
# print the JSON string representation of the object
print(Body14.to_json())

# convert the object into a dict
body14_dict = body14_instance.to_dict()
# create an instance of Body14 from a dict
body14_from_dict = Body14.from_dict(body14_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


