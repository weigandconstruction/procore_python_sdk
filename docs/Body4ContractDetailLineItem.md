# Body4ContractDetailLineItem

The Detail Line Item object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_item_id** | **int** | Line Item ID | [optional] 
**amount** | **str** | Amount | [optional] 
**description** | **str** | Description | [optional] 

## Example

```python
from procore_sdk.models.body4_contract_detail_line_item import Body4ContractDetailLineItem

# TODO update the JSON string below
json = "{}"
# create an instance of Body4ContractDetailLineItem from a JSON string
body4_contract_detail_line_item_instance = Body4ContractDetailLineItem.from_json(json)
# print the JSON string representation of the object
print(Body4ContractDetailLineItem.to_json())

# convert the object into a dict
body4_contract_detail_line_item_dict = body4_contract_detail_line_item_instance.to_dict()
# create an instance of Body4ContractDetailLineItem from a dict
body4_contract_detail_line_item_from_dict = Body4ContractDetailLineItem.from_dict(body4_contract_detail_line_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


