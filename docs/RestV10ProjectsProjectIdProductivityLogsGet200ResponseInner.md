# RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company** | **str** | Name of Company | [optional] 
**contract** | **str** | Approved Commitment Contract title | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Date of record | [optional] 
**datetime** | **datetime** | Estimated UTC datetime of record | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**line_item_id** | **int** | ID of the Line Item from the approved Commitment Contract | [optional] 
**line_item_description** | **str** | Description of the Line Item | [optional] 
**line_item_holder** | [**RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder**](RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder.md) |  | [optional] 
**notes** | **str** | Additional notes | [optional] 
**position** | **int** | Order in which this entry was recorded | [optional] 
**previously_delivered** | **str** | Number of materials that were previously delivered on site | [optional] 
**previously_used** | **str** | Number of materials previously put in place on site | [optional] 
**quantity_delivered** | **str** | Number of materials delivered on site | [optional] 
**quantity_used** | **str** | Number of materials put in place on site | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 
**created_by** | [**RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy**](RestV10ProjectsProjectIdWorkLogsGet200ResponseInnerCreatedBy.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_productivity_logs_get200_response_inner_instance = RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_productivity_logs_get200_response_inner_dict = rest_v10_projects_project_id_productivity_logs_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner from a dict
rest_v10_projects_project_id_productivity_logs_get200_response_inner_from_dict = RestV10ProjectsProjectIdProductivityLogsGet200ResponseInner.from_dict(rest_v10_projects_project_id_productivity_logs_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


