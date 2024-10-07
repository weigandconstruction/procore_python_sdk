# RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision

Published BIM Model Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**bim_file** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile**](RestV10CoordinationIssuesGet200ResponseInnerAllOfCoordinationIssueFile.md) |  | [optional] 
**bim_model_id** | **int** | ID of the associated BIM Model | [optional] 
**geometry_file_bundle_id** | **int** | ID of the associated geometry file bundle | [optional] 
**suitability** | **str** | Suitability of the revision | [optional] 
**publish_status** | **str** | Status of the revision | [optional] 
**revision** | **int** | The sequential revision count | [optional] 
**publisher_name** | **str** | Name of application publishing the model revision | [optional] 
**publisher_version** | **str** | Version of application publishing the model revision | [optional] 
**min_boundary** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | [optional] 
**max_boundary** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | [optional] 
**rotation** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionMinBoundary.md) |  | [optional] 
**viewpoints** | [**List[RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner]**](RestV10CoordinationIssuesGet200ResponseInnerAllOfViewpointsInner.md) | An array of viewpoints | [optional] 
**created_by** | [**RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee**](RestV10CoordinationIssuesGet200ResponseInnerAllOfAssignee.md) |  | [optional] 
**created_at** | **datetime** | Created date | [optional] 
**updated_at** | **datetime** | Updated date | [optional] 
**bim_gridline** | [**RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline**](RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevisionBimGridline.md) |  | [optional] 
**published_model** | [**RestV10ScheduleIntegrationGet200ResponseInnerFile**](RestV10ScheduleIntegrationGet200ResponseInnerFile.md) |  | [optional] 
**object_definition** | [**RestV10ScheduleIntegrationGet200ResponseInnerFile**](RestV10ScheduleIntegrationGet200ResponseInnerFile.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_bim_models_get200_response_inner_one_of1_current_revision import RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision from a JSON string
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_instance = RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision.from_json(json)
# print the JSON string representation of the object
print(RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision.to_json())

# convert the object into a dict
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_dict = rest_v10_bim_models_get200_response_inner_one_of1_current_revision_instance.to_dict()
# create an instance of RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision from a dict
rest_v10_bim_models_get200_response_inner_one_of1_current_revision_from_dict = RestV10BimModelsGet200ResponseInnerOneOf1CurrentRevision.from_dict(rest_v10_bim_models_get200_response_inner_one_of1_current_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


