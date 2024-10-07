# Body131


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model_revision** | [**Body131BimModelRevision**](Body131BimModelRevision.md) |  | 

## Example

```python
from procore_sdk.models.body131 import Body131

# TODO update the JSON string below
json = "{}"
# create an instance of Body131 from a JSON string
body131_instance = Body131.from_json(json)
# print the JSON string representation of the object
print(Body131.to_json())

# convert the object into a dict
body131_dict = body131_instance.to_dict()
# create an instance of Body131 from a dict
body131_from_dict = Body131.from_dict(body131_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


