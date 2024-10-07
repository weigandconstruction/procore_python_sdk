# Body136


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_level** | [**Body136BimLevel**](Body136BimLevel.md) |  | 

## Example

```python
from procore_sdk.models.body136 import Body136

# TODO update the JSON string below
json = "{}"
# create an instance of Body136 from a JSON string
body136_instance = Body136.from_json(json)
# print the JSON string representation of the object
print(Body136.to_json())

# convert the object into a dict
body136_dict = body136_instance.to_dict()
# create an instance of Body136 from a dict
body136_from_dict = Body136.from_dict(body136_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


