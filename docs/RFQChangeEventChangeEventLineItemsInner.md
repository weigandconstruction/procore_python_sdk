# RFQChangeEventChangeEventLineItemsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**cost_code_biller_name** | **str** | Cost Code biller name | [optional] 
**cost_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerCostCode.md) |  | [optional] 
**cost_code_is_budgeted** | **bool** | Cost Code budgeted status | [optional] 
**description** | **str** | Description | [optional] 
**event_id** | **int** | Event ID | [optional] 
**line_item_type** | [**LineItemType**](LineItemType.md) |  | [optional] 
**rom** | **int** | Rough order of magnitude (ROM) | [optional] 
**contract** | [**RFQChangeEventChangeEventLineItemsInnerContract**](RFQChangeEventChangeEventLineItemsInnerContract.md) |  | [optional] 
**links** | [**RFQChangeEventChangeEventLineItemsInnerLinks**](RFQChangeEventChangeEventLineItemsInnerLinks.md) |  | [optional] 
**statuses** | [**RFQChangeEventChangeEventLineItemsInnerStatuses**](RFQChangeEventChangeEventLineItemsInnerStatuses.md) |  | [optional] 
**number** | **str** | Number | [optional] 
**status** | **str** | Change Event Status name | [optional] 
**title** | **str** | Title | [optional] 
**vendor** | [**RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor**](RestV10ProjectsProjectIdWasteLogsGet200ResponseInnerVendor.md) |  | [optional] 
**commitment_contract_cost** | **str** | Commitment contract cost | [optional] 
**commitment_pco_cost** | **str** | Commitment Potential Change Order cost | [optional] 
**budget_mod_amount** | **str** | Budget Modification transfer amount | [optional] 
**budget_mod** | [**RFQChangeEventChangeEventLineItemsInnerBudgetMod**](RFQChangeEventChangeEventLineItemsInnerBudgetMod.md) |  | [optional] 
**prime_pco_cost** | **str** | Prime Potential Change Order cost | [optional] 
**rfq_amount** | **str** | RFQ amount | [optional] 
**rfq_status** | **str** | RFQ status | [optional] 

## Example

```python
from procore_sdk.models.rfq_change_event_change_event_line_items_inner import RFQChangeEventChangeEventLineItemsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RFQChangeEventChangeEventLineItemsInner from a JSON string
rfq_change_event_change_event_line_items_inner_instance = RFQChangeEventChangeEventLineItemsInner.from_json(json)
# print the JSON string representation of the object
print(RFQChangeEventChangeEventLineItemsInner.to_json())

# convert the object into a dict
rfq_change_event_change_event_line_items_inner_dict = rfq_change_event_change_event_line_items_inner_instance.to_dict()
# create an instance of RFQChangeEventChangeEventLineItemsInner from a dict
rfq_change_event_change_event_line_items_inner_from_dict = RFQChangeEventChangeEventLineItemsInner.from_dict(rfq_change_event_change_event_line_items_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


