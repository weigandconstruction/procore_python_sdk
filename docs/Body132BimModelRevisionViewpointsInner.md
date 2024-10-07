# Body132BimModelRevisionViewpointsInner

BIM Model Revision Viewpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bim_model_revision_id** | **int** | BIM Model Revision ID | 
**bim_viewpoint_id** | **int** | BIM Viewpoint ID. The BIM Viewpoint should be associated to the same BIM File as the BIM Model Revision | 
**primary** | **bool** | Flag to indicate whether this is primary viewpoint for the model revision. There can only be one primary viewpoint per model revision | [optional] 

## Example

```python
from procore_sdk.models.body132_bim_model_revision_viewpoints_inner import Body132BimModelRevisionViewpointsInner

# TODO update the JSON string below
json = "{}"
# create an instance of Body132BimModelRevisionViewpointsInner from a JSON string
body132_bim_model_revision_viewpoints_inner_instance = Body132BimModelRevisionViewpointsInner.from_json(json)
# print the JSON string representation of the object
print(Body132BimModelRevisionViewpointsInner.to_json())

# convert the object into a dict
body132_bim_model_revision_viewpoints_inner_dict = body132_bim_model_revision_viewpoints_inner_instance.to_dict()
# create an instance of Body132BimModelRevisionViewpointsInner from a dict
body132_bim_model_revision_viewpoints_inner_from_dict = Body132BimModelRevisionViewpointsInner.from_dict(body132_bim_model_revision_viewpoints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


