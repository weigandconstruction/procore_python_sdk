# RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** | Additional comments | [optional] 
**contents** | **str** | Contents of the delivery | [optional] 
**var_date** | **date** | (ie. &#39;2016-04-19&#39;) | [optional] 
**datetime** | **datetime** | Datetime of record. Mutually exclusive with the date property. | [optional] 
**delivery_from** | **str** | Name of the Company that delivered the items | [optional] 
**time_hour** | **int** | Time of delivery - hour | 
**time_minute** | **int** | Time of delivery - minute | 
**tracking_number** | **str** | Tracking number for the delivery | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delivery_logs_post_request_delivery_log import RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog from a JSON string
rest_v10_projects_project_id_delivery_logs_post_request_delivery_log_instance = RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delivery_logs_post_request_delivery_log_dict = rest_v10_projects_project_id_delivery_logs_post_request_delivery_log_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog from a dict
rest_v10_projects_project_id_delivery_logs_post_request_delivery_log_from_dict = RestV10ProjectsProjectIdDeliveryLogsPostRequestDeliveryLog.from_dict(rest_v10_projects_project_id_delivery_logs_post_request_delivery_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


