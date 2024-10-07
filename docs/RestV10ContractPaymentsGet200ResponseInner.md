# RestV10ContractPaymentsGet200ResponseInner

Contract Payment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**amount** | **str** | Payment amount | [optional] 
**check_number** | **str** | Check number | [optional] 
**contract_id** | **int** | Contract ID associated with the payment | [optional] 
**created_at** | **datetime** | Created at | [optional] 
**var_date** | **date** | Payment Date | [optional] 
**date_payment_settled** | **datetime** | Date Payment settled | [optional] 
**date_payment_initiated** | **datetime** | Date Payment Initiated | [optional] 
**draw_request_number** | **int** | Payment number of a Draw Request, Owner Invoice, or Subcontractor Invoice | [optional] 
**external_payment_id** | **str** | Only payments made through Procore Pay have an external_payment_id | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**notes** | **str** | Associated notes | [optional] 
**payment_number** | **int** | Payment number | [optional] 
**attachments** | [**List[RestV10WorkOrderContractsPost201ResponseAttachmentsInner]**](RestV10WorkOrderContractsPost201ResponseAttachmentsInner.md) | Payment attachments | [optional] 
**project_id** | **int** | Integer ID for the associated Project | [optional] 
**requisition_id** | **int** | Invoice ID | [optional] 
**origin_id** | **str** | Origin ID | [optional] 
**origin_code** | **str** | Origin Code | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**status** | **str** | Status | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_contract_payments_get200_response_inner import RestV10ContractPaymentsGet200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10ContractPaymentsGet200ResponseInner from a JSON string
rest_v10_contract_payments_get200_response_inner_instance = RestV10ContractPaymentsGet200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(RestV10ContractPaymentsGet200ResponseInner.to_json())

# convert the object into a dict
rest_v10_contract_payments_get200_response_inner_dict = rest_v10_contract_payments_get200_response_inner_instance.to_dict()
# create an instance of RestV10ContractPaymentsGet200ResponseInner from a dict
rest_v10_contract_payments_get200_response_inner_from_dict = RestV10ContractPaymentsGet200ResponseInner.from_dict(rest_v10_contract_payments_get200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


