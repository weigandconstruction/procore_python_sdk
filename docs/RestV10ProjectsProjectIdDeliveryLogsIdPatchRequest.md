# RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_log** | [**RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog**](RestV10ProjectsProjectIdDeliveryLogsIdPatchRequestDeliveryLog.md) |  | 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delivery_logs_id_patch_request import RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest from a JSON string
rest_v10_projects_project_id_delivery_logs_id_patch_request_instance = RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delivery_logs_id_patch_request_dict = rest_v10_projects_project_id_delivery_logs_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest from a dict
rest_v10_projects_project_id_delivery_logs_id_patch_request_from_dict = RestV10ProjectsProjectIdDeliveryLogsIdPatchRequest.from_dict(rest_v10_projects_project_id_delivery_logs_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


