# RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | All supplies were delivered on time | [optional] 
**contents** | **str** | Contents of the delivery | [optional] 
**var_date** | **date** | Format: YYYY-MM-DD Example: 2016-04-19 | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**delivery_from** | **str** | Company that deliveried the items | [optional] 
**time_hour** | **int** | Delivery Time - hour | [optional] 
**time_minute** | **int** | Delivery Time - minute | [optional] 
**tracking_number** | **str** | Delivery tracking number | [optional] 
**status** | **str** | Approval for pending logs | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log import RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog from a JSON string
rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log_instance = RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log_dict = rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog from a dict
rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log_from_dict = RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog.from_dict(rest_v10_projects_project_id_delivery_logs_id_patch_request_delivery_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


