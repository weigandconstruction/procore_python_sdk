# Body130


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model_revision** | [**Body130BimModelRevision**](Body130BimModelRevision.md) |  | 

## Example

```python
from procore_sdk.models.body130 import Body130

# TODO update the JSON string below
json = "{}"
# create an instance of Body130 from a JSON string
body130_instance = Body130.from_json(json)
# print the JSON string representation of the object
print(Body130.to_json())

# convert the object into a dict
body130_dict = body130_instance.to_dict()
# create an instance of Body130 from a dict
body130_from_dict = Body130.from_dict(body130_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


