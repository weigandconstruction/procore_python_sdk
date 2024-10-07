# Commitment1PaymentsIssuedInner

Contract Payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**amount** | **str** | Payment amount | [optional] 
**check_number** | **str** | Check number | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Payment date | [optional] 
**draw_request_number** | **int** | Payment number of a Draw Request, Owner Invoice, or Subcontractor Invoice | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**notes** | **str** | Associated notes | [optional] 
**payment_number** | **int** | Payment number | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Payment attachments | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**origin_data** | **str** | Origin data | [optional] 

## Example

```python
from procore_sdk.models.commitment1_payments_issued_inner import Commitment1PaymentsIssuedInner

# TODO update the JSON string below
json = "{}"
# create an instance of Commitment1PaymentsIssuedInner from a JSON string
commitment1_payments_issued_inner_instance = Commitment1PaymentsIssuedInner.from_json(json)
# print the JSON string representation of the object
print(Commitment1PaymentsIssuedInner.to_json())

# convert the object into a dict
commitment1_payments_issued_inner_dict = commitment1_payments_issued_inner_instance.to_dict()
# create an instance of Commitment1PaymentsIssuedInner from a dict
commitment1_payments_issued_inner_from_dict = Commitment1PaymentsIssuedInner.from_dict(commitment1_payments_issued_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


