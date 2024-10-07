# RestV10BimModelRevisionViewpointsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_model_revision_id** | **int** | ID of associated published BIM Model Revision | [optional] 
**bim_viewpoint_id** | **int** | ID of associated BIM Viewpoint | [optional] 
**primary** | **bool** | Indicates whether primary viewpoint | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_viewpoint** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revision_viewpoints_get200_response_inner import RestV10BimModelRevisionViewpointsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionViewpointsGet200ResponseInner from a JSON string
rest_v10_bim_model_revision_viewpoints_get200_response_inner_instance = RestV10BimModelRevisionViewpointsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionViewpointsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_bim_model_revision_viewpoints_get200_response_inner_dict = rest_v10_bim_model_revision_viewpoints_get200_response_inner_instance.to_dict()
# create an instance of RestV10BimModelRevisionViewpointsGet200ResponseInner from a dict
rest_v10_bim_model_revision_viewpoints_get200_response_inner_from_dict = RestV10BimModelRevisionViewpointsGet200ResponseInner.from_dict(rest_v10_bim_model_revision_viewpoints_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


