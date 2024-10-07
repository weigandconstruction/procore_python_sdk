# RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Date of record. Mutually exclusive with the datetime property. | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**notes** | **str** | Notes | [optional] 
**num_workers** | **int** | Number of workers | [optional] 
**num_hours** | **str** | Number of hours for each worker | [optional] 
**contact_id** | **int** | ID of the Vendor that is performing work | [optional] 
**user_id** | **int** | ID of the user that is performing work. Use this instead of contact_id when tracking hours for a specific user. | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**location_id** | **int** | The ID of the Location of the Manpower Log. &#x60;location_id&#x60; takes precedence over &#x60;mt_location&#x60; | [optional] 
**trade_id** | **int** | ID of the Trade associated to the Manpower Log | [optional] 
**mt_location** | **List[str]** | Use this for creating a new multi-tier or single-tier Location. This will be ignored if &#x60;location_id&#x60; is provided. | [optional] 
**custom_field_custom_field_definition_id** | [**WorkOrderContractCustomFieldCustomFieldDefinitionId**](WorkOrderContractCustomFieldCustomFieldDefinitionId.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_manpower_logs_post_request_manpower_log import RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog from a JSON string
rest_v10_projects_project_id_manpower_logs_post_request_manpower_log_instance = RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_manpower_logs_post_request_manpower_log_dict = rest_v10_projects_project_id_manpower_logs_post_request_manpower_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog from a dict
rest_v10_projects_project_id_manpower_logs_post_request_manpower_log_from_dict = RestV10ProjectsProjectIdManpowerLogsPostRequestManpowerLog.from_dict(rest_v10_projects_project_id_manpower_logs_post_request_manpower_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


