# RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response

Time and Material Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**project_id** | **int** | ID of the project the T&amp;M ticket was logged for | [optional] 
**company_id** | **int** | ID of the company the T&amp;M ticket was logged for | [optional] 
**creation** | **List[int]** |  | [optional] 
**customer_signed** | **List[int]** |  | [optional] 
**company_signed** | **List[int]** |  | [optional] 
**closed** | **List[int]** |  | [optional] 
**group_equipment_totals_by** | **str** | Grouping configurations for T&amp;M Equipment push to Change Management | [optional] 
**group_labor_totals_by** | **str** | Grouping configurations for T&amp;M Labor push to Change Management | [optional] 
**notify_dl_on_customer_signed** | **bool** |  | [optional] 
**notify_dl_on_company_signed** | **bool** |  | [optional] 
**notify_dl_on_creation** | **bool** |  | [optional] 
**notify_dl_on_closed** | **bool** |  | [optional] 
**updated_at** | **datetime** | Date the T&amp;M ticket was updated | [optional] 
**created_at** | **datetime** | Date the T&amp;M ticket was created | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_time_and_material_notifications_get200_response import RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response from a JSON string
rest_v10_projects_project_id_time_and_material_notifications_get200_response_instance = RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.to_json())

# convert the object into a dict
rest_v10_projects_project_id_time_and_material_notifications_get200_response_dict = rest_v10_projects_project_id_time_and_material_notifications_get200_response_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response from a dict
rest_v10_projects_project_id_time_and_material_notifications_get200_response_from_dict = RestV10ProjectsProjectIdTimeAndMaterialNotificationsGet200Response.from_dict(rest_v10_projects_project_id_time_and_material_notifications_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


