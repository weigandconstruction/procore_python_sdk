# Body98


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**sub_job_id** | **int** | Unique identifier for the Sub Job | [optional] 
**cost_code** | [**CostCode1**](CostCode1.md) |  | 

## Example

```python
from procore_sdk.models.body98 import Body98

# TODO update the JSON string below
json = "{}"
# create an instance of Body98 from a JSON string
body98_instance = Body98.from_json(json)
# print the JSON string representation of the object
print(Body98.to_json())

# convert the object into a dict
body98_dict = body98_instance.to_dict()
# create an instance of Body98 from a dict
body98_from_dict = Body98.from_dict(body98_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


