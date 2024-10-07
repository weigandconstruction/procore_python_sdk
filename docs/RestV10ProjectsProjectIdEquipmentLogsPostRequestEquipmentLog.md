# RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of record. Format: YYYY-MM-DD | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**hours_idle** | **int** | Number of hours the Equipment was idle | [optional] 
**hours_operating** | **int** | Number of hours the Equipment was in operation | [optional] 
**inspected** | **bool** | Inspection status of Equipment before operation | [optional] 
**inspection_hour** | **int** | Time of inspection - hour | 
**inspection_minute** | **int** | Time of inspection - minute | 
**notes** | **str** | Notes | [optional] 
**location_id** | **int** | The ID of the Location of the Inspection Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**equipment_id** | **int** | Equipment ID | [optional] 
**equipment_name** | **str** | Equipment name. This Equipment will create on the fly if it doesn&#39;t exist and will take precedence over Equipment ID. | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_equipment_logs_post_request_equipment_log import RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog from a JSON string
rest_v10_projects_project_id_equipment_logs_post_request_equipment_log_instance = RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_equipment_logs_post_request_equipment_log_dict = rest_v10_projects_project_id_equipment_logs_post_request_equipment_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog from a dict
rest_v10_projects_project_id_equipment_logs_post_request_equipment_log_from_dict = RestV10ProjectsProjectIdEquipmentLogsPostRequestEquipmentLog.from_dict(rest_v10_projects_project_id_equipment_logs_post_request_equipment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


