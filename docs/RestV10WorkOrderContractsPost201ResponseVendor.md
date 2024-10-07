# RestV10WorkOrderContractsPost201ResponseVendor

Vendor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**company** | **str** | Company | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_work_order_contracts_post201_response_vendor import RestV10WorkOrderContractsPost201ResponseVendor

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10WorkOrderContractsPost201ResponseVendor from a JSON string
rest_v10_work_order_contracts_post201_response_vendor_instance = RestV10WorkOrderContractsPost201ResponseVendor.from_json(json)
# print the JSON string representation of the object
print(RestV10WorkOrderContractsPost201ResponseVendor.to_json())

# convert the object into a dict
rest_v10_work_order_contracts_post201_response_vendor_dict = rest_v10_work_order_contracts_post201_response_vendor_instance.to_dict()
# create an instance of RestV10WorkOrderContractsPost201ResponseVendor from a dict
rest_v10_work_order_contracts_post201_response_vendor_from_dict = RestV10WorkOrderContractsPost201ResponseVendor.from_dict(rest_v10_work_order_contracts_post201_response_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


