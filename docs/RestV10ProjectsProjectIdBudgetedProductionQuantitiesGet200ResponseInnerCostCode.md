# RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Cost Code ID | [optional] 
**biller_id** | **int** | Biller ID | [optional] 
**biller_type** | **str** | Biller type | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**deleted_at** | **datetime** | Deleted at | [optional] 
**full_code** | **str** | Full Cost code, including parent prefixes | [optional] 
**name** | **str** | Name | [optional] 
**parent_id** | **int** | Parent | [optional] 
**sortable_code** | **str** | Sortable code (this property is deprecated - see full_code) | [optional] 
**standard_cost_code_id** | **int** | Standard Cost Code ID | [optional] 
**updated_at** | **datetime** | Updated at | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode from a JSON string
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code_instance = RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code_dict = rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode from a dict
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code_from_dict = RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode.from_dict(rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_cost_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


