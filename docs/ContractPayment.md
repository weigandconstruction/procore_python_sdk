# ContractPayment

Contract Payment object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Payment date | [optional] 
**invoice_number** | **str** | Invoice number | [optional] 
**check_number** | **str** | Check number | [optional] 
**invoice_date** | **date** | Invoice date | [optional] 
**draw_request_number** | **int** | Draw Request number | [optional] 
**notes** | **str** | Associated notes | [optional] 
**payment_number** | **int** | Payment number | [optional] 
**payment_method** | **str** | Payment method | [optional] 
**amount** | **str** | Payment amount | [optional] 
**origin_id** | **str** | Contract payment third party ID | [optional] 
**origin_data** | **str** | Contract payment third party data | [optional] 
**prostore_file_ids** | **List[int]** | Any prostore files to actualize contract payment&#39;s attachments. Mutually exclusive with the &#x60;attachments&#x60; property. | [optional] 

## Example

```python
from procore_sdk.models.contract_payment import ContractPayment

# TODO update the JSON string below
json = "{}"
# create an instance of ContractPayment from a JSON string
contract_payment_instance = ContractPayment.from_json(json)
# print the JSON string representation of the object
print(ContractPayment.to_json())

# convert the object into a dict
contract_payment_dict = contract_payment_instance.to_dict()
# create an instance of ContractPayment from a dict
contract_payment_from_dict = ContractPayment.from_dict(contract_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


