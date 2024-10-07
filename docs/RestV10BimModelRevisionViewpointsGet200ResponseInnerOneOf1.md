# RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1

BIM Model Revision Viewpoint associates BIM Model Revisions to BIM Viewpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_model_revision_id** | **int** | ID of associated published BIM Model Revision | [optional] 
**bim_viewpoint** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.md) |  | [optional] 
**primary** | **bool** | Indicates whether primary viewpoint | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1 import RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1 from a JSON string
rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1_instance = RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1.to_json())

# convert the object into a dict
rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1_dict = rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1_instance.to_dict()
# create an instance of RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1 from a dict
rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1_from_dict = RestV10BimModelRevisionViewpointsGet200ResponseInnerOneOf1.from_dict(rest_v10_bim_model_revision_viewpoints_get200_response_inner_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


