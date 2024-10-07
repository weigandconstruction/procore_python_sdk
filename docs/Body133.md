# Body133


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model_revision_plan** | [**Body133BimModelRevisionPlan**](Body133BimModelRevisionPlan.md) |  | 

## Example

```python
from procore_sdk.models.body133 import Body133

# TODO update the JSON string below
json = "{}"
# create an instance of Body133 from a JSON string
body133_instance = Body133.from_json(json)
# print the JSON string representation of the object
print(Body133.to_json())

# convert the object into a dict
body133_dict = body133_instance.to_dict()
# create an instance of Body133 from a dict
body133_from_dict = Body133.from_dict(body133_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


