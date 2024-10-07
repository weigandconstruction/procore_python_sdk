# Body138


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_levels** | [**List[Body136BimLevel]**](Body136BimLevel.md) | An array of BIM Level payloads | 

## Example

```python
from procore_sdk.models.body138 import Body138

# TODO update the JSON string below
json = "{}"
# create an instance of Body138 from a JSON string
body138_instance = Body138.from_json(json)
# print the JSON string representation of the object
print(Body138.to_json())

# convert the object into a dict
body138_dict = body138_instance.to_dict()
# create an instance of Body138 from a dict
body138_from_dict = Body138.from_dict(body138_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


