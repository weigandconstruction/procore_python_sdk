# RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | Name of the Business | [optional] 
**dba** | **str** | Business Name DBA (Doing Business As) | [optional] 
**logo_url** | **str** |  | [optional] 
**primary_slug** | **str** | Slug for Business | [optional] 
**construction_sectors** | **List[str]** | Construction Sectors this Business works in | [optional] 
**business_types** | **List[str]** | Business Types this Business falls under | [optional] 
**provided_services** | [**List[BusinessNormalViewProvidedServicesInner]**](BusinessNormalViewProvidedServicesInner.md) | Services the Business Provides | [optional] 
**avg_contract_size** | [**RestV10VendorsIdGet200ResponseOneOf1AllOfBusinessAvgContractSize**](RestV10VendorsIdGet200ResponseOneOf1AllOfBusinessAvgContractSize.md) |  | [optional] 
**company_size** | [**RestV10VendorsIdGet200ResponseOneOf1AllOfBusinessCompanySize**](RestV10VendorsIdGet200ResponseOneOf1AllOfBusinessCompanySize.md) |  | [optional] 

## Example

```python
from procore_sdk.models.rest_v10_vendors_id_get200_response_one_of1_all_of_business import RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness

# TODO update the JSON string below
json = "{}"
# create an instance of RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness from a JSON string
rest_v10_vendors_id_get200_response_one_of1_all_of_business_instance = RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness.from_json(json)
# print the JSON string representation of the object
print(RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness.to_json())

# convert the object into a dict
rest_v10_vendors_id_get200_response_one_of1_all_of_business_dict = rest_v10_vendors_id_get200_response_one_of1_all_of_business_instance.to_dict()
# create an instance of RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness from a dict
rest_v10_vendors_id_get200_response_one_of1_all_of_business_from_dict = RestV10VendorsIdGet200ResponseOneOf1AllOfBusiness.from_dict(rest_v10_vendors_id_get200_response_one_of1_all_of_business_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


