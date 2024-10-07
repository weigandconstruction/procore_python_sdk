# StandardCostCodeList3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**is_erp_list** | **bool** | Standard Cost Code List ERP Integrated | [optional] 
**name** | **str** | Name | [optional] 
**company_id** | **int** | Company ID | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code_list3 import StandardCostCodeList3

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCodeList3 from a JSON string
standard_cost_code_list3_instance = StandardCostCodeList3.from_json(json)
# print the JSON string representation of the object
print(StandardCostCodeList3.to_json())

# convert the object into a dict
standard_cost_code_list3_dict = standard_cost_code_list3_instance.to_dict()
# create an instance of StandardCostCodeList3 from a dict
standard_cost_code_list3_from_dict = StandardCostCodeList3.from_dict(standard_cost_code_list3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


