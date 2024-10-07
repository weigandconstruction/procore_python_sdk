# RestV10SubmittalLogsIdGet200ResponseDistributionInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**distributed_date** | **datetime** |  | [optional] 
**distributed_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**distributed_to** | [**List[RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy]**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**final_attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_distribution_info import RestV10SubmittalLogsIdGet200ResponseDistributionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalLogsIdGet200ResponseDistributionInfo from a JSON string
rest_v10_submittal_logs_id_get200_response_distribution_info_instance = RestV10SubmittalLogsIdGet200ResponseDistributionInfo.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalLogsIdGet200ResponseDistributionInfo.to_json())

# convert the object into a dict
rest_v10_submittal_logs_id_get200_response_distribution_info_dict = rest_v10_submittal_logs_id_get200_response_distribution_info_instance.to_dict()
# create an instance of RestV10SubmittalLogsIdGet200ResponseDistributionInfo from a dict
rest_v10_submittal_logs_id_get200_response_distribution_info_from_dict = RestV10SubmittalLogsIdGet200ResponseDistributionInfo.from_dict(rest_v10_submittal_logs_id_get200_response_distribution_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


