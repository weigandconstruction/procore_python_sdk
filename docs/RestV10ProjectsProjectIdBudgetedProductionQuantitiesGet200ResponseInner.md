# RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner

Budgeted Production Quantity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**unit_of_measure** | **str** | The measuerment of the install production quantity | [optional] 
**project_id** | **int** | The Project ID the Budgeted Production Quantity was created with | [optional] 
**wbs_code_id** | **int** | The Production Quantity Code for the Budgeted Production Quantity. | [optional] 
**cost_code** | [**RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode**](RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInnerCostCode.md) |  | [optional] 
**quantity** | **float** | Amount of cost code budgeted to be installed | [optional] 
**updated_at** | **datetime** | Date the actual production quantity was updated | [optional] 
**created_at** | **datetime** | Date the actual production quantity was created | [optional] 
**created_by** | [**ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee**](ArrayOfTaskItemsThatWereSentOutInnerAllOfAssignee.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner import RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner from a JSON string
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_instance = RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_dict = rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner from a dict
rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_from_dict = RestV10ProjectsProjectIdBudgetedProductionQuantitiesGet200ResponseInner.from_dict(rest_v10_projects_project_id_budgeted_production_quantities_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


