# RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**standard_cost_code_list_id** | **int** | Standard Cost Code List ID | [optional] 
**parent_id** | **int** | Parent ID | [optional] 
**code** | **str** | Cost code, not including parent prefix | [optional] 
**full_code** | **str** | Cost code, including parent prefixes | [optional] 
**name** | **str** | Description | [optional] 
**origin_data** | **str** | Origin data | [optional] 
**origin_id** | **str** | Origin ID | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner import RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner from a JSON string
rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner_instance = RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner.from_json(json)
# print the JSON string representation of the object
print(RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner.to_json())

# convert the object into a dict
rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner_dict = rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner_instance.to_dict()
# create an instance of RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner from a dict
rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner_from_dict = RestV10VendorsIdGet200ResponseOneOf1AllOfStandardCostCodesInner.from_dict(rest_v10_vendors_id_get200_response_one_of1_all_of_standard_cost_codes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


