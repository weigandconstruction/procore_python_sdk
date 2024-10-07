# RestV10ProjectsProjectIdBudgetChangesIdPatchRequest

Budget Change Package information Input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique identifier of this budget change | [optional] 
**number** | **int** | Number field of budget change | [optional] 
**status** | **str** | Status of budget change | [optional] 
**title** | **str** | Title of budget change | [optional] 
**description** | **str** | Description of budget change in HTML format | [optional] 
**adjustment_line_items** | [**List[RestV10ProjectsProjectIdBudgetChangesIdPatchRequestAdjustmentLineItemsInner]**](RestV10ProjectsProjectIdBudgetChangesIdPatchRequestAdjustmentLineItemsInner.md) | List of budget change adjustments | [optional] 
**prostore_file_ids** | **List[int]** | The desired prostore file identifiers that will replace the current collection of attachments associated with the budget change | [optional] 
**production_quantities** | [**List[RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner]**](RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner.md) | List of budget change production quantities | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_id_patch_request import RestV10ProjectsProjectIdBudgetChangesIdPatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdPatchRequest from a JSON string
rest_v10_projects_project_id_budget_changes_id_patch_request_instance = RestV10ProjectsProjectIdBudgetChangesIdPatchRequest.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesIdPatchRequest.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_id_patch_request_dict = rest_v10_projects_project_id_budget_changes_id_patch_request_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdPatchRequest from a dict
rest_v10_projects_project_id_budget_changes_id_patch_request_from_dict = RestV10ProjectsProjectIdBudgetChangesIdPatchRequest.from_dict(rest_v10_projects_project_id_budget_changes_id_patch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


