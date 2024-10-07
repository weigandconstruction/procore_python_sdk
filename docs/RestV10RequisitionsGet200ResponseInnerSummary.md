# RestV10RequisitionsGet200ResponseInnerSummary

Requisition (Subcontractor Invoice) summary (present in all views)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balance_to_finish_including_retainage** | **str** | Balance to finish including retainage | [optional] 
**completed_work_retainage_percent** | **str** | Completed work retainage percent | [optional] 
**completed_work_retainage_amount** | **str** | Completed work retainage amount | [optional] 
**contract_sum_to_date** | **str** | Contract sum to date | [optional] 
**current_payment_due** | **str** | Current payment due | [optional] 
**formatted_period** | **str** | Formatted billing period | [optional] 
**less_previous_certificates_for_payment** | **str** | Less previous certificates for payment | [optional] 
**negative_change_order_item_total** | **str** | Negative change order item total | [optional] 
**negative_new_change_order_item_total** | **str** | Negative new change order item total | [optional] 
**negative_previous_change_order_item_total** | **str** | Negative previous change order item total | [optional] 
**net_change_by_change_orders** | **str** | Net change by change orders | [optional] 
**original_contract_sum** | **str** | Original contract sum | [optional] 
**positive_change_order_item_total** | **str** | Positive change order item total | [optional] 
**positive_new_change_order_item_total** | **str** | Positive new change order item total | [optional] 
**positive_previous_change_order_item_total** | **str** | Positive previous change order item total | [optional] 
**stored_materials_retainage_amount** | **str** | Stored materials retainage amount | [optional] 
**stored_materials_retainage_percent** | **str** | Stored materials retainage percent | [optional] 
**tax_applicable_to_this_payment** | **str** | Tax applicable to this payment | [optional] 
**total_completed_and_stored_to_date** | **str** | Total completed and stored to date | [optional] 
**total_earned_less_retainage** | **str** | Total earned less retainage | [optional] 
**total_retainage** | **str** | Total retainage | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_requisitions_get200_response_inner_summary import RestV10RequisitionsGet200ResponseInnerSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10RequisitionsGet200ResponseInnerSummary from a JSON string
rest_v10_requisitions_get200_response_inner_summary_instance = RestV10RequisitionsGet200ResponseInnerSummary.from_json(json)
# print the JSON string representation of the object
print(RestV10RequisitionsGet200ResponseInnerSummary.to_json())

# convert the object into a dict
rest_v10_requisitions_get200_response_inner_summary_dict = rest_v10_requisitions_get200_response_inner_summary_instance.to_dict()
# create an instance of RestV10RequisitionsGet200ResponseInnerSummary from a dict
rest_v10_requisitions_get200_response_inner_summary_from_dict = RestV10RequisitionsGet200ResponseInnerSummary.from_dict(rest_v10_requisitions_get200_response_inner_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


