# RestV10SubmittalLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**title** | **str** |  | [optional] 
**number** | **str** |  | 
**revision** | **str** |  | [optional] 
**due_date** | **date** |  | [optional] 
**attachment_count** | **int** |  | [optional] 
**status** | **str** |  | 
**closed** | **bool** |  | [optional] 
**specification_section** | [**RestV10SubmittalLogsGet200ResponseInnerSpecificationSection**](RestV10SubmittalLogsGet200ResponseInnerSpecificationSection.md) |  | [optional] 
**package** | [**RestV10SubmittalLogsGet200ResponseInnerPackage**](RestV10SubmittalLogsGet200ResponseInnerPackage.md) |  | [optional] 
**ball_in_court** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**responses** | [**List[RestV10SubmittalLogsGet200ResponseInnerResponsesInner]**](RestV10SubmittalLogsGet200ResponseInnerResponsesInner.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_logs_get200_response_inner import RestV10SubmittalLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalLogsGet200ResponseInner from a JSON string
rest_v10_submittal_logs_get200_response_inner_instance = RestV10SubmittalLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_submittal_logs_get200_response_inner_dict = rest_v10_submittal_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10SubmittalLogsGet200ResponseInner from a dict
rest_v10_submittal_logs_get200_response_inner_from_dict = RestV10SubmittalLogsGet200ResponseInner.from_dict(rest_v10_submittal_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


