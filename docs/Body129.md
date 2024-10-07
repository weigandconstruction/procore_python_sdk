# Body129


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model** | [**Body129BimModel**](Body129BimModel.md) |  | 

## Example

```python
from procore_sdk.models.body129 import Body129

# TODO update the JSON string below
json = "{}"
# create an instance of Body129 from a JSON string
body129_instance = Body129.from_json(json)
# print the JSON string representation of the object
print(Body129.to_json())

# convert the object into a dict
body129_dict = body129_instance.to_dict()
# create an instance of Body129 from a dict
body129_from_dict = Body129.from_dict(body129_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


