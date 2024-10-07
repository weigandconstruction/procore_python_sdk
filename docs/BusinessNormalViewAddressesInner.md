# BusinessNormalViewAddressesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID for the address | [optional] 
**name** | **str** | Address Name | [optional] 
**address1** | **str** | Business Street Address | [optional] 
**address2** | **str** | Street Address Line 2 | [optional] 
**city** | **str** | Address City | [optional] 
**latitude** | **float** | Latitude of the Address | [optional] 
**longitude** | **float** | Longitude of the Address | [optional] 
**province** | **str** | Address State or Province | [optional] 
**postal_code1** | **str** | Address Primary Zip Code or Other Postal Code | [optional] 
**country_code** | **str** | Country Code | [optional] 
**phone_number** | **str** | Business Phone Number | [optional] 
**fax_number** | **str** | Business Fax Number | [optional] 
**primary** | **bool** | Indicates whether this is the primary address for the Business. This is also the Main Office of the company. | [optional] 
**address_types** | **List[str]** | Address Types | [optional] 

## Example

```python
from procore_sdk.models.business_normal_view_addresses_inner import BusinessNormalViewAddressesInner

# TODO update the JSON string below
json = "{}"
# create an instance of BusinessNormalViewAddressesInner from a JSON string
business_normal_view_addresses_inner_instance = BusinessNormalViewAddressesInner.from_json(json)
# print the JSON string representation of the object
print(BusinessNormalViewAddressesInner.to_json())

# convert the object into a dict
business_normal_view_addresses_inner_dict = business_normal_view_addresses_inner_instance.to_dict()
# create an instance of BusinessNormalViewAddressesInner from a dict
business_normal_view_addresses_inner_from_dict = BusinessNormalViewAddressesInner.from_dict(business_normal_view_addresses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


