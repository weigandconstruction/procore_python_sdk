# Body10


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | The ID of the Project the ToDo belongs to | 
**todo** | [**ToDo**](ToDo.md) |  | 

## Example

```python
from procore_sdk.models.body10 import Body10

# TODO update the JSON string below
json = "{}"
# create an instance of Body10 from a JSON string
body10_instance = Body10.from_json(json)
# print the JSON string representation of the object
print(Body10.to_json())

# convert the object into a dict
body10_dict = body10_instance.to_dict()
# create an instance of Body10 from a dict
body10_from_dict = Body10.from_dict(body10_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


