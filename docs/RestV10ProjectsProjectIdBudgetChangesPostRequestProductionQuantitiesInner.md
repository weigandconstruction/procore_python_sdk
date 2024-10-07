# RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner

Budget Change Adjustment Production Quantity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment of the production quantity | [optional] 
**cost_code_id** | **int** | Cost Code ID | 
**description** | **str** | Description of the production quantity | [optional] 
**quantity** | **float** | Estimated cost quantity | 
**ref** | **str** | Identifier used to map production quantities in the request to their respective objects or errors in the response | [optional] 
**uom** | **str** | Unit of measure used | 
**change_event_production_quantity_id** | **float** | ID of the Change Event Production Quantity that is to be associated with the Budget Change Production Quantity | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner import RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner from a JSON string
rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner_instance = RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner_dict = rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner from a dict
rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesPostRequestProductionQuantitiesInner.from_dict(rest_v10_projects_project_id_budget_changes_post_request_production_quantities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


