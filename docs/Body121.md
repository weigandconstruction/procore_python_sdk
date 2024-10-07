# Body121


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_viewpoint** | [**Body121BimViewpoint**](Body121BimViewpoint.md) |  | 

## Example

```python
from procore_sdk.models.body121 import Body121

# TODO update the JSON string below
json = "{}"
# create an instance of Body121 from a JSON string
body121_instance = Body121.from_json(json)
# print the JSON string representation of the object
print(Body121.to_json())

# convert the object into a dict
body121_dict = body121_instance.to_dict()
# create an instance of Body121 from a dict
body121_from_dict = Body121.from_dict(body121_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


