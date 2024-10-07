# RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner

Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item id | [optional] 
**amount** | **str** | Line Item amount | [optional] 
**cost_code** | [**RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerCostCode**](RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerCostCode.md) |  | [optional] 
**created_at** | **datetime** | Created at date and time | [optional] 
**description** | **str** | Line Item description | [optional] 
**extended_amount** | **float** | Line Item extended amount | [optional] 
**extended_type** | **str** | Line Item extended type | [optional] 
**holder** | [**ArrayOfPotentialChangeOrderLineItemsErrorsInnerAllOfHolder**](ArrayOfPotentialChangeOrderLineItemsErrorsInnerAllOfHolder.md) |  | [optional] 
**line_item_type** | [**RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerLineItemType**](RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerLineItemType.md) |  | [optional] 
**origin_id** | **str** | Line Item third party id | [optional] 
**position** | **int** | Line Item position | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**quantity** | **float** | Line Item quantity | [optional] 
**total_amount** | **float** | Line Item total amount | [optional] 
**unit_cost** | **float** | Line Item unit cost | [optional] 
**uom** | **str** | Line Item units of measure | [optional] 
**updated_at** | **datetime** | Updated at date and time | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**currency_configuration** | [**RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerCurrencyConfiguration**](RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner_instance = RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner_dict = rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner from a dict
rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner_from_dict = RestV10ProjectsProjectIdDirectCostsLineItemsGet200ResponseInner.from_dict(rest_v10_projects_project_id_direct_costs_line_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


