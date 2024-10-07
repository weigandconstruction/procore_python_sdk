# RestV10SubmittalLogsIdGet200ResponseSubmittalPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**description** | **str** |  | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_submittal_logs_id_get200_response_submittal_package import RestV10SubmittalLogsIdGet200ResponseSubmittalPackage

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10SubmittalLogsIdGet200ResponseSubmittalPackage from a JSON string
rest_v10_submittal_logs_id_get200_response_submittal_package_instance = RestV10SubmittalLogsIdGet200ResponseSubmittalPackage.from_json(json)
# print the JSON string representation of the object
print(RestV10SubmittalLogsIdGet200ResponseSubmittalPackage.to_json())

# convert the object into a dict
rest_v10_submittal_logs_id_get200_response_submittal_package_dict = rest_v10_submittal_logs_id_get200_response_submittal_package_instance.to_dict()
# create an instance of RestV10SubmittalLogsIdGet200ResponseSubmittalPackage from a dict
rest_v10_submittal_logs_id_get200_response_submittal_package_from_dict = RestV10SubmittalLogsIdGet200ResponseSubmittalPackage.from_dict(rest_v10_submittal_logs_id_get200_response_submittal_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


