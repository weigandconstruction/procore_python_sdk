# RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner

Line Item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item id | [optional] 
**amount** | **str** | Line Item amount | [optional] 
**company** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCompany.md) |  | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**created_at** | **datetime** | Created at date and time | [optional] 
**description** | **str** | Line Item description | [optional] 
**extended_type** | **str** | Line Item extended type | [optional] 
**holder** | [**ArrayOfPotentialChangeOrderLineItemsErrorsInnerAllOfHolder**](ArrayOfPotentialChangeOrderLineItemsErrorsInnerAllOfHolder.md) |  | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**origin_data** | **str** | Line Item third party data | [optional] 
**origin_id** | **str** | Line Item third party id | [optional] 
**position** | **int** | Line Item position | [optional] 
**project** | [**RestV10WorkOrderContractsGet200ResponseInnerProject**](RestV10WorkOrderContractsGet200ResponseInnerProject.md) |  | [optional] 
**quantity** | **float** | Line Item quantity | [optional] 
**tax_code_id** | **int** | Tax Code ID | [optional] 
**total_amount** | **float** | Line Item total amount | [optional] 
**extended_amount** | **float** | Line Item extended amount | [optional] 
**unit_cost** | **float** | Line Item unit cost | [optional] 
**uom** | **str** | Line Item units of measure | [optional] 
**updated_at** | **datetime** | Updated at date and time | [optional] 
**change_event_line_item** | [**RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem**](RestV10WorkOrderContractsWorkOrderContractIdLineItemsSyncPatch200ResponseEntitiesInnerChangeEventLineItem.md) |  | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**currency_configuration** | [**RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInnerCurrencyConfiguration**](RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner import RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner from a JSON string
rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner_instance = RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner_dict = rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner_instance.to_dict()
# create an instance of RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner from a dict
rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner_from_dict = RestV10ProjectsProjectIdDirectCostsDirectCostIdLineItemsGet200ResponseInner.from_dict(rest_v10_projects_project_id_direct_costs_direct_cost_id_line_items_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


