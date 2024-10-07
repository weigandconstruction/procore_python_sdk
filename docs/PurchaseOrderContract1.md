# PurchaseOrderContract1

Purchase Order Contract object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounting_method** | **str** | Accounting method | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**assignee_id** | **int** | Assignee ID | [optional] 
**bill_to_address** | **str** | Bill to address | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**delivery_date** | **date** | Delivery date | [optional] 
**description** | **str** | Description | [optional] 
**executed** | **bool** | Executed status | [optional] 
**execution_date** | **date** | Execution date | [optional] 
**issued_on_date** | **date** | Issued on | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**number** | **str** | Number | [optional] 
**payment_terms** | **str** | Payment terms | [optional] 
**private** | **bool** | Enable/Disable private status | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**ship_to_address** | **str** | Ship to address | [optional] 
**ship_via** | **str** | Ship via | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 

## Example

```python
from procore_sdk.models.purchase_order_contract1 import PurchaseOrderContract1

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseOrderContract1 from a JSON string
purchase_order_contract1_instance = PurchaseOrderContract1.from_json(json)
# print the JSON string representation of the object
print(PurchaseOrderContract1.to_json())

# convert the object into a dict
purchase_order_contract1_dict = purchase_order_contract1_instance.to_dict()
# create an instance of PurchaseOrderContract1 from a dict
purchase_order_contract1_from_dict = PurchaseOrderContract1.from_dict(purchase_order_contract1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


