# Body11


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the ToDo belongs to | 
**todo** | [**ToDo2**](ToDo2.md) |  | 

## Example

```python
from procore_sdk.models.body11 import Body11

# TODO update the JSON string below
json = "{}"
# create an instance of Body11 from a JSON string
body11_instance = Body11.from_json(json)
# print the JSON string representation of the object
print(Body11.to_json())

# convert the object into a dict
body11_dict = body11_instance.to_dict()
# create an instance of Body11 from a dict
body11_from_dict = Body11.from_dict(body11_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


