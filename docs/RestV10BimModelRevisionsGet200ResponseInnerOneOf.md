# RestV10BimModelRevisionsGet200ResponseInnerOneOf

Published BIM Model Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_file_id** | **int** | ID of the associated BIM File | [optional] 
**bim_gridline_id** | **int** | ID of the associated Gridline | [optional] 
**bim_model_id** | **int** | ID of the associated BIM Model | [optional] 
**geometry_file_bundle_id** | **int** | ID of the associated geometry file bundle | [optional] 
**suitability** | **str** | Suitability of the revision | [optional] 
**publish_status** | **str** | Status of the revision | [optional] 
**revision** | **int** | The sequential revision count | [optional] 
**publisher_name** | **str** | Name of application publishing the model revision | [optional] 
**publisher_version** | **str** | Version of application publishing the model revision | [optional] 
**min_boundary** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**max_boundary** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**rotation** | [**Body125BimPlanOneOfModelMapStart**](Body125BimPlanOneOfModelMapStart.md) |  | [optional] 
**viewpoints** | [**List[RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner]**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.md) | An array of viewpoints | [optional] 
**created_by** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee**](RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_model_revisions_get200_response_inner_one_of import RestV10BimModelRevisionsGet200ResponseInnerOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelRevisionsGet200ResponseInnerOneOf from a JSON string
rest_v10_bim_model_revisions_get200_response_inner_one_of_instance = RestV10BimModelRevisionsGet200ResponseInnerOneOf.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelRevisionsGet200ResponseInnerOneOf.to_json())

# convert the object into a dict
rest_v10_bim_model_revisions_get200_response_inner_one_of_dict = rest_v10_bim_model_revisions_get200_response_inner_one_of_instance.to_dict()
# create an instance of RestV10BimModelRevisionsGet200ResponseInnerOneOf from a dict
rest_v10_bim_model_revisions_get200_response_inner_one_of_from_dict = RestV10BimModelRevisionsGet200ResponseInnerOneOf.from_dict(rest_v10_bim_model_revisions_get200_response_inner_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


