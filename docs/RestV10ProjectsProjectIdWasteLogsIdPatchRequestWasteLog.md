# RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**approximate_quantity** | **int** | Waste log approximate quantity | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**description** | **str** | Description | [optional] 
**disposal_location** | **str** | Waste disposal location | [optional] 
**material** | **str** | Type of waste disposed of | [optional] 
**method_of_disposal** | **str** | Method used to dispose of the waste | [optional] 
**time_hour** | **int** | Time of waste disposal - hour | [optional] 
**time_minute** | **int** | Time of waste disposal - minute | [optional] 
**vendor_id** | **int** | ID of the Vendor who disposed of the waste | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log import RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog from a JSON string
rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log_instance = RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log_dict = rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog from a dict
rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log_from_dict = RestV10ProjectsProjectIdWasteLogsIdPatchRequestWasteLog.from_dict(rest_v10_projects_project_id_waste_logs_id_patch_request_waste_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


