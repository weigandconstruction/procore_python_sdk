# RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner

Budget Change Adjustment Production Quantity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** | ID of this production quantity | [optional] 
**budget_change_id** | **float** | ID of the Budget Change to which this production quantity is associated | [optional] 
**comment** | **str** | Comment of the production quantity | [optional] 
**description** | **str** | Description of the production quantity | [optional] 
**quantity** | **float** | Estimated cost quantity | [optional] 
**ref** | **str** | Identifier used to map production quantities in the request to their respective objects or errors in the response | [optional] 
**uom** | **str** | Unit of measure used | [optional] 
**wbs_code** | [**RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerWbsCode**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerWbsCode.md) |  | [optional] 
**cost_code** | [**RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerCostCode**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerCostCode.md) |  | [optional] 
**sub_job** | [**RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerSubJob**](RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInnerSubJob.md) |  | [optional] 
**change_event_production_quantity_id** | **float** | ID of the associated Change Event Production Quantity | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner import RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner from a JSON string
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner_instance = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner_dict = rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner from a dict
rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner_from_dict = RestV10ProjectsProjectIdBudgetChangesPost201ResponseDataAllOfProductionQuantitiesInner.from_dict(rest_v10_projects_project_id_budget_changes_post201_response_data_all_of_production_quantities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


