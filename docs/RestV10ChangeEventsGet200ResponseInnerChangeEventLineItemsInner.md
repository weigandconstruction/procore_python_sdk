# RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**budget_code** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetCode.md) |  | [optional] 
**cost_code_biller_name** | **str** | Cost Code Biller name | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**cost_code_is_budgeted** | **bool** | Cost Code is budgeted | [optional] 
**description** | **str** | Description | [optional] 
**event_id** | **int** | Change Event ID | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**rom** | **int** | Rough order of magnitude (ROM) | [optional] 
**contract** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerContract.md) |  | [optional] 
**links** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerLinks.md) |  | [optional] 
**statuses** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerStatuses.md) |  | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**biller** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBiller**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBiller.md) |  | [optional] 
**proposed_vendor_id** | **int** | Proposed Vendor ID | [optional] 
**proposed_contract_id** | **int** | Proposed Contract ID | [optional] 
**uom** | **str** | Unit of Measure | [optional] 
**estimated_cost_amount** | **str** | Estimated Cost Amount | [optional] 
**estimated_cost_quantity** | **float** | Estimated Cost Quantity | [optional] 
**estimated_cost_unit_cost** | **float** | Estimated Cost Unit Cost | [optional] 
**estimated_cost_calculation_strategy** | **str** | Estimated Cost Calculation Strategy controls whether estimated_cost_amount is calculated by multiplying the quantity and unit_cost attributes or set manually to a provided value. | [optional] 
**line_item_type_id** | **int** | Line Item Type ID | [optional] 
**cost_code_id** | **int** | Cost Code ID | [optional] 
**editable** | **bool** | Editable status | [optional] 
**deletable** | **bool** | Deletable status | [optional] 
**request_for_quote_id** | **int** | Request For Quote ID | [optional] 
**biller_guid** | **str** | Biller GUID | [optional] 
**commitment_contract_cost** | **str** | Commitment Contract Cost | [optional] 
**commitment_pco_cost** | **str** | Commitment PCO Cost | [optional] 
**budget_mod_amount** | **str** | Budget Modification Amount | [optional] 
**budget_mod** | [**RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod**](RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInnerBudgetMod.md) |  | [optional] 
**prime_pco_cost** | **float** | Prime PCO Cost | [optional] 
**rfq_amount** | **float** | Request RFQ Amount | [optional] 
**rfq_sent** | **str** | RFQ status | [optional] 
**currency_configuration** | [**RFQCurrencyConfiguration**](RFQCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_change_events_get200_response_inner_change_event_line_items_inner import RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner from a JSON string
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_instance = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner.to_json())

# convert the object into a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_dict = rest_v10_change_events_get200_response_inner_change_event_line_items_inner_instance.to_dict()
# create an instance of RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner from a dict
rest_v10_change_events_get200_response_inner_change_event_line_items_inner_from_dict = RestV10ChangeEventsGet200ResponseInnerChangeEventLineItemsInner.from_dict(rest_v10_change_events_get200_response_inner_change_event_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


