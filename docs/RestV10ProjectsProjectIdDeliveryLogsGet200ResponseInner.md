# RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**comments** | **str** | Additional comments | [optional] 
**contents** | **str** | Contents of the delivery | [optional] 
**var_date** | **date** | Date of delivery | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**delivery_from** | **str** | Name of the Company that delivered the items | [optional] 
**position** | **int** | Position in the list of recorded deliveries for the day | [optional] 
**status** | **str** | Is a log pending or approved | [optional] 
**time_hour** | **int** | Time of delivery - hour | [optional] 
**time_minute** | **int** | Time of delivery - minute | [optional] 
**tracking_number** | **str** | Tracking number for the delivery | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 
**attachments** | [**List[RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner]**](RestV10CompaniesCompanyIdWorkflowPermanentLogsGet200ResponseInnerAttachmentsInner.md) | :filename to be deprecated, use :name | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_delivery_logs_get200_response_inner import RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_delivery_logs_get200_response_inner_instance = RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_delivery_logs_get200_response_inner_dict = rest_v10_projects_project_id_delivery_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_delivery_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdDeliveryLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_delivery_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


