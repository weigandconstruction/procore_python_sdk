# RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner

Budget Modification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**from_budget_line_item_id** | **int** | Source line item id | [optional] 
**notes** | **str** | Notes describing the modification | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**to_budget_line_item_id** | **int** | Target line item id | [optional] 
**transfer_amount** | **float** | Amount transfered from the source Budget Line Item to the Target Budget Line Item | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_modifications_get200_response_inner import RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_budget_modifications_get200_response_inner_instance = RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_modifications_get200_response_inner_dict = rest_v10_projects_project_id_budget_modifications_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner from a dict
rest_v10_projects_project_id_budget_modifications_get200_response_inner_from_dict = RestV10ProjectsProjectIdBudgetModificationsGet200ResponseInner.from_dict(rest_v10_projects_project_id_budget_modifications_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


