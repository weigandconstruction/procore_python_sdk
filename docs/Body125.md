# Body125


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**view** | **str** | Specify response schema view | [optional] 
**bim_plan** | [**Body125BimPlan**](Body125BimPlan.md) |  | 

## Example

```python
from procore_sdk.models.body125 import Body125

# TODO update the JSON string below
json = "{}"
# create an instance of Body125 from a JSON string
body125_instance = Body125.from_json(json)
# print the JSON string representation of the object
print(Body125.to_json())

# convert the object into a dict
body125_dict = body125_instance.to_dict()
# create an instance of Body125 from a dict
body125_from_dict = Body125.from_dict(body125_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


