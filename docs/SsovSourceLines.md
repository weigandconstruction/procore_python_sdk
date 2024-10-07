# SsovSourceLines

Line Item (when the 'ssov_source_lines' view is requested)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Line Item id | [optional] 
**amount** | **str** | Line Item amount | [optional] 
**description** | **str** | Line Item description | [optional] 
**position** | **int** | Line Item position | [optional] 
**wbs_code** | [**RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode**](RestV10WorkOrderContractsPost201ResponseLineItemsInnerWbsCode.md) |  | [optional] 
**currency_configuration** | [**RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration**](RestV10WorkOrderContractsGet200ResponseInnerCurrencyConfiguration.md) |  | [optional] 

## Example

```python
from procore_sdk.models.ssov_source_lines import SsovSourceLines

# TODO update the JSON string below
json = "{}"
# create an instance of SsovSourceLines from a JSON string
ssov_source_lines_instance = SsovSourceLines.from_json(json)
# print the JSON string representation of the object
print(SsovSourceLines.to_json())

# convert the object into a dict
ssov_source_lines_dict = ssov_source_lines_instance.to_dict()
# create an instance of SsovSourceLines from a dict
ssov_source_lines_from_dict = SsovSourceLines.from_dict(ssov_source_lines_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


