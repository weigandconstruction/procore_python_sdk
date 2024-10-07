# WorkOrderContract1

Work Order Contract object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**accounting_method** | **str** | Accounting method | [optional] 
**actual_completion_date** | **date** | Actual completion date | [optional] 
**approval_letter_date** | **str** | Approval letter date | [optional] 
**contract_date** | **date** | Contract date | [optional] 
**contract_estimated_completion_date** | **date** | Estimated completion date | [optional] 
**contract_start_date** | **date** | Start Date | [optional] 
**description** | **str** | Description | [optional] 
**exclusions** | **str** | Exclusions | [optional] 
**executed** | **bool** | Executed (or not) | [optional] [default to False]
**execution_date** | **date** | Execution date | [optional] 
**inclusions** | **str** | Inclusions | [optional] 
**issued_on_date** | **date** | Issued on date | [optional] 
**letter_of_intent_date** | **date** | Letter of intent date | [optional] 
**origin_code** | **str** | Origin code | [optional] 
**origin_data** | **str** | Origin Data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**number** | **str** | Number | [optional] 
**private** | **bool** | If true, visible to admins and whitelisted accessors; otherwise visible to those with read only access. | [optional] 
**retainage_percent** | **str** | Retainage percent | [optional] 
**returned_date** | **date** | Returned date | [optional] 
**signed_contract_received_date** | **date** | Signed contract received date | [optional] 
**status** | **str** | Status | [optional] 
**title** | **str** | Title | [optional] 
**vendor_id** | **int** | Vendor ID | [optional] 

## Example

```python
from procore_sdk.models.work_order_contract1 import WorkOrderContract1

# TODO update the JSON string below
json = "{}"
# create an instance of WorkOrderContract1 from a JSON string
work_order_contract1_instance = WorkOrderContract1.from_json(json)
# print the JSON string representation of the object
print(WorkOrderContract1.to_json())

# convert the object into a dict
work_order_contract1_dict = work_order_contract1_instance.to_dict()
# create an instance of WorkOrderContract1 from a dict
work_order_contract1_from_dict = WorkOrderContract1.from_dict(work_order_contract1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


