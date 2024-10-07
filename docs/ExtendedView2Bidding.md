# ExtendedView2Bidding

Bidding status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affirmative_action** | **bool** |  | [optional] 
**small_business** | **bool** |  | [optional] 
**african_american_business** | **bool** |  | [optional] 
**hispanic_business** | **bool** |  | [optional] 
**womens_business** | **bool** |  | [optional] 
**historically_underutilized_business** | **bool** |  | [optional] 
**sdvo_business** | **bool** |  | [optional] 
**certified_business_enterprise** | **bool** |  | [optional] 
**asian_american_business** | **bool** |  | [optional] 
**native_american_business** | **bool** |  | [optional] 
**disadvantaged_business** | **bool** |  | [optional] 
**minority_business_enterprise** | **bool** |  | [optional] 
**eight_a_business** | **bool** |  | [optional] 

## Example

```python
from procore_sdk.models.extended_view2_bidding import ExtendedView2Bidding

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedView2Bidding from a JSON string
extended_view2_bidding_instance = ExtendedView2Bidding.from_json(json)
# print the JSON string representation of the object
print(ExtendedView2Bidding.to_json())

# convert the object into a dict
extended_view2_bidding_dict = extended_view2_bidding_instance.to_dict()
# create an instance of ExtendedView2Bidding from a dict
extended_view2_bidding_from_dict = ExtendedView2Bidding.from_dict(extended_view2_bidding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


