# StandardCostCodeList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_to_use_on_new_projects** | **bool** | Standard Cost Code List can be used on new projects | [optional] 
**id** | **int** | Unique identifier for the Standard Cost Code List | [optional] 
**is_erp_list** | **bool** | Standard Cost Code List ERP Integrated | [optional] 
**name** | **str** | Name | [optional] 

## Example

```python
from procore_sdk.models.standard_cost_code_list import StandardCostCodeList

# TODO update the JSON string below
json = "{}"
# create an instance of StandardCostCodeList from a JSON string
standard_cost_code_list_instance = StandardCostCodeList.from_json(json)
# print the JSON string representation of the object
print(StandardCostCodeList.to_json())

# convert the object into a dict
standard_cost_code_list_dict = standard_cost_code_list_instance.to_dict()
# create an instance of StandardCostCodeList from a dict
standard_cost_code_list_from_dict = StandardCostCodeList.from_dict(standard_cost_code_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


