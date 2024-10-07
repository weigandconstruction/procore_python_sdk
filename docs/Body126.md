# Body126


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_plan** | [**Body126BimPlan**](Body126BimPlan.md) |  | 

## Example

```python
from procore_sdk.models.body126 import Body126

# TODO update the JSON string below
json = "{}"
# create an instance of Body126 from a JSON string
body126_instance = Body126.from_json(json)
# print the JSON string representation of the object
print(Body126.to_json())

# convert the object into a dict
body126_dict = body126_instance.to_dict()
# create an instance of Body126 from a dict
body126_from_dict = Body126.from_dict(body126_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


