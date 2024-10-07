# RestV10SubmittalLogsIdGet200ResponseApproversInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_information** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**id** | **int** |  | [optional] 
**response** | **str** |  | [optional] 
**sent_date** | **date** |  | [optional] 
**returned_date** | **date** |  | [optional] 
**due_date** | **date** |  | [optional] 
**comment** | **str** |  | [optional] 
**distributed** | **List[int]** |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_approvers_inner import RestV10SubmittalLogsIdGet200ResponseApproversInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalLogsIdGet200ResponseApproversInner from a JSON string
rest_v10_submittal_logs_id_get200_response_approvers_inner_instance = RestV10SubmittalLogsIdGet200ResponseApproversInner.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalLogsIdGet200ResponseApproversInner.to_json())

# convert the object into a dict
rest_v10_submittal_logs_id_get200_response_approvers_inner_dict = rest_v10_submittal_logs_id_get200_response_approvers_inner_instance.to_dict()
# create an instance of RestV10SubmittalLogsIdGet200ResponseApproversInner from a dict
rest_v10_submittal_logs_id_get200_response_approvers_inner_from_dict = RestV10SubmittalLogsIdGet200ResponseApproversInner.from_dict(rest_v10_submittal_logs_id_get200_response_approvers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


