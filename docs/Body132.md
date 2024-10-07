# Body132


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** | Unique identifier for the project. | 
**bim_model_revision_viewpoints** | [**List[Body132BimModelRevisionViewpointsInner]**](Body132BimModelRevisionViewpointsInner.md) | An array of BIM Model Revision Viewpoint payloads | 

## Example

```python
from procore_sdk.models.body132 import Body132

# TODO update the JSON string below
json = "{}"
# create an instance of Body132 from a JSON string
body132_instance = Body132.from_json(json)
# print the JSON string representation of the object
print(Body132.to_json())

# convert the object into a dict
body132_dict = body132_instance.to_dict()
# create an instance of Body132 from a dict
body132_from_dict = Body132.from_dict(body132_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


