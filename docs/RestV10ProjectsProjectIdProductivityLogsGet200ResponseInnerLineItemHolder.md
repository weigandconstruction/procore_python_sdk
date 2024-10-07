# RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder

Object that the Line Item belongs to (WorkOrderContract, PurchaseOrderContract, PotentialChangeOrder)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**title** | **str** | Title | [optional] 
**number** | **str** | Number | [optional] 
**type** | **str** | The type of object that the Line Item belongs to | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder import RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder from a JSON string
rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder_instance = RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder.to_json())

# convert the object into a dict
rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder_dict = rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder from a dict
rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder_from_dict = RestV10ProjectsProjectIdProductivityLogsGet200ResponseInnerLineItemHolder.from_dict(rest_v10_projects_project_id_productivity_logs_get200_response_inner_line_item_holder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


