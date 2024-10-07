# RestV10ProjectsProjectIdBudgetChangesPostRequest

Budget Change Package information Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | Number field of budget change. If not provided, it will be assigned. | [optional] 
**status** | **str** | Status of budget change | 
**title** | **str** | Title of budget change | [optional] 
**description** | **str** | Description of budget change in HTML format | [optional] 
**adjustment_line_items** | [**List[RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner]**](RestV10ProjectsProjectIdBudgetChangesPostRequestAdjustmentLineItemsInner.md) | List of budget change line items. todo this key be renamed to line_items in the future | [optional] 
**prostore_file_ids** | **List[int]** | The prostore file identifiers that will be associated with this budget change as attachments | [optional] 
**production_quantities** | [**List[RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner]**](RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner.md) | List of budget change production quantities | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post_request import RestV10ProjectsProjectIdBudgetChangesPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequest from a JSON string
rest_v10_projects_project_id_budget_changes_post_request_instance = RestV10ProjectsProjectIdBudgetChangesPostRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPostRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post_request_dict = rest_v10_projects_project_id_budget_changes_post_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequest from a dict
rest_v10_projects_project_id_budget_changes_post_request_from_dict = RestV10ProjectsProjectIdBudgetChangesPostRequest.from_dict(rest_v10_projects_project_id_budget_changes_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


