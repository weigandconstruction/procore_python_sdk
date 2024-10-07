# RestV10SubmittalLogsIdGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**formatted_number** | **str** |  | [optional] 
**revision** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 
**received_date** | **date** |  | [optional] 
**issue_date** | **date** |  | [optional] 
**submit_by** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**type** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**closed** | **bool** |  | [optional] 
**created_by** | [**RestV10SubmittalLogsIdGet200ResponseCreatedBy**](RestV10SubmittalLogsIdGet200ResponseCreatedBy.md) |  | [optional] 
**received_from** | [**RestV10SubmittalLogsIdGet200ResponseReceivedFrom**](RestV10SubmittalLogsIdGet200ResponseReceivedFrom.md) |  | [optional] 
**approvers** | [**List[RestV10SubmittalLogsIdGet200ResponseApproversInner]**](RestV10SubmittalLogsIdGet200ResponseApproversInner.md) |  | [optional] 
**distribution_members** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**ball_in_court** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**specification_section** | [**RestV10SubmittalLogsGet200ResponseInnerSpecificationSection**](RestV10SubmittalLogsGet200ResponseInnerSpecificationSection.md) |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 
**distribution_info** | [**RestV10SubmittalLogsIdGet200ResponseDistributionInfo**](RestV10SubmittalLogsIdGet200ResponseDistributionInfo.md) |  | [optional] 
**submittal_package** | [**RestV10SubmittalLogsIdGet200ResponseSubmittalPackage**](RestV10SubmittalLogsIdGet200ResponseSubmittalPackage.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response import RestV10SubmittalLogsIdGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalLogsIdGet200Response from a JSON string
rest_v10_submittal_logs_id_get200_response_instance = RestV10SubmittalLogsIdGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalLogsIdGet200Response.to_json())

# convert the object into a dict
rest_v10_submittal_logs_id_get200_response_dict = rest_v10_submittal_logs_id_get200_response_instance.to_dict()
# create an instance of RestV10SubmittalLogsIdGet200Response from a dict
rest_v10_submittal_logs_id_get200_response_from_dict = RestV10SubmittalLogsIdGet200Response.from_dict(rest_v10_submittal_logs_id_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


