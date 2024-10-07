# RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner

Budget Change Adjustment Production Quantity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of this Production Quantity | [optional] 
**comment** | **str** | Comment of the adjustment | [optional] 
**cost_code_id** | **int** | Cost Code ID | 
**description** | **str** | Description of the Production Quantity | [optional] 
**quantity** | **float** | Estimated cost quantity | 
**ref** | **str** | Identifier used to map production quantities in the request to their respective objects or errors in the response | [optional] 
**uom** | **str** | Unit of measure used | 
**change_event_production_quantity_id** | **float** | ID of the Change Event Production Quantity that is to be associated with the Budget Change Production Quantity | [optional] 
**delete** | **bool** | Whether this production quantity should be deleted | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner import RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner from a JSON string
rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner_instance = RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner_dict = rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner from a dict
rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesIdPatchRequestProductionQuantitiesInner.from_dict(rest_v10_projects_project_id_budget_changes_id_patch_request_production_quantities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


